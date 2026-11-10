<script setup lang="ts">
import SvgDefs from '@/components/SvgDefs.vue'
import Navbar from '@/components/Navbar.vue'
import SiteFooter from '@/components/SiteFooter.vue'
import { useCursorTrail } from '@/composables/useCursorTrail'

useCursorTrail()
</script>

<template>
  <SvgDefs />
  <Navbar />
  <main>
    <RouterView />
  </main>
  <SiteFooter />
</template>
