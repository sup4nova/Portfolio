<script setup lang="ts">
const channels = [
  { name: 'CH 1 · owned', ai: 8 },
  { name: 'CH 2 · hands-on', ai: 22 },
  { name: 'CH 3 · assisted', ai: 70 },
]

const lanes = [
  {
    title: 'Architecture & decisions',
    text: "Data modeling, tech choices, system design, technical documentation and patches — I own these. AI isn't reliable enough here and the judgment has to be mine.",
  },
  {
    title: 'Docs & patches',
    text: "Debugging logic, maintaining structure, writing specs — I handle these manually because they require understanding the full context of what's been built.",
  },
  {
    title: 'AI-assisted',
    text: 'Repetitive front-end implementation, code audits, quick second opinions. AI earns its place when the task is well-defined and the output is verifiable.',
  },
]
</script>

<template>
  <section id="ai" class="section t-lemon bg-stripes">
    <svg class="deco sparkle" style="--s: 34px; left: 5%; top: 5%; --c: #fff" aria-hidden="true"><use href="#spark" /></svg>

    <div class="section__in">
      <span class="label">World 6 · 人工知能</span>
      <h2 class="h-display glitch section__title">How I use AI on my projects</h2>
      <p class="ai__lead">
        AI is part of my workflow — not to replace thinking, but to move faster on the parts that don't need it. I stay
        in control of what matters and let AI handle what it's good at.
      </p>

      <div class="split ai__grid">
        <div class="win">
          <div class="win__bar">
            <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
            <span class="win__title">mixing_session.exe</span>
          </div>
          <div class="win__body">
            <ul class="mix">
              <li v-for="c in channels" :key="c.name">
                <div class="mix__head">
                  <span class="label">{{ c.name }}</span>
                  <b class="mix__val">AI {{ c.ai }}%</b>
                </div>
                <div class="mix__track" role="img" :aria-label="`${c.name}: AI ${c.ai}%`">
                  <i :style="{ width: c.ai + '%' }"></i>
                </div>
              </li>
            </ul>

            <div class="row ai__tools">
              <span class="label">Tools</span>
              <span class="tag" style="--tag: var(--c-1)">Claude AI</span>
              <span class="tag" style="--tag: var(--c-2)">ChatGPT</span>
              <span class="tag tag--pixel">Me · master</span>
            </div>
          </div>
        </div>

        <div class="lanes">
          <article v-for="l in lanes" :key="l.title" class="win">
            <div class="win__body">
              <h3 class="lanes__title">{{ l.title }}</h3>
              <p class="lanes__text">{{ l.text }}</p>
            </div>
          </article>
        </div>
      </div>

      <figure class="win ai__quote">
        <div class="win__bar">
          <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="win__title">What I learned · liner notes</span>
        </div>
        <blockquote class="win__body">
          "Both projects started with a question: what can AI actually do? <mark>Synorva</mark> was a learning
          experiment at the intersection of AI and music. The <mark>job scraper</mark> wasn't AI-powered at first — I
          added it when automation became a real need, not an assumption. Working with AI taught me where it genuinely
          helps and where you still have to show up yourself."
        </blockquote>
      </figure>
    </div>
  </section>
</template>

<style scoped>
.ai__lead {
  max-width: 62ch;
  margin: 0 0 1.8rem;
}
.ai__grid {
  align-items: start;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.4rem;
}
@media (max-width: 880px) {
  .ai__grid {
    grid-template-columns: minmax(0, 1fr);
  }
}

.mix {
  display: grid;
  gap: 1.2rem;
  margin: 0 0 1.6rem;
  padding: 0;
  list-style: none;
}
.mix__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 0.4rem;
}
.mix__val {
  font: var(--fs-pixel) var(--f-pixel);
  letter-spacing: 0.08em;
}
.mix__track {
  height: 16px;
  border: var(--line);
  border-radius: var(--r-pill);
  background: var(--surface);
  overflow: hidden;
}
.mix__track i {
  display: block;
  height: 100%;
  background: var(--c-1);
  border-right: var(--line);
}
.ai__tools {
  padding-top: 1rem;
  border-top: var(--line);
}

.lanes {
  display: grid;
  gap: 1.4rem;
}
.lanes__title {
  margin: 0 0 0.4rem;
  font: 600 var(--fs-h3) / 1.25 var(--f-body);
}
.lanes__text {
  margin: 0;
  font-size: 0.93rem;
}

.ai__quote {
  margin: 1.4rem 0 0;
}
.ai__quote blockquote {
  margin: 0;
  font-size: 1.05rem;
}
.ai__quote mark {
  padding: 0 0.25em;
  border-radius: var(--r-sm);
  background: var(--c-2);
  color: var(--ink);
}
</style>
