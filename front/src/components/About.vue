<script setup lang="ts">
import { ref } from 'vue'

const tracks = [
  { title: 'Curious', note: 'Learns by taking things apart', time: '3:12' },
  { title: 'Diligent', note: "Follow-up until it's actually fixed", time: '4:05' },
  { title: 'Skilled', note: 'IT support, IAM, scripting, cyber', time: '3:48' },
  { title: 'Sounds have colors', note: 'Synesthesia mix', time: '2:21' },
  { title: 'Night shift', note: 'Bonus track · lights low, music loud', time: '5:30' },
]

// pas d'audio : simple état visuel (égaliseur animé)
const hitColors = ['var(--c-2)', 'var(--c-1)', 'var(--c-3)']
const current = ref(0)
const playing = ref(false)

function pick(i: number) {
  current.value = i
  playing.value = true
}
</script>

<template>
  <section id="about" class="section t-lemon bg-gingham">
    <svg class="deco sparkle" style="--s: 34px; left: 6%; top: 12%; --c: #fff" aria-hidden="true"><use href="#spark" /></svg>

    <div class="section__in split about">
      <div>
        <span class="label">World 2 · Side A · 音楽</span>
        <h2 class="h-display glitch section__title">About me</h2>
        <p class="about__lead">
          21, between Rennes &amp; Paris. IT support engineer by day, creative dev at night. I run support like
          product: SLAs, calm comms, and docs that keep things from breaking twice. Recorded in two languages,
          because international tickets don't wait.
        </p>
        <div class="row">
          <span class="tag" style="--tag: var(--c-2)">Curious</span>
          <span class="tag" style="--tag: var(--c-1)">Diligent</span>
          <span class="tag">Skilled</span>
        </div>
      </div>

      <div class="win">
        <div class="win__bar">
          <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="win__title">liner_notes.txt</span>
        </div>
        <div class="win__body">
          <ol class="trk">
            <li v-for="(t, i) in tracks" :key="t.title">
              <button type="button" class="trk__btn" :class="{ 'is-on': i === current }" :aria-current="i === current" @click="pick(i)">
                <span class="hit" :class="{ 'hit--still': i !== current }" :style="{ '--c': hitColors[i % hitColors.length] }" aria-hidden="true">{{ i + 1 }}</span>
                <span>{{ t.title }}<small>{{ t.note }}</small></span>
                <span class="trk__d">{{ t.time }}</span>
              </button>
            </li>
          </ol>

          <div class="player">
            <button
              type="button"
              class="player__play"
              :aria-label="playing ? 'Pause' : 'Play'"
              :aria-pressed="playing"
              @click="playing = !playing"
            >
              {{ playing ? '❚❚' : '▶' }}
            </button>
            <span class="slider" :class="{ 'is-paused': !playing }" aria-hidden="true"><span class="slider__ball"></span></span>
            <span class="label">Now playing · {{ tracks[current]?.title }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.about {
  align-items: start;
  grid-template-columns: minmax(0, 1fr) minmax(0, 0.9fr);
}
@media (max-width: 880px) {
  .about {
    grid-template-columns: minmax(0, 1fr);
  }
}
.about__lead {
  max-width: 50ch;
  margin: 0 0 1.6rem;
}

.trk {
  list-style: none;
  margin: 0;
  padding: 0;
}
.trk li {
  border-bottom: 1.5px dashed color-mix(in srgb, var(--ink) 35%, transparent);
}
.trk li:last-child {
  border: 0;
}
.trk__btn {
  display: grid;
  grid-template-columns: 30px 1fr auto;
  gap: 0.8rem;
  align-items: center;
  width: 100%;
  padding: 0.65rem 0.4rem;
  border: 0;
  border-radius: var(--r-sm);
  background: transparent;
  color: inherit;
  font: inherit;
  text-align: left;
  cursor: pointer;
}
.trk__btn:hover,
.trk__btn.is-on {
  background: color-mix(in srgb, var(--c-2) 55%, transparent);
}
.trk__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}
.trk .hit {
  --s: 30px;
}
.trk__d {
  font: var(--fs-pixel) var(--f-pixel);
  letter-spacing: 0.08em;
}
.trk small {
  display: block;
  color: var(--ink-2);
  font-size: 0.85rem;
}

.player {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.8rem;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: var(--line);
}
.player__play {
  display: grid;
  place-items: center;
  flex: none;
  width: 40px;
  height: 40px;
  border: var(--line);
  border-radius: 50%;
  background: var(--accent);
  color: var(--ink);
  font-size: 0.8rem;
  cursor: pointer;
}
.player__play:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

.player .slider {
  flex: 1;
  min-width: 60px;
  --s: 26px;
}
.player .slider.is-paused .slider__ball {
  animation-play-state: paused;
}
</style>
