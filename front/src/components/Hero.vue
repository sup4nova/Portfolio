<script setup lang="ts">
import stars from '../assets/sup4nova-stars.jpeg'
</script>

<template>
  <section
    class="grid md:grid-cols-2 gap-10 items-center max-w-6xl mx-auto px-6 py-20
           text-[#EDEDED] bg-[#050505]"
  >
    <!-- Bloc texte -->
    <div class="space-y-5">
      <p class="uppercase text-sm tracking-wide text-[#66FF9A]">New release</p>

      <h1 class="text-5xl md:text-6xl font-800 leading-tight">
        Cyber. Sound. AI.
      </h1>

      <p class="opacity-80 max-w-prose text-lg">
        MIAOU MIAOU MIAOU
        <span class="text-[#D16FFF]">cyber aesthetics</span>,
        <span class="text-[#FF9D40]">sound design</span> and
        <span class="text-[#66FF9A]">AI-driven art</span>.
      </p>

      <div class="flex flex-wrap gap-4 pt-4">
        <RouterLink
          to="/projects"
          class="inline-flex items-center gap-2 px-6 py-3 rounded-xl
                 bg-[#D16FFF]/90 hover:bg-[#D16FFF]
                 transition shadow-[0_0_16px_rgba(209,111,255,.35)]
                 font-semibold tracking-wide"
        >
          View Projects
        </RouterLink>

        <RouterLink
          to="/about"
          class="inline-flex items-center gap-2 px-6 py-3 rounded-xl
                 border border-white/15 hover:border-[#FF9D40]/60 transition
                 font-semibold tracking-wide"
        >
          About Me
        </RouterLink>
      </div>
    </div>

    <div class="flex justify-center md:justify-end">
      <img
        :src="stars"
        alt="Sup4nova hero visual"
        class="rounded-xl shadow-2xl ring-2 ring-white/10
               border border-white/10 max-w-[480px] w-full
               hover:drop-shadow-[0_0_15px_#D16FFF80] transition"
      />
    </div>
  </section>
</template>
