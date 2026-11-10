<script setup lang="ts">
defineProps<{
  type: 'scallop' | 'torn' | 'checker' | 'arch' | 'slider'
  /** couleur de fond de la section du dessus */
  from: string
  /** couleur de fond de la section du dessous */
  to: string
}>()
</script>

<template>
  <div class="sep" :class="`sep--${type}`" :style="{ '--from': from, '--to': to }" aria-hidden="true">
    <svg v-if="type === 'torn'">
      <use href="#torn" fill="#fffdf6" y="4" />
      <use href="#torn" :fill="from" />
    </svg>
    <svg v-else-if="type === 'arch'" viewBox="0 0 1200 80" preserveAspectRatio="none">
      <path d="M0 80C260 -8 940 -8 1200 80Z" :fill="to" />
    </svg>
    <span v-else-if="type === 'slider'" class="slider t-melon"><span class="slider__ball"></span></span>
  </div>
</template>
