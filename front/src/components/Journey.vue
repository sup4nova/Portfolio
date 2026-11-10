<script setup lang="ts">
import Certifications from './Certifications.vue'

const hitColors = ['var(--c-3)', 'var(--c-1)', 'var(--c-2)']

// du plus récent au plus ancien
const steps = [
  {
    dates: '12/2025 → now',
    role: 'Customer Care & Technical Support',
    org: 'TEC3H · Rennes · CDI',
    text: 'Multi-channel support with SLA-driven prioritization. Owns the session lifecycle and partner API setup.',
    points: ['~15-20 calls/day, L1/L2 triage', 'Partner API setup via Postman', 'Owns the FAQ & knowledge base'],
    tags: ['SLA', 'Postman', 'KB'],
    current: true,
  },
  {
    dates: '10/2024 → 08/2025',
    role: 'IT Support Engineer',
    org: 'Contentsquare · Paris · Apprenticeship',
    text: 'L1/L2 internal IT via Jira SM. IAM & endpoints across Okta, Jamf and Google Admin.',
    points: [
      'Asset lifecycle in Snipe-IT',
      'Python/PowerShell automations (Slack auto-assign)',
      'London stock audit & office move',
    ],
    tags: ['Jira SM', 'Okta', 'Jamf', 'Python'],
  },
  {
    dates: '05 → 06/2024',
    role: 'Cybersecurity / InfoSec Intern',
    org: 'Eviden (Atos) · Rennes',
    text: 'Built a PowerShell compliance tool verifying flow matrices against firewall rules.',
    points: ['JSON config: zero code edits when the network changes', 'GUI for non-tech teams, FR/EN docs'],
    tags: ['PowerShell', 'GUI', 'JSON'],
  },
  {
    dates: '09/2023 → 07/2025',
    role: 'M.Sc. Information Systems & Cybersecurity',
    org: 'ESNA · Rennes · Mention Bien',
    text: 'Network architecture, infosec, IAM, automation and project management, alternated with the apprenticeship.',
    points: ['Two-year master, work-study'],
    tags: ['Network', 'InfoSec', 'IAM', 'PM'],
  },
  {
    dates: '09/2021 → 07/2023',
    role: 'B.Sc. Computer Science',
    org: 'IUT de Lannion · Université Rennes 1 · Mention Assez Bien',
    text: 'CS fundamentals, programming, databases, networks and human-centered design.',
    points: ['Class projects in Python, Java and Vue'],
    tags: ['Python', 'Java', 'SQL', 'Vue'],
  },
]
</script>

<template>
  <section id="journey" class="section t-melon bg-stripes">
    <svg class="deco sticker" style="--s: 48px; right: 5%; top: 4%" aria-hidden="true"><use href="#star" /></svg>

    <div class="section__in">
      <span class="label">World 3 · 冒険</span>
      <h2 class="h-display glitch section__title">Journey</h2>
      <p class="journey__lead">Work, internships and diplomas, newest first.</p>

      <div class="journey__grid grid-3">
        <article v-for="(s, i) in steps" :key="s.dates + s.role" class="win">
          <div class="win__bar">
            <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
            <span class="win__title">{{ s.dates }}</span>
          </div>
          <div class="win__body">
            <div class="journey__head">
              <span class="hit" :class="{ 'hit--still': !s.current }" :style="{ '--c': hitColors[i % hitColors.length] }" aria-hidden="true">{{ i + 1 }}</span>
              <div>
                <h3 class="journey__role">{{ s.role }}</h3>
                <p class="journey__org">{{ s.org }}</p>
              </div>
            </div>
            <p class="journey__text">{{ s.text }}</p>
            <ul class="journey__points">
              <li v-for="p in s.points" :key="p">{{ p }}</li>
            </ul>
            <div class="row journey__tags">
              <span v-if="s.current" class="tag tag--live glitter">Now</span>
              <span v-if="s.current" class="judge judge--300" aria-hidden="true">300</span>
              <span v-for="t in s.tags" :key="t" class="tag" style="--tag: var(--c-2)">{{ t }}</span>
            </div>
          </div>
        </article>
      </div>

      <Certifications />
    </div>
  </section>
</template>

<style scoped>
.journey__lead {
  max-width: 50ch;
  margin: 0 0 1.6rem;
}
.journey__grid {
  align-items: start;
}
.journey__head {
  display: flex;
  gap: 0.8rem;
  align-items: flex-start;
  margin-bottom: 0.7rem;
}
.journey__head .hit {
  --s: 40px;
}
.journey__role {
  margin: 0 0 0.2rem;
  font: 600 var(--fs-h3) / 1.25 var(--f-body);
}
.journey__org {
  margin: 0;
  font-size: 0.88rem;
  color: var(--ink-2);
}
.journey__text {
  margin: 0 0 0.7rem;
  font-size: 0.93rem;
}
.journey__points {
  margin: 0 0 1rem;
  padding-left: 1.1rem;
  font-size: 0.88rem;
  color: var(--ink-2);
}
.journey__tags {
  gap: 0.4rem;
}
</style>
