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
</script>

<template>
  <Carousel
    :items-to-show="3"
    :wrap-around="true"
    :autoplay="3000"
    :transition="500"
    :breakpoints="{
      1280: { itemsToShow: 3, snapAlign: 'center' },
      1024: { itemsToShow: 2.2, snapAlign: 'center' },
      768:  { itemsToShow: 1.5, snapAlign: 'center' },
      480:  { itemsToShow: 1.1, snapAlign: 'center' },
      0:    { itemsToShow: 1, snapAlign: 'center' }
    }"
  >
    <Slide v-for="(cert, idx) in certifications" :key="idx">
      <div class="cert-card">
        <h3>{{ cert.title }}</h3>
        <p v-if="cert.issuer">{{ cert.issuer }}</p>
        <p v-if="cert.year" class="year">Obtenue : {{ cert.year }}</p>
      </div>
    </Slide>

    <template #addons>
      <Navigation />
      <Pagination />
    </template>
  </Carousel>
</template>

<style scoped>
/* ta carte */
.cert-card {
  background: #fff;
  color: #0f172a;
  border-radius: 0.75rem;
  padding: 1rem 1.25rem;
  min-height: 110px;
  box-shadow: 0 8px 20px rgba(0,0,0,.08);
  display: flex;
  flex-direction: column;
  gap: .35rem;
}
.cert-card h3 {
  font-weight: 600;
  font-size: 0.9rem;
  line-height: 1.2;
}
.cert-card p {
  font-size: 0.75rem;
}
.cert-card .year {
  font-size: 0.7rem;
  opacity: .7;
}

/* réduire l’écart entre slides */
.carousel__slide {
  padding: 0;
}
/* centrer le carrousel sur fond noir */
.carousel {
  max-width: 1200px;
  margin: 0 auto;
}
</style>
