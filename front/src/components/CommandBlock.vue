<script setup lang="ts">
import { ref } from 'vue'

const output = ref<string[]>([
  'Welcome to Sup4nova shell',
  'Type "help" to see commands'
])
const cmd = ref('')

const commands: Record<string, string> = {
  help: 'Commands: help, info, clear',
  info: 'With 💜 by Sup4nova',
}

function run() {
  const value = cmd.value.trim()
  if (!value) return
  output.value.push(`$ ${value}`)

  if (value === 'clear') {
    output.value = []
  } else if (commands[value]) {
    output.value.push(commands[value])
  } else {
    output.value.push(`'${value}' is not recognized.`)
  }

  cmd.value = ''
}
</script>

<template>
  <div class="win max-w-xl">
    <div class="win__bar">
      <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
      <span class="win__title">sup4nova shell</span>
    </div>
    <div class="win__body">
      <div class="h-52 overflow-auto text-sm font-mono space-y-1 mb-3">
        <div v-for="(line, i) in output" :key="i">{{ line }}</div>
      </div>
      <div class="flex gap-2 items-center font-mono">
        <span class="font-bold">sup4nova $</span>
        <input
          v-model="cmd"
          @keyup.enter="run"
          class="flex-1 bg-transparent outline-none border-b-2 border-[var(--ink)] pb-1"
          placeholder="help"
        />
      </div>
    </div>
  </div>
</template>
