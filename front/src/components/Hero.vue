<script setup lang="ts">
import stars from '../assets/sup4nova-stars.jpeg'
</script>

<template>
  <section id="home" class="section hero t-melon bg-dots">
    <svg class="deco sparkle" style="--s: 40px; right: 7%; top: 16%" aria-hidden="true"><use href="#spark" /></svg>
    <svg class="deco sticker" style="--s: 56px; left: 4%; bottom: 8%; --c: var(--c-3)" aria-hidden="true"><use href="#star" /></svg>

    <div class="section__in split">
      <div class="win">
        <div class="win__bar">
          <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="win__title">C:\sup4nova.exe</span>
        </div>

        <div class="win__body hero__body">
          <span class="label">World 1 · 起動</span>

          <h1 class="h-display hero__title" aria-label="Sup4nova">Sup<span class="chrome">4</span>nova</h1>

          <p class="hero__text">
            Explorations at the edge of cyber, development &amp; AI-driven art.
          </p>

          <div class="row">
            <a href="#projects" class="btn">See my work ↓</a>
            <a href="mailto:contact@sup4nova.com" class="btn btn--ghost">contact@sup4nova.com</a>
          </div>

          <div class="row hero__status">
            <span class="tag tag--live">Open to work · Q3 2026</span>
            <span class="tag" style="--tag: var(--c-2)">EU + remote</span>
          </div>
        </div>
      </div>

      <!-- .glow en wrapper : le filter de .frame--flower écraserait le halo -->
      <div class="glow hero__frame">
        <div class="frame frame--flower">
          <img :src="stars" alt="Sup4nova hero visual" />
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* la navbar flottante n'a pas d'emprise : on réserve sa hauteur */
.hero {
  padding-top: clamp(6rem, 12vw, 8rem);
}
.hero__body {
  padding: 2rem 2.2rem 2.2rem;
}
.hero__title {
  font-size: var(--fs-hero);
  margin: 1rem 0 0.9rem;
}
.hero__text {
  max-width: 34ch;
  margin: 0 0 1.6rem;
  font-size: 1.15rem;
}
.hero__status {
  margin-top: 1.4rem;
}
@media (max-width: 880px) {
  .hero__body {
    padding: 1.6rem 1.4rem 1.8rem;
  }
  .hero__frame {
    max-width: 320px;
    margin: 0 auto;
  }
}
</style>
