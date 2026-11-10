<script setup lang="ts">
import SectionDivider from '@/components/SectionDivider.vue'
import Hero from '@/components/Hero.vue'
import About from '@/components/About.vue'
import Journey from '@/components/Journey.vue'
import Stack from '@/components/Stack.vue'
import Projects from '@/components/Projects.vue'
import WorkingWithAI from '@/components/WorkingWithAI.vue'
import Contact from '@/components/Contact.vue'

// fonds des deux thèmes (--bg de .t-melon / .t-lemon)
const MELON = '#f3fbf5'
const LEMON = '#dff0ff'
</script>

<template>
  <Hero />
  <SectionDivider type="scallop" :from="MELON" :to="LEMON" />
  <About />
  <SectionDivider type="torn" :from="LEMON" :to="MELON" />
  <Journey />
  <SectionDivider type="checker" :from="MELON" :to="LEMON" />
  <Stack />
  <SectionDivider type="arch" :from="LEMON" :to="MELON" />
  <Projects />
  <SectionDivider type="slider" :from="MELON" :to="LEMON" />
  <WorkingWithAI />
  <SectionDivider type="torn" :from="LEMON" :to="MELON" />
  <Contact />
</template>
