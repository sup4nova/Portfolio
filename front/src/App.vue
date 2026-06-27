<template>
  <div class="min-h-100vh bg-[#0a0a0a] text-[#EDEDED]">
    <Navbar />
    <div id="home"><Hero /></div>
    <div id="about"><LongCard /></div>
    <div id="working-with-ai"><WorkingWithAI /></div>
    <div id="projects"><BlogPosts /></div>
    <CareerLedger />
    <Certifications />
    <div id="contact"><ContactCard /></div>
    <AppFooter />
  </div>
</template>

<style>
#about {
  margin-top: 5rem;
}
</style>

<script setup lang="ts">
import Navbar from '@/components/Navbar.vue'
import Hero from '@/components/Hero.vue'
import LongCard from '@/components/LongCard.vue'
import WorkingWithAI from '@/components/WorkingWithAI.vue'
import BlogPosts from '@/components/BlogPosts.vue'
import CareerLedger from '@/components/CareerLedger.vue'
import Certifications from '@/components/Certifications.vue'
import ContactCard from './components/ContactCard.vue'
import AppFooter from './components/AppFooter.vue'
</script>
