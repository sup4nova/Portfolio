<script setup lang="ts">
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Navigation, Pagination } from 'vue3-carousel'

const certifications = [
  { title: 'AWS Certified Cloud Practitioner', issuer: 'Amazon Web Services', year: '2024' },
  { title: 'Google Professional Cloud Architect', issuer: 'Google Cloud', year: '2023' },
  { title: 'Azure Administrator Associate', issuer: 'Microsoft', year: '2022' },
  { title: 'Scrum Master Certified', issuer: 'ScrumStudy', year: '2022' },
  { title: 'Cisco CCNA', issuer: 'Cisco', year: '2021' },
]

// pas d'autoplay si l'utilisateur préfère réduire les animations
const autoplay = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 3000
</script>

<template>
  <div id="certifications" class="certs">
    <span class="label">Achievements</span>
    <h3 class="h-display certs__title">Certifications</h3>

    <Carousel
      :items-to-show="3"
      :wrap-around="true"
      :autoplay="autoplay"
      :transition="500"
      :breakpoints="{
        1280: { itemsToShow: 3, snapAlign: 'center' },
        1024: { itemsToShow: 2.2, snapAlign: 'center' },
        768:  { itemsToShow: 1.5, snapAlign: 'center' },
        480:  { itemsToShow: 1.1, snapAlign: 'center' },
        0:    { itemsToShow: 1, snapAlign: 'center' }
      }"
    >
      <Slide v-for="cert in certifications" :key="cert.title">
        <div class="win cert-card">
          <div class="win__bar">
            <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
            <span class="win__title">{{ cert.issuer }}</span>
          </div>
          <div class="win__body cert-card__body">
            <h4 class="cert-card__title">{{ cert.title }}</h4>
            <span class="tag tag--pixel" style="--tag: var(--c-2)">Obtenue : {{ cert.year }}</span>
          </div>
        </div>
      </Slide>

      <template #addons>
        <Navigation />
        <Pagination />
      </template>
    </Carousel>
  </div>
</template>

<style scoped>
.certs {
  margin-top: clamp(3rem, 7vw, 5rem);
}
.certs__title {
  font-size: clamp(1.6rem, 3vw, 2.2rem);
  margin: 0.8rem 0 1.2rem;
}
.cert-card {
  width: 100%;
  text-align: left;
}
.cert-card__body {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.8rem;
  min-height: 7.5rem;
  padding: 1.1rem 1.2rem;
}
.cert-card__title {
  margin: 0;
  font: 600 1rem / 1.3 var(--f-body);
}

/* l'ombre dure de .win déborde : on garde de la marge dans la fenêtre du carrousel */
:deep(.carousel__slide) {
  padding: 0.4rem 0.9rem 0.9rem;
}

/* carrousel aux couleurs de la section */
.certs :deep(.carousel) {
  --vc-clr-primary: var(--ink);
  --vc-clr-secondary: var(--ink);
  --vc-clr-white: var(--paper);
  --vc-pgn-background-color: color-mix(in srgb, var(--ink) 25%, transparent);
  --vc-pgn-active-color: var(--ink);
}
:deep(.carousel__prev:focus-visible),
:deep(.carousel__next:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}
</style>
