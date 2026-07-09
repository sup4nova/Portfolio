"""Compatibility scoring for the "Are we a match?" quiz.

Technical fit blends two signals: fixed weights for the chip/scale answers,
and a TF-IDF cosine similarity between the candidate's free-text goal and a
short corpus describing my actual skills/projects per category. Culture fit
is weights only — there's no free text to compare there.

The free-text goal is also checked against a "dealbreaker" corpus (support
roles, on-call pressure, fake remote, etc.) independent of whatever focus
chips were picked, since a recruiter can tick "dev" and still describe a
support-heavy role in their own words. Both corpora are fit into the same
TF-IDF vector space so shared vocabulary (e.g. "remote" showing up in both a
genuine remote pitch and the fake-remote red flag) gets weighted down by
document frequency instead of causing false positives.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from schemas import MatchRequest, MatchResponse

FOCUS_WEIGHTS = {
    "ai": 90,
    "automation": 90,
    "cyber": 92,
    "creative": 88,
    "dev": 88,
    "support": 15,
    "other": 60,
}

FOCUS_CORPUS = {
    "ai": "AI and machine learning integration, LLM APIs like Claude and ChatGPT, "
          "multimodal analysis of music and images, AI-assisted workflows.",
    "automation": "Automation and workflows, scripting, PowerShell, job scraping and "
                  "CV generation tooling, conversational bots and chat integrations, "
                  "cutting down repetitive manual work.",
    "cyber": "Cybersecurity, AES encryption and decryption tooling, CTFs, bug bounty "
             "initiation, secure coding, cryptography, Java security tools.",
    "creative": "Audio and sound design, music analysis, valence-arousal emotion "
                "mapping, generative audio tracks from images and video.",
    "dev": "Frontend and backend web development, Vue 3, TypeScript, Vite, Node.js, "
           "Python, Java, building and shipping full applications end to end.",
    "support": "Customer support, technical support, troubleshooting, user experience "
               "improvements, helping users get the most out of software.",
    "other": "Other skills and interests, miscellaneous projects, generalist capabilities.",
}

# Ids scored purely as a technical-fit signal — "support"/"other" are excluded
# since they aren't a positive direction, just neutral filler categories.
POSITIVE_FOCUS_IDS = ["ai", "automation", "cyber", "creative", "dev"]

# Free-text signals that should pull the score down regardless of which focus
# chips were checked.
DEALBREAKER_CORPUS = {
    "support": "Customer support, client-facing support, phone support, ticket "
               "queues, help desk, customer success, player support, being the "
               "direct point of contact for customers all day, every day.",
    "relational_role": "Sales engineer, solutions engineer, account management, "
                        "stakeholder management, client relationship building, "
                        "sales-driven technical role, traditional project management "
                        "with constant meetings and stakeholders.",
    "oncall_pressure": "24/7 on-call rotations, being paged at night, high-pressure "
                        "production incidents, crunch time, burnout culture, "
                        "always-on availability expectations.",
    "leetcode": "Whiteboard algorithm interviews, LeetCode-style coding challenges, "
                "competitive programming interview process, algorithmic trivia.",
    "fake_remote": "Position advertised as remote but actually requiring relocation "
                    "to headquarters, mandatory visa sponsorship, local residency "
                    "required, native language fluency expected, frequent mandatory "
                    "office attendance despite the remote label.",
    "stagnation": "Repetitive maintenance work, no growth opportunities, legacy "
                  "codebase with no innovation, stagnant role with minimal learning "
                  "or mentorship.",
}

WORKSTYLE_WEIGHTS = {
    "startup": 90,
    "structured": 88,
    "remote": 100,
    "inperson": 65,
}

TEAMVALUES_WEIGHTS = {
    "autonomy": 95,
    "ownership": 92,
    "crossteam": 85,
    "speed": 88,
    "internationals": 95,
}

TEAMSIZE_WEIGHTS = {
    "solo": 90,
    "small": 70,
    "scaleup": 95,
    "enterprise": 88,
}

# Single shared TF-IDF space for both corpora — fitting them together means a
# word appearing in both (e.g. "remote") gets a realistic document frequency
# instead of looking uniquely distinctive to whichever corpus it's compared
# against in isolation.
_FOCUS_IDS = list(FOCUS_CORPUS.keys())
_DEALBREAKER_IDS = list(DEALBREAKER_CORPUS.keys())
_ALL_TEXTS = list(FOCUS_CORPUS.values()) + list(DEALBREAKER_CORPUS.values())
_vectorizer = TfidfVectorizer(stop_words="english")
_all_vectors = _vectorizer.fit_transform(_ALL_TEXTS)
_focus_vectors = _all_vectors[: len(_FOCUS_IDS)]
_dealbreaker_vectors = _all_vectors[len(_FOCUS_IDS):]


def _avg(values: list[float], fallback: float = 70.0) -> float:
    return sum(values) / len(values) if values else fallback


def _similarities(goal: str) -> dict[str, float] | None:
    goal = goal.strip()
    if not goal:
        return None
    goal_vector = _vectorizer.transform([goal])
    focus_sims = cosine_similarity(goal_vector, _focus_vectors)[0]
    dealbreaker_sims = cosine_similarity(goal_vector, _dealbreaker_vectors)[0]
    # Short free-text vs a short corpus rarely scores above ~0.3-0.4 cosine
    # similarity even on a strong match, so scale generously and cap at 100.
    scaled = {cat: max(0.0, min(100.0, s * 220)) for cat, s in zip(_FOCUS_IDS, focus_sims)}
    scaled.update({cat: max(0.0, min(100.0, s * 220)) for cat, s in zip(_DEALBREAKER_IDS, dealbreaker_sims)})
    return scaled


def _semantic_score(similarities: dict[str, float], focus: list[str]) -> float:
    relevant_ids = [f for f in focus if f in FOCUS_CORPUS] or POSITIVE_FOCUS_IDS
    return _avg([similarities[cat] for cat in relevant_ids])


def _dealbreaker_penalty(similarities: dict[str, float]) -> float:
    best_positive = max(similarities[cat] for cat in POSITIVE_FOCUS_IDS)
    worst_dealbreaker = max(similarities[cat] for cat in _DEALBREAKER_IDS)

    margin = worst_dealbreaker - best_positive
    if margin <= 5:
        return 0.0
    return min(0.85, margin / 60)


def _result_meta(score: int) -> tuple[str, str]:
    if score >= 85:
        return "Strong match", "That's a real overlap — let's talk."
    if score >= 70:
        return "Good overlap", "Worth a conversation, most of it lines up."
    if score >= 50:
        return "Some alignment", "A few gaps, but the core direction fits."
    return "Different wavelengths", "Not an obvious fit — but I'm always up for a chat."


def compute_match(payload: MatchRequest) -> MatchResponse:
    chip_score = _avg([FOCUS_WEIGHTS[f] for f in payload.focus if f in FOCUS_WEIGHTS], fallback=65.0)
    scale_score = 100 - abs(payload.aiNative - 3) * 15
    base_tech = (chip_score + scale_score) / 2

    similarities = _similarities(payload.goal)
    if similarities is not None:
        semantic = _semantic_score(similarities, payload.focus)
        tech_score = round(0.6 * base_tech + 0.4 * semantic)
    else:
        tech_score = round(base_tech)

    culture_score = round(_avg([
        _avg([WORKSTYLE_WEIGHTS[w] for w in payload.workStyle if w in WORKSTYLE_WEIGHTS]),
        _avg([TEAMVALUES_WEIGHTS[t] for t in payload.teamValues if t in TEAMVALUES_WEIGHTS]),
        _avg([TEAMSIZE_WEIGHTS[payload.teamSize]] if payload.teamSize in TEAMSIZE_WEIGHTS else [], fallback=70.0),
    ]))

    if similarities is not None:
        penalty = _dealbreaker_penalty(similarities)
        if penalty:
            tech_score = round(tech_score * (1 - penalty))
            culture_score = round(culture_score * (1 - penalty))

    overall = round((tech_score + culture_score) / 2)
    tag, message = _result_meta(overall)

    return MatchResponse(
        techScore=tech_score,
        cultureScore=culture_score,
        overall=overall,
        tag=tag,
        message=message,
    )
