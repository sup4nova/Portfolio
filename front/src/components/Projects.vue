<script setup lang="ts">
const projects = [
  {
    title: 'Synorva',
    file: 'synorva.cart',
    text: 'Multimodal AI tool that analyzes music and visuals and generates coherent audio tracks.',
    tags: [{ label: 'Beta · Demo', live: true }, { label: 'Private' }],
    link: 'https://github.com/sup4nova/Synorva',
    frame: 'frame--flower',
  },
  {
    title: 'Jobscraper',
    file: 'jobscraper.cart',
    text: 'Collects offers from multiple platforms, filters relevant ones and generates a tailored CV for each application.',
    tags: [{ label: 'Demo', live: true }, { label: 'Private' }],
    frame: 'frame--checker',
  },
  {
    title: 'JavaCryptoTool',
    file: 'cryptotool.cart',
    text: 'Java AES encryption and decryption tool with a web interface and servlet backend.',
    tags: [{ label: 'Online', live: true }, { label: 'School project' }],
    frame: 'frame--checker',
  },
]
</script>

<template>
  <section id="projects" class="section t-melon bg-gingham">
    <svg class="deco sticker" style="--s: 48px; right: 5%; top: 4%" aria-hidden="true"><use href="#star" /></svg>

    <div class="section__in">
      <span class="label">World 5 · 遊戯</span>
      <h2 class="h-display glitch section__title">Projects</h2>
      <p class="projects__lead">Side projects, each one a small game I wanted to play.</p>

      <div class="projects__grid grid-3">
        <article v-for="p in projects" :key="p.title" class="win">
          <div class="win__bar">
            <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
            <span class="win__title">{{ p.file }}</span>
          </div>
          <div class="win__body">
            <div class="frame projects__frame" :class="p.frame">
              <div class="ph">{{ p.title }}</div>
            </div>

            <h3 class="projects__title">{{ p.title }}</h3>
            <p class="projects__text">{{ p.text }}</p>
            <div class="row projects__tags">
              <span v-for="t in p.tags" :key="t.label" class="tag" :class="{ 'tag--live': t.live }" :style="t.live ? undefined : '--tag: var(--c-2)'">
                {{ t.label }}
              </span>
            </div>
            <a v-if="p.link" :href="p.link" target="_blank" rel="noreferrer" class="btn btn--accent projects__link">
              Read more →
            </a>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.projects__lead {
  max-width: 50ch;
  margin: 0 0 1.6rem;
}
.projects__grid {
  align-items: stretch;
}
.projects__grid .win {
  display: flex;
  flex-direction: column;
}
.projects__grid .win__body {
  display: flex;
  flex: 1;
  flex-direction: column;
}
.projects__frame {
  width: 62%;
  margin: 0 auto 1.2rem;
}
.projects__title {
  margin: 0 0 0.4rem;
  font: 600 var(--fs-h3) / 1.25 var(--f-body);
}
.projects__text {
  margin: 0 0 1rem;
  font-size: 0.93rem;
}
.projects__tags {
  gap: 0.4rem;
  margin-top: auto;
}
.projects__link {
  align-self: flex-start;
  margin-top: 1rem;
}
@media (max-width: 640px) {
  .projects__frame {
    width: 9rem;
  }
}
</style>
