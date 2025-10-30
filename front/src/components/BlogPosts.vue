<script setup lang="ts">
import { ref } from 'vue'

import plant1 from '../assets/plant1.jpg'
import plant2 from '../assets/plant2.jpg'
import plant3 from '../assets/plant3.jpg'

const posts = ref([
  {
    title: 'Nuxt Icon v1',
    description: 'Discover Nuxt Icon v1!',
    image: plant1,
    date: '2024-11-25'
  },
  {
    title: 'Nuxt 3.14',
    description: 'Nuxt 3.14 is out!',
    image: plant2,
    date: '2024-11-04'
  },
  {
    title: 'Nuxt 3.13',
    description: 'Nuxt 3.13 is out!',
    image: plant3,
    date: '2024-08-22'
  }
])
</script>

<template>
  <section class="max-w-5xl mx-auto px-6 py-20 space-y-8 text-[#EDEDED] bg-[#050505]">
    <h2 class="text-4xl font-800 tracking-tight text-[#D16FFF] mb-8">Latest Posts</h2>

    <div class="grid gap-8">
      <article
        v-for="(post, index) in posts"
        :key="index"
        class="flex flex-col md:flex-row items-center gap-6 p-6 rounded-2xl
               border border-white/10 bg-[#0B0B0B]/80 backdrop-blur-md
               hover:border-[#D16FFF]/40 hover:shadow-[0_0_20px_rgba(209,111,255,0.3)]
               transition duration-300"
      >
        <img
          :src="post.image"
          :alt="post.title"
          class="w-full md:w-60 h-40 object-cover rounded-xl border border-white/10"
        />

        <div class="flex-1 space-y-3">
          <p class="text-xs text-[#66FF9A]/70">{{ new Date(post.date).toDateString() }}</p>
          <h3 class="text-2xl font-bold text-[#FF9D40]">{{ post.title }}</h3>
          <p class="opacity-80">{{ post.description }}</p>
          <button
            class="mt-2 px-4 py-2 rounded-lg bg-[#D16FFF]/80 hover:bg-[#D16FFF]
                   text-white font-semibold tracking-wide transition"
          >
            Read more →
          </button>
        </div>
      </article>
    </div>
  </section>
</template>
