<!-- CareerLedger.vue -->

<script setup lang="ts">
import { ref, computed } from 'vue'

type Kind = 'Work' | 'Apprenticeship' | 'Internship' | 'Education'

interface Experience {
  kind: Kind
  accent: string
  symbol: string
  startDate: string
  endDate: string | null
  role: string
  org: string
  orgUrl?: string
  city: string
  honors?: string
  desc: string
  highlights?: string[]
  stack: string[]
  stackLabel?: string
}

const experiences: Experience[] = [
  {
    kind: 'Work',
    accent: '#cbff48',
    symbol: '◉',
    startDate: '12/2025',
    endDate: null,
    role: 'Customer Care & Technical Support',
    org: 'TEC3H',
    city: 'Rennes, FR',
    desc: 'Handled multi-channel customer and technical support operations, managing the full lifecycle of platform sessions, partner integrations, and L1/L2 issue resolution in an SLA-driven environment.',
    highlights: [
      'Managed support across phone, ticketing, email, WhatsApp & web',
      '~15–20 calls/day with autonomous prioritization & follow-up',
      'Session lifecycle management: activation, maintenance & deactivation',
      'Created and shared partner API access via Postman',
      'Collaborated with Sales, QA & Development on complex incidents',
      'Maintained FAQ / knowledge base documentation',
    ],
    stack: [
      'Technical Support',
      'L1/L2',
      'Postman',
      'API Setup',
      'SLA',
      'Knowledge Base',
      'Customer Success',
      'OVH Cloud',
      'Filezilla',
    ],
  },

  {
    kind: 'Apprenticeship',
    accent: '#5ee9c8',
    symbol: '◐',
    startDate: '10/2024',
    endDate: '08/2025',
    role: 'IT Support Engineer',
    org: 'Contentsquare',
    city: 'Paris, FR',
    desc: 'Delivered L1/L2 internal IT support in a fast-paced international environment, administering IAM, endpoints, SaaS access, and employee lifecycle operations while contributing to automation and IT projects.',
    highlights: [
      'L1/L2 support via Jira Service Management',
      'IAM & endpoint administration: Okta, Jamf & Google Admin',
      'Provisioned Slack, Zoom, Jira & SaaS access',
      'Managed onboarding/offboarding & hardware lifecycle',
      'Automated onboarding workflows with Python & PowerShell',
      'Contributed to London stock audit & Rennes office move',
    ],
    stack: [
      'Jira SM',
      'Okta',
      'Jamf',
      'Google Admin',
      'Snipe-IT',
      'Python',
      'PowerShell',
      'macOS',
      'Windows',
      'Zoom',
      'Slack',
    ],
  },

  {
    kind: 'Internship',
    accent: '#00bb81',
    symbol: '◇',
    startDate: '05/2024',
    endDate: '06/2024',
    role: 'Cybersecurity / Information Security Intern',
    org: 'Eviden (Atos)',
    city: 'Rennes, FR',
    desc: 'Developed a PowerShell-based compliance auditing solution to validate firewall rules against network flow matrices, simplifying security verification workflows for technical and non-technical teams.',
    highlights: [
      'Built repeatable compliance checks for firewall verification',
      'Designed JSON-based configuration with zero code edits',
      'Developed a PowerShell GUI for non-technical users',
      'Produced bilingual FR/EN documentation',
      'Standardized internal security control processes',
    ],
    stack: [
      'PowerShell',
      'JSON',
      'GUI',
      'Firewall Audit',
      'Network Security',
      'Automation',
      'Documentation',
    ],
  },

  {
    kind: 'Education',
    accent: 'rgba(255,255,255,.72)',
    symbol: '✦',
    startDate: '09/2024',
    endDate: '08/2025',
    role: 'BTS SIO - SLAM (Cybersecurity Focus)',
    org: 'ESNA Bretagne',
    city: 'Rennes, FR',
    honors: 'Completed',
    desc: 'Second-year specialization in software solutions, cybersecurity, and professional IT operations completed through apprenticeship.',
    stack: [
      'Cybersecurity',
      'Software Development',
      'Systems',
      'Networks',
      'Professional Practice',
    ],
    stackLabel: 'Curriculum',
  },

  {
    kind: 'Education',
    accent: 'rgba(255,255,255,.72)',
    symbol: '✦',
    startDate: '09/2023',
    endDate: '08/2024',
    role: 'BTS SIO - SLAM',
    org: 'Lycée Victor et Hélène Basch',
    city: 'Rennes, FR',
    honors: 'First Year',
    desc: 'First year of the French BTS SIO diploma focused on software solutions, business applications, networking fundamentals, and IT project methodologies.',
    stack: [
      'Software Development',
      'SQL',
      'Networking',
      'Project Management',
      'Business Applications',
    ],
    stackLabel: 'Curriculum',
  },

  {
    kind: 'Education',
    accent: 'rgba(255,255,255,.55)',
    symbol: '✧',
    startDate: '09/2022',
    endDate: '08/2023',
    role: 'LLCER English - First Year',
    org: 'Université Rennes 2',
    city: 'Rennes, FR',
    desc: 'Undergraduate studies in English language, literature and intercultural communication.',
    stack: [
      'English',
      'Communication',
      'Literature',
      'Intercultural Studies',
    ],
    stackLabel: 'Studies',
  },

  {
    kind: 'Education',
    accent: 'rgba(255,255,255,.45)',
    symbol: '✧',
    startDate: '09/2019',
    endDate: '08/2022',
    role: 'French Baccalauréat Général',
    org: 'Lycée Kerneuzec',
    city: 'Quimperlé, FR',
    honors: 'Mathematics · Physics-Chemistry · SVT',
    desc: 'General French high school diploma with scientific specialization in mathematics, physics-chemistry and life sciences.',
    stack: [
      'Mathematics',
      'Physics',
      'Chemistry',
      'Biology',
    ],
    stackLabel: 'Specialties',
  },
]

const kinds: Kind[] = ['Work', 'Apprenticeship', 'Internship', 'Education']
const activeFilter = ref<Kind | 'All'>('All')

const sortedExperiences = [...experiences].sort((a, b) => {
  const [am, ay] = a.startDate.split('/')
  const [bm, by] = b.startDate.split('/')

  return (
    new Date(`${by}-${bm}-01`).getTime() -
    new Date(`${ay}-${am}-01`).getTime()
  )
})

const filtered = computed(() =>
  activeFilter.value === 'All'
    ? sortedExperiences
    : sortedExperiences.filter(e => e.kind === activeFilter.value)
)

function countOf(k: Kind) {
  return experiences.filter(e => e.kind === k).length
}

function duration(start: string, end: string | null) {
  const startParts = start.split('/').map(Number)

  const sm = startParts[0] ?? 1
  const sy = startParts[1] ?? new Date().getFullYear()

  const startDate = new Date(sy, sm - 1)

  let endDate: Date

  if (end) {
    const endParts = end.split('/').map(Number)

    const em = endParts[0] ?? 1
    const ey = endParts[1] ?? new Date().getFullYear()

    endDate = new Date(ey, em - 1)
  } else {
    endDate = new Date()
  }

  const months =
    (endDate.getFullYear() - startDate.getFullYear()) * 12 +
    (endDate.getMonth() - startDate.getMonth()) +
    1

  const years = Math.floor(months / 12)
  const remMonths = months % 12

  if (years === 0) return `${remMonths} mos`
  if (remMonths === 0) return `${years} yr`

  return `${years} yr ${remMonths} mos`
}

</script>

<template>
  <section class="career-section">
    <span class="bg-grid"></span>
    <span class="bg-glow"></span>

    <header class="section-header">
      <div class="head-l">
        <h2 class="section-title">
          <span>Studies and</span>
          <em class="t-it">Work experience</em>
        </h2>

        <p class="section-sub">
        Timeline bringing together my jobs, internships, apprenticeships, and diplomas in chronological order.
        </p>
      </div>
    </header>

    <nav class="filters">
      <button
        class="filter-chip"
        :class="{ active: activeFilter === 'All' }"
        @click="activeFilter = 'All'"
      >
        <span>All</span>
        <span class="ch-count">{{ experiences.length }}</span>
      </button>

      <button
        v-for="k in kinds"
        :key="k"
        class="filter-chip"
        :class="{ active: activeFilter === k }"
        @click="activeFilter = k"
      >
        <span>{{ k }}</span>
        <span class="ch-count">{{ countOf(k) }}</span>
      </button>

      <span class="filter-sep"></span>
    </nav>

    <ol class="ledger">
      <li
        v-for="(exp, i) in filtered"
        :key="i"
        class="row"
        :style="{ '--accent': exp.accent }"
      >
        <span class="accent-strip"></span>

        <div class="col-body">
          <header class="row-head">
            <span class="kind-tag">
              <span class="kind-sym">{{ exp.symbol }}</span>
              <span>{{ exp.kind }}</span>
            </span>

            <span class="row-range">
              {{ exp.startDate }} → {{ exp.endDate ?? 'Now' }}
            </span>

            <span class="row-dur">
              {{ duration(exp.startDate, exp.endDate) }}
            </span>
          </header>

          <h3 class="row-role">{{ exp.role }}</h3>

          <p class="row-org">
            <a
              v-if="exp.orgUrl"
              class="org-name"
              :href="exp.orgUrl"
              target="_blank"
              rel="noopener"
            >
              {{ exp.org }}
            </a>

            <span v-else class="org-name">{{ exp.org }}</span>

            <span class="sep">/</span>

            <span class="org-city">{{ exp.city }}</span>

            <template v-if="exp.honors">
              <span class="sep">/</span>
              <span class="org-honors">{{ exp.honors }}</span>
            </template>
          </p>

          <p class="row-desc">{{ exp.desc }}</p>

          <ul v-if="exp.highlights" class="row-highlights">
            <li v-for="h in exp.highlights" :key="h">
              <span class="bullet">›</span>
              <span>{{ h }}</span>
            </li>
          </ul>
        </div>

        <aside class="col-meta">
          <span class="meta-gh">
            {{ exp.stackLabel ?? 'Stack & tools' }}
          </span>

          <div class="stack">
            <span
              v-for="s in exp.stack"
              :key="s"
              class="stchip"
            >
              {{ s }}
            </span>
          </div>
        </aside>
      </li>
    </ol>

    <footer class="section-foot">
      <span class="legend">
        <span
          class="legend-dot"
          style="background:#cbff48;box-shadow:0 0 10px #cbff48"
        ></span>
        Position
      </span>

      <span class="legend">
        <span
          class="legend-dot"
          style="background:#5ee9c8;box-shadow:0 0 10px #5ee9c8"
        ></span>
        Apprenticeship
      </span>

      <span class="legend">
        <span
          class="legend-dot"
          style="background:#00bb81;box-shadow:0 0 10px #00bb81"
        ></span>
        Internship
      </span>

      <span class="legend">
        <span
          class="legend-dot"
          style="background:rgba(255,255,255,.7)"
        ></span>
        Diploma
      </span>
    </footer>
  </section>
</template>

<style scoped>
.career-section {
  --lime: #cbff48;
  --emerald: #00bb81;
  --aqua: #5ee9c8;
  --ink: #fff;
  --ink-2: rgba(255,255,255,.62);
  --ink-3: rgba(255,255,255,.38);
  --line: rgba(255,255,255,.08);
  --line-2: rgba(255,255,255,.14);
  --bg: #151515;
  --bg-row: rgba(255,255,255,.018);

  position: relative;
  isolation: isolate;
  padding: 4.5rem clamp(1.25rem, 5vw, 3rem) 4rem;
  margin: 4rem auto;
  width: 90%;
  max-width: 1200px;
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 24px;
  overflow: hidden;
}

.section-header {
  position: relative;
  width: auto;
  z-index: 1;
  margin: 0 auto 2.25rem;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 2rem;
  padding-bottom: 1.75rem;
  border-bottom: 1px solid var(--line);
}

.head-l {
  display: flex;
  flex-direction: column;
  gap: .65rem;
}

.section-title {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  font-size: clamp(2.2rem, 4.4vw, 3.6rem);
  line-height: 1;
  letter-spacing: -.025em;
  color: var(--lime);
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: .4rem .55rem;
}

.t-it {
  color: var(--ink);
  font-style: italic;
  font-weight: 400;
}

.section-sub {
  font-size: .95rem;
  color: var(--ink-2);
  margin: .25rem 0 0;
}

.filters {
  position: relative;
  z-index: 1;
  margin: 0 auto 1.5rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .5rem;
}

.filter-chip {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  padding: .55rem .95rem;
  background: transparent;
  color: var(--ink-2);
  border: 1px solid var(--line-2);
  border-radius: 999px;
  font-family: 'DM Sans', sans-serif;
  font-size: .82rem;
  font-weight: 500;
  cursor: pointer;
  transition: all .18s;
}

.filter-chip:hover {
  color: var(--ink);
  border-color: rgba(255,255,255,.3);
}

.filter-chip.active {
  background: var(--lime);
  color: #0a0a0a;
  border-color: var(--lime);
  box-shadow: 0 0 20px rgba(212, 252, 112, 0.129);
}

.ch-count {
  font-family: 'JetBrains Mono', monospace;
  font-size: .65rem;
  color: var(--ink-3);
  letter-spacing: .08em;
}

.filter-sep {
  flex: 1;
  height: 1px;
  background: var(--line);
  margin: 0 .5rem;
}

.ledger {
  position: relative;
  z-index: 1;
  margin: 0 auto;
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.row {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 260px;
  gap: 2rem;
  padding: 1.75rem;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: rgba(255,255,255,.02);
  backdrop-filter: blur(10px);
  transition: .25s ease;
  overflow: hidden;
}

.row:hover {
  background:
    linear-gradient(
      90deg,
      color-mix(in srgb, var(--accent) 7%, transparent),
      transparent 55%
    );
}

.accent-strip {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--accent);
}

.col-body {
  display: flex;
  flex-direction: column;
  gap: .65rem;
}

.row-head {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .6rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.kind-tag {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding: .22rem .6rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--accent) 12%, transparent);
  border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent);
  color: var(--accent);
  font-weight: 600;
}

.row-range {
  color: var(--ink-2);
}

.row-dur {
  color: var(--ink-3);
}

.row-role {
  font-family: 'Playfair Display', serif;
  font-size: 1.7rem;
  font-weight: 700;
  line-height: 1.15;
  color: var(--ink);
  margin: 0;
  transition: color .25s;
}

.row:hover .row-role {
  color: var(--accent);
}

.row-org {
  font-family: 'JetBrains Mono', monospace;
  font-size: .78rem;
  color: var(--ink-2);
  margin: 0;
  display: inline-flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.org-name {
  color: var(--ink);
  font-weight: 600;
  text-decoration: none;
}

.org-name:hover {
  color: var(--accent);
}

.org-city {
  color: var(--ink-3);
  text-transform: uppercase;
  letter-spacing: .14em;
  font-size: .7rem;
}

.org-honors {
  color: var(--accent);
  font-style: italic;
}

.row-desc {
  font-family: 'DM Sans', sans-serif;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--ink-2);
  max-width: 68ch;
}

.row-highlights {
  margin: .5rem 0 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: .35rem;
}

.row-highlights li {
  display: grid;
  grid-template-columns: 16px 1fr;
  gap: .5rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: .78rem;
  color: var(--ink-2);
}

.bullet {
  color: var(--accent);
}

.col-meta {
  display: flex;
  flex-direction: column;
  gap: .8rem;
  align-items: flex-end;
  border-left: 1px dashed var(--line);
  padding-left: 1.5rem;
}

.meta-gh {
  font-family: 'JetBrains Mono', monospace;
  font-size: .62rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--ink-3);
}

.stack {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  justify-content: flex-end;
}

.stchip {
  font-family: 'JetBrains Mono', monospace;
  font-size: .68rem;
  letter-spacing: .06em;
  padding: .3rem .55rem;
  border: 1px solid var(--line-2);
  border-radius: 6px;
  background: rgba(255,255,255,.025);
  color: var(--ink-2);
  transition: .18s ease;
}

.stchip:hover {
  border-color: var(--accent);
  color: var(--accent);
  transform: translateY(-1px);
}

.section-foot {
  position: relative;
  z-index: 1;
  margin: 1.5rem auto 0;
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.25rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink-2);
}

.legend {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
}

.legend-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.sep {
  color: var(--ink-3);
}

@media (max-width: 900px) {
  .row {
    grid-template-columns: 1fr;
  }

  .col-meta {
    align-items: flex-start;
    border-left: none;
    border-top: 1px dashed var(--line);
    padding-left: 0;
    padding-top: 1rem;
  }
}

@media (max-width: 768px) {
  .career-section {
    padding: 3rem 1.25rem;
  }

  .section-title {
    font-size: 2.3rem;
  }

  .row {
    padding: 1.25rem;
  }

  .row-role {
    font-size: 1.35rem;
  }
}
</style>
```
