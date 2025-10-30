<script setup lang="ts">
import jellyfish from '@/assets/jellyfish.jpg'
</script>

<template>
  <section
    class="max-w-3xl mx-auto my-10 p-6 rounded-2xl border border-white/10 
           bg-[#0A0A0A]/80 backdrop-blur-md shadow-[0_0_20px_rgba(209,111,255,.2)]
           flex items-center gap-6 hover:shadow-[0_0_25px_rgba(209,111,255,.4)]
           transition"
  >
    <img :src="jellyfish" alt="Tailwind CSS" class="w-48 h-auto rounded-xl border border-white/10" />

    <div class="space-y-2">
      <h3 class="text-2xl font-bold text-[#D16FFF]">Tailwind CSS</h3>
      <p class="text-[#EDEDED]/80 text-sm leading-relaxed">
        Nuxt UI integrates with the latest Tailwind CSS v4, bringing significant improvements.
      </p>
    </div>
  </section>
</template>
