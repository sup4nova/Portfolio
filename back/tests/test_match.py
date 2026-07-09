from fastapi.testclient import TestClient

from main import app
from match import compute_match
from schemas import MatchRequest

client = TestClient(app)


def test_match_endpoint_returns_scores_in_range():
    res = client.post("/match", json={
        "goal": "We need someone to automate our support workflows with LLMs",
        "focus": ["automation", "ai"],
        "aiNative": 4,
        "workStyle": ["remote"],
        "teamValues": ["autonomy"],
        "teamSize": "small",
    })
    assert res.status_code == 200
    body = res.json()
    for key in ("techScore", "cultureScore", "overall"):
        assert 0 <= body[key] <= 100
    assert body["tag"]
    assert body["message"]


def test_match_endpoint_accepts_empty_payload():
    res = client.post("/match", json={})
    assert res.status_code == 200


def test_match_rejects_invalid_ai_native():
    res = client.post("/match", json={"aiNative": 9})
    assert res.status_code == 422


def test_relevant_goal_scores_higher_than_off_topic_goal():
    relevant = compute_match(MatchRequest(
        goal="Looking for help automating internal tooling with LLM integrations",
        focus=["automation", "ai"],
    ))
    off_topic = compute_match(MatchRequest(
        goal="We need a truck driver for our logistics fleet",
        focus=["automation", "ai"],
    ))
    assert relevant.techScore > off_topic.techScore


def test_empty_goal_falls_back_to_chip_weights_only():
    result = compute_match(MatchRequest(focus=["cyber"], aiNative=3))
    # cyber chip weight (92) averaged with a neutral scale score (100) -> 96
    assert result.techScore == 96


def test_dealbreaker_role_scores_low_even_with_matching_chips():
    # Chips say "dev" but the free text describes exactly what should be avoided.
    result = compute_match(MatchRequest(
        goal=(
            "Looking for a developer, you'll also handle customer support "
            "tickets and phone calls with clients daily, plus 24/7 on-call rotations"
        ),
        focus=["dev", "automation"],
        aiNative=4,
        workStyle=["remote"],
        teamValues=["autonomy"],
        teamSize="small",
    ))
    assert result.overall < 30
    assert result.tag == "Different wavelengths"


def test_genuine_remote_role_is_not_penalized_as_fake_remote():
    # "remote" appears in both the real pitch and the fake-remote red flag
    # corpus — a legitimate remote role must not get dragged down by that.
    result = compute_match(MatchRequest(
        goal=(
            "We're building LLM-powered automation, fully remote, "
            "you'd own the whole pipeline end to end"
        ),
        focus=["automation", "ai"],
        aiNative=4,
        workStyle=["remote"],
        teamValues=["autonomy", "ownership"],
        teamSize="small",
    ))
    assert result.overall >= 70


def test_leetcode_red_flag_detected_within_an_otherwise_good_pitch():
    result = compute_match(MatchRequest(
        goal=(
            "We're looking for an automation engineer, note our interview "
            "process includes several rounds of LeetCode-style algorithm challenges"
        ),
        focus=["automation", "dev"],
        aiNative=3,
        workStyle=["remote"],
        teamValues=["ownership"],
        teamSize="scaleup",
    ))
    assert result.overall < 30
