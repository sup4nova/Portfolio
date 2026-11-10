<script setup lang="ts">
// `hot` = outils utilisés tous les jours
const groups = [
  { name: 'iam_endpoints/', items: ['okta*', 'jamf*', 'google-admin', 'snipe-it', 'sso-mfa', 'vpn'] },
  { name: 'support_itsm/', items: ['jira-sm*', 'postman', 'slack', 'zoom', 'l1-l2', 'sla', 'kb'] },
  { name: 'scripting/', items: ['python*', 'powershell*', 'bash', 'json'] },
  { name: 'cyber_jr/', items: ['firewall-rules', 'flow-matrices', 'compliance', 'oscp-track'] },
  { name: 'frontend_side/', items: ['vue3*', 'typescript', 'vite', 'node', 'figma'] },
  { name: 'creative/', items: ['sound-design', 'generative-art', 'daw', 'creative-coding'] },
].map((g) => ({
  name: g.name,
  items: g.items.map((i) => ({ label: i.replace('*', ''), hot: i.endsWith('*') })),
}))
</script>

<template>
  <section id="stack" class="section t-lemon bg-dots">
    <svg class="deco sparkle" style="--s: 36px; right: 6%; top: 8%" aria-hidden="true"><use href="#spark" /></svg>

    <div class="section__in">
      <span class="label">World 4 · 電脳</span>
      <h2 class="h-display glitch section__title">~/stack</h2>
      <p class="stack__lead">Fewer, sharper. The kit I reach for daily, listed straight from the terminal.</p>

      <div class="win">
        <div class="win__bar">
          <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="win__title">sup4nova@void: ~</span>
        </div>
        <div class="win__body">
          <p class="stack__cmd"><b>sup4nova@void</b>:~$ ls ./stack --by-category</p>

          <dl class="stack__groups">
            <div v-for="g in groups" :key="g.name" class="stack__group">
              <dt class="label">{{ g.name }}</dt>
              <dd class="row stack__items">
                <span
                  v-for="item in g.items"
                  :key="item.label"
                  class="tag"
                  :style="item.hot ? '--tag: var(--c-1)' : undefined"
                >
                  {{ item.label }}
                </span>
              </dd>
            </div>
          </dl>
          <p class="stack__legend">
            <span class="tag" style="--tag: var(--c-1)">highlighted</span> = daily drivers
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.stack__lead {
  max-width: 50ch;
  margin: 0 0 1.6rem;
}
.stack__cmd {
  margin: 0 0 1.4rem;
  font: var(--fs-pixel) / 1.5 var(--f-pixel);
  letter-spacing: 0.08em;
}
.stack__groups {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.4rem 2rem;
  margin: 0;
}
.stack__group {
  min-width: 0;
}
.stack__groups dd {
  margin: 0.6rem 0 0;
}
.stack__items {
  gap: 0.4rem;
}
.stack__legend {
  margin: 1.4rem 0 0;
  padding-top: 1rem;
  border-top: 1.5px dashed color-mix(in srgb, var(--ink) 35%, transparent);
  font-size: 0.85rem;
  color: var(--ink-2);
}
@media (max-width: 560px) {
  .stack__groups {
    grid-template-columns: minmax(0, 1fr);
  }
}
</style>
