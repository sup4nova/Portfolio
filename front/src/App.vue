<template>
  <div class="min-h-100vh bg-[#050505] text-[#EDEDED]">
    <Navbar />,
    <Hero />
    <LongCard />
    <BlogPosts />
    <Certifications />
    <main class="max-w-6xl mx-auto px-6 py-10">
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import Navbar from '@/components/Navbar.vue'
import Hero from '@/components/Hero.vue'
import LongCard from '@/components/LongCard.vue'
import BlogPosts from '@/components/BlogPosts.vue'
import Certifications from '@/components/Certifications.vue'

</script>
