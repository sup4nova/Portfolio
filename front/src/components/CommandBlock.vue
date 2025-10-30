<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'

/**
 * Props
 * - password (string | null) : mot de passe "fun" côté client (null => pas de verrou)
 * - revealSlotOnUnlock (boolean) : si true, affiche le slot default après unlock
 */
defineProps<{ password?: string | null; revealSlotOnUnlock?: boolean }>()
const props = defineProps<any>()

// état
const lines = reactive<{ type: 'out'|'err'|'in', text: string }[]>([
  { type: 'out', text: 'Welcome to Sup4nova shell — tape `help` pour la liste des commandes.' }
])
const input = ref('')
const history: string[] = []
let historyIndex = -1

const locked = ref(!!props.password)         // si un pw est fourni, on est locked
const unlocked = ref(!props.password)

const prompt = computed(() => (locked.value ? 'password' : 'sup4nova'))

// commandes simples
function runCommand(raw: string) {
  const cmd = raw.trim()
  if (!cmd) return
  lines.push({ type: 'in', text: `$ ${cmd}` })
  history.unshift(cmd); historyIndex = -1

  const [name, ...args] = cmd.split(/\s+/)

  if (locked.value && name !== 'unlock') {
    lines.push({ type: 'err', text: '🔒 Site verrouillé — tapez `unlock <motdepasse>`' })
    return
  }

  switch (name.toLowerCase()) {
    case 'help':
      lines.push({ type: 'out', text: 'Commands: help, echo <text>, date, clear, unlock <pw>, whoami' })
      break
    case 'echo':
      lines.push({ type: 'out', text: args.join(' ') })
      break
    case 'date':
      lines.push({ type: 'out', text: new Date().toString() })
      break
    case 'clear':
      lines.splice(0, lines.length)
      break
    case 'whoami':
      lines.push({ type: 'out', text: 'sup4nova — cyber · audio · AI' })
      break
    case 'unlock': {
      const pw = args.join(' ')
      if (!props.password) {
        lines.push({ type: 'err', text: 'No password set for this terminal.' })
      } else if (pw === props.password) {
        locked.value = false
        unlocked.value = true
        lines.push({ type: 'out', text: '🔓 Unlocked! Bienvenue.' })
      } else {
        lines.push({ type: 'err', text: 'Wrong password.' })
      }
      break
    }
    default:
      lines.push({ type: 'err', text: `Unknown command: ${name}` })
  }
}

function submit() {
  const value = input.value
  input.value = ''
  runCommand(value)
}

// history nav
function onKeyDown(e: KeyboardEvent) {
  if (e.key === 'Enter') {
    e.preventDefault()
    submit()
  } else if (e.key === 'ArrowUp') {
    e.preventDefault()
    if (history.length === 0) return
    historyIndex = Math.min(historyIndex + 1, history.length - 1)
    input.value = history[historyIndex] || ''
  } else if (e.key === 'ArrowDown') {
    e.preventDefault()
    if (history.length === 0) return
    historyIndex = Math.max(historyIndex - 1, -1)
    input.value = historyIndex === -1 ? '' : history[historyIndex]
  }
}

// auto focus
const inputRef = ref<HTMLInputElement | null>(null)
onMounted(() => inputRef.value?.focus())
</script>

<template>
  <div class="w-full max-w-3xl mx-auto rounded-2xl border border-white/10 bg-black/50 p-4 text-[#EDEDED]">
    <!-- output -->
    <div class="h-64 overflow-auto p-2 space-y-2 mb-3" style="font-family: ui-monospace, SFMono-Regular, Menlo, monospace;">
      <div v-for="(l, i) in lines" :key="i" class="whitespace-pre-wrap">
        <template v-if="l.type === 'out'">
          <span class="text-[#EDEDED]">{{ l.text }}</span>
        </template>
        <template v-else-if="l.type === 'err'">
          <span class="text-[#FF6B6B]">ERROR: {{ l.text }}</span>
        </template>
        <template v-else>
          <span class="text-[#9AE6B4]">{{ l.text }}</span>
        </template>
      </div>
    </div>

    <!-- prompt -->
    <div class="flex items-center gap-3" style="font-family: ui-monospace, SFMono-Regular, Menlo, monospace;">
      <div class="px-3 py-1 rounded-md bg-[#111] text-sm text-[#66FF9A]">{{ prompt }}</div>

      <input
        ref="inputRef"
        v-model="input"
        @keydown="onKeyDown"
        :type="locked ? 'password' : 'text'"
        placeholder="Type a command (help)"
        class="flex-1 bg-transparent outline-none border border-white/5 rounded-md px-3 py-2 placeholder:opacity-50"
      />

      <button @click="submit" class="ml-2 px-3 py-2 rounded-md bg-[#D16FFF]/80 hover:bg-[#D16FFF] transition">Run</button>
    </div>

    <!-- reveal slot if unlocked and prop set -->
    <div v-if="unlocked && (props.revealSlotOnUnlock ?? false)" class="mt-4 p-3 rounded-md border border-white/6 bg-black/30">
      <slot>🔐 Slot revealed — put secret content here</slot>
    </div>
  </div>
</template>

<style scoped>
/* small scrollbar */
div.h-64::-webkit-scrollbar { height: 8px; width: 8px; }
div.h-64::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.06); border-radius: 8px; }
</style>
