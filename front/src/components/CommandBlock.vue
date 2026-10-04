<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue'

const visible = ref(false)
const minimized = ref(false)
const output = ref<{ text: string; type: 'system' | 'cmd' | 'response' | 'error' }[]>([
  { text: '✦ Sup4nova shell v2.0', type: 'system' },
  { text: 'Type "help" to see available commands.', type: 'system' },
])
const cmd = ref('')
const terminalBody = ref<HTMLElement | null>(null)

const commands: Record<string, string | string[]> = {
  help: 'Commands: help · info · stack · contact · projects · clear',
  info: 'Sup4nova — Designer & dev. Cyber aesthetics, sound design, AI art.',
  stack: 'Vue 3 · TypeScript · Vite · Node.js · Python · Figma · Sound design',
  contact: 'Email: contact@sup4nova.studio — GitHub: github.com/sup4nova',
  projects: 'Synorva (multimodal AI) · Portfolio v2 · ??? WIP',
}

function run() {
  const value = cmd.value.trim().toLowerCase()
  if (!value) return

  output.value.push({ text: `$ ${value}`, type: 'cmd' })

  if (value === 'clear') {
    output.value = []
  } else if (commands[value]) {
    const res = commands[value]
    const lines = Array.isArray(res) ? res : [res as string]
    lines.forEach(l => output.value.push({ text: l, type: 'response' }))
  } else {
    output.value.push({ text: `'${value}': command not found. Try "help".`, type: 'error' })
  }

  cmd.value = ''
  nextTick(() => {
    if (terminalBody.value) {
      terminalBody.value.scrollTop = terminalBody.value.scrollHeight
    }
  })
}

onMounted(() => {
  setTimeout(() => { visible.value = true }, 800)
})
</script>

<template>
  <Transition name="terminal-pop">
    <div v-if="visible" class="terminal-wrap" :class="{ minimized }">

      <!-- title bar -->
      <div class="terminal-bar" @click="minimized = !minimized">
        <div class="bar-dots">
          <span class="dot dot-red" @click.stop="visible = false"></span>
          <span class="dot dot-yellow" @click.stop="minimized = !minimized"></span>
          <span class="dot dot-green"></span>
        </div>
        <span class="bar-title">sup4nova — shell</span>
        <span class="bar-hint">{{ minimized ? '▲ expand' : '▼ minimize' }}</span>
      </div>

      <!-- body -->
      <Transition name="terminal-slide">
        <div v-if="!minimized" class="terminal-body" ref="terminalBody">
          <div
            v-for="(line, i) in output"
            :key="i"
            class="terminal-line"
            :class="`line-${line.type}`"
          >
            {{ line.text }}
          </div>

          <div class="terminal-input-row">
            <span class="prompt">sup4nova $</span>
            <input
              v-model="cmd"
              @keyup.enter="run"
              class="terminal-input"
              placeholder="help"
              autofocus
              spellcheck="false"
            />
          </div>
        </div>
      </Transition>

    </div>
  </Transition>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

.terminal-wrap {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 420px;
  background: #0d0d0d;
  border: 1px solid #CBFF4830;
  border-radius: 12px;
  overflow: hidden;
  z-index: 1000;
  box-shadow: 0 24px 60px #00000060;
  font-family: 'JetBrains Mono', monospace;
}

.terminal-wrap.minimized {
  width: 240px;
}

/* title bar */
.terminal-bar {
  background: #161616;
  padding: 0.6rem 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  border-bottom: 1px solid #1e1e1e;
  user-select: none;
}

.bar-dots {
  display: flex;
  gap: 5px;
  flex-shrink: 0;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  cursor: pointer;
  transition: opacity 0.2s;
}

.dot:hover { opacity: 0.7; }
.dot-red    { background: #ff5f57; }
.dot-yellow { background: #CBFF48; }
.dot-green  { background: #00bb81; }

.bar-title {
  font-size: 0.7rem;
  color: #555;
  flex: 1;
  letter-spacing: 0.06em;
}

.bar-hint {
  font-size: 0.6rem;
  color: #333;
  letter-spacing: 0.06em;
}

/* body */
.terminal-body {
  padding: 0.9rem 1rem;
  height: 200px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 3px;
  scrollbar-width: thin;
  scrollbar-color: #2a2a2a transparent;
}

.terminal-line {
  font-size: 0.75rem;
  line-height: 1.6;
}

.line-system   { color: #444; }
.line-cmd      { color: #CBFF48; }
.line-response { color: #ccc; }
.line-error    { color: #ff5f57; }

.terminal-input-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.4rem;
  padding-top: 0.4rem;
  border-top: 1px solid #1e1e1e;
}

.prompt {
  font-size: 0.75rem;
  color: #00bb81;
  white-space: nowrap;
  flex-shrink: 0;
}

.terminal-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: #f0f0f0;
  caret-color: #CBFF48;
}

.terminal-input::placeholder {
  color: #333;
}

/* animations */
.terminal-pop-enter-active {
  transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.terminal-pop-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.96);
}

.terminal-slide-enter-active,
.terminal-slide-leave-active {
  transition: max-height 0.3s ease, opacity 0.2s ease;
  max-height: 300px;
  overflow: hidden;
}
.terminal-slide-enter-from,
.terminal-slide-leave-to {
  max-height: 0;
  opacity: 0;
}
</style>
