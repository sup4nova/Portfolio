<!-- MatchQuiz.vue -->

<script setup lang="ts">
import { computed, reactive, ref } from 'vue'

type Option = { id: string; label: string }

const FOCUS: Option[] = [
  { id: 'ai', label: 'AI / LLM integration' },
  { id: 'automation', label: 'Automation & workflows' },
  { id: 'cyber', label: 'Cybersecurity' },
  { id: 'creative', label: 'Audio / creative tech' },
  { id: 'dev', label: 'Frontend / backend dev' },
  { id: 'support', label: 'Support' },
  { id: 'other', label: 'Other' }
]
const WORKSTYLE: Option[] = [
  { id: 'startup', label: 'Fast-moving startup' },
  { id: 'structured', label: 'Structured process' },
  { id: 'remote', label: 'Remote-first' },
  { id: 'inperson', label: 'In-person collaboration' },
]
const TEAMVALUES: Option[] = [
  { id: 'autonomy', label: 'Autonomy' },
  { id: 'ownership', label: 'Deep technical ownership' },
  { id: 'crossteam', label: 'Cross-team collaboration' },
  { id: 'speed', label: 'Shipping speed' },
  { id: 'internationals', label: 'International team' },
]
const TEAMSIZE: Option[] = [
  { id: 'solo', label: 'Solo / freelance' },
  { id: 'small', label: 'Small team (<10)' },
  { id: 'scaleup', label: 'Scale-up' },
  { id: 'enterprise', label: 'Enterprise' },
]

type StepId = 'goal' | 'focus' | 'aiNative' | 'workStyle' | 'teamValues' | 'teamSize'
type Step = { id: StepId; section: 'Tech' | 'Culture' }

const STEPS: Step[] = [
  { id: 'goal', section: 'Tech' },
  { id: 'focus', section: 'Tech' },
  { id: 'aiNative', section: 'Tech' },
  { id: 'workStyle', section: 'Culture' },
  { id: 'teamValues', section: 'Culture' },
  { id: 'teamSize', section: 'Culture' },
]

type Answers = {
  goal: string
  focus: string[]
  aiNative: number
  workStyle: string[]
  teamValues: string[]
  teamSize: string
}

function emptyAnswers(): Answers {
  return { goal: '', focus: [], aiNative: 3, workStyle: [], teamValues: [], teamSize: '' }
}

type MatchResult = {
  techScore: number
  cultureScore: number
  overall: number
  tag: string
  message: string
}

const isOpen = ref(false)
const step = ref(0)
const answers = reactive<Answers>(emptyAnswers())
const result = ref<MatchResult | null>(null)
const isSubmitting = ref(false)
const errorMsg = ref('')

const currentStep = computed(() => STEPS[step.value])
const isResult = computed(() => step.value >= STEPS.length)

const canAdvance = computed(() => {
  const s = currentStep.value
  if (!s) return true
  if (s.id === 'focus') return answers.focus.length > 0
  if (s.id === 'workStyle') return answers.workStyle.length > 0
  if (s.id === 'teamValues') return answers.teamValues.length > 0
  if (s.id === 'teamSize') return answers.teamSize !== ''
  return true
})

function open() {
  step.value = 0
  Object.assign(answers, emptyAnswers())
  result.value = null
  errorMsg.value = ''
  isOpen.value = true
}
function close() {
  isOpen.value = false
}

function toggleMulti(list: string[], id: string, max?: number) {
  const i = list.indexOf(id)
  if (i >= 0) {
    list.splice(i, 1)
    return
  }
  if (max && list.length >= max) list.shift()
  list.push(id)
}

async function next() {
  if (!canAdvance.value) return
  if (step.value < STEPS.length - 1) {
    step.value++
    return
  }
  step.value++
  await submit()
}
function back() {
  if (step.value > 0) step.value--
}

const API_URL = import.meta.env.VITE_API_URL || '/api'

async function submit() {
  isSubmitting.value = true
  errorMsg.value = ''
  try {
    const res = await fetch(`${API_URL}/match`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(answers),
    })
    if (!res.ok) throw new Error(`Request failed (${res.status})`)
    result.value = await res.json()
  } catch {
    errorMsg.value = "Couldn't reach the matching service"
  } finally {
    isSubmitting.value = false
  }
}

function restart() {
  open()
}
</script>

<template>

  <Teleport to="body">
    <button v-if="!isOpen" class="mq-trigger floating" type="button" @click="open">
      <span aria-hidden="true">🤝</span><span>Are we a match?</span>
    </button>

    <div v-if="isOpen" class="mq-overlay show" @click.self="close">
      <div class="mq-modal">
        <header class="mq-head">
          <div class="mq-head-l">
            <span class="mq-eyebrow">
              <span class="dot"></span>
              <span>{{ isResult ? 'Result' : `Question ${step + 1} / ${STEPS.length}` }}</span>
            </span>
            <span v-if="!isResult" class="mq-section">{{ currentStep!.section }}</span>
          </div>
          <button class="mq-close" type="button" aria-label="Close" @click="close">✕</button>
        </header>

        <div class="mq-progress">
          <span
            v-for="(s, i) in STEPS"
            :key="s.id"
            class="mq-progress-seg"
            :class="{ done: isResult || i < step, active: !isResult && i === step }"
          ></span>
        </div>

        <div v-if="!isResult" class="mq-body">
          <template v-if="currentStep!.id === 'goal'">
            <h3 class="mq-q">What are you trying to build or solve?</h3>
            <p class="mq-hint">Helps me understand the context</p>
            <textarea
              v-model="answers.goal"
              class="mq-textarea"
              rows="4"
              placeholder="e.g. we need someone who can own IT support and grow into security…"
            ></textarea>
          </template>

          <template v-else-if="currentStep!.id === 'focus'">
            <h3 class="mq-q">Which of these matter most for this role?</h3>
            <p class="mq-hint">Pick up to 3 of the options below</p>
            <div class="mq-chips">
              <button
                v-for="o in FOCUS"
                :key="o.id"
                type="button"
                class="mq-chip"
                :class="{ on: answers.focus.includes(o.id) }"
                @click="toggleMulti(answers.focus, o.id, 3)"
              >{{ o.label }}</button>
            </div>
          </template>

          <template v-else-if="currentStep!.id === 'aiNative'">
            <h3 class="mq-q">How AI-native is the role?</h3>
            <p class="mq-hint">From "just a tool we use" to "core to the product".</p>
            <div class="mq-scale">
              <input v-model.number="answers.aiNative" type="range" min="1" max="5" step="1" class="mq-range" />
              <div class="mq-scale-labels">
                <span>Just a tool</span>
                <span class="mq-scale-val">{{ answers.aiNative }}</span>
                <span>Core to product</span>
              </div>
            </div>
          </template>

          <template v-else-if="currentStep!.id === 'workStyle'">
            <h3 class="mq-q">How do you like to work?</h3>
            <p class="mq-hint">Pick as many as apply</p>
            <div class="mq-chips">
              <button
                v-for="o in WORKSTYLE"
                :key="o.id"
                type="button"
                class="mq-chip"
                :class="{ on: answers.workStyle.includes(o.id) }"
                @click="toggleMulti(answers.workStyle, o.id)"
              >{{ o.label }}</button>
            </div>
          </template>

          <template v-else-if="currentStep!.id === 'teamValues'">
            <h3 class="mq-q">What matters most on your team?</h3>
            <p class="mq-hint">Pick up to 2 of the options below</p>
            <div class="mq-chips">
              <button
                v-for="o in TEAMVALUES"
                :key="o.id"
                type="button"
                class="mq-chip"
                :class="{ on: answers.teamValues.includes(o.id) }"
                @click="toggleMulti(answers.teamValues, o.id, 2)"
              >{{ o.label }}</button>
            </div>
          </template>

          <template v-else-if="currentStep!.id === 'teamSize'">
            <h3 class="mq-q">Team size?</h3>
            <p class="mq-hint">Pick one of the options below</p>
            <div class="mq-chips">
              <button
                v-for="o in TEAMSIZE"
                :key="o.id"
                type="button"
                class="mq-chip"
                :class="{ on: answers.teamSize === o.id }"
                @click="answers.teamSize = o.id"
              >{{ o.label }}</button>
            </div>
          </template>

          <footer class="mq-nav">
            <button class="mq-btn ghost" type="button" :disabled="step === 0" @click="back">← Back</button>
            <button class="mq-btn primary" type="button" :disabled="!canAdvance" @click="next">
              {{ step === STEPS.length - 1 ? 'See result' : 'Next' }} →
            </button>
          </footer>
        </div>

        <div v-else class="mq-result">
          <template v-if="isSubmitting">
            <p class="mq-hint">Computing your match…</p>
          </template>
          <template v-else-if="errorMsg">
            <p class="mq-hint">{{ errorMsg }}</p>
            <footer class="mq-nav">
              <button class="mq-btn primary" type="button" @click="submit">Retry →</button>
            </footer>
          </template>
          <template v-else-if="result">
            <div class="mq-result-top">
              <span class="mq-result-big">{{ result.overall }}<span class="pct">%</span></span>
              <span class="mq-result-tag">{{ result.tag }}</span>
            </div>
            <p class="mq-result-msg">{{ result.message }}</p>
            <div class="mq-bars">
              <div class="mq-bar-row">
                <span class="mq-bar-label">Technical fit</span>
                <span class="mq-bar-track"><span class="mq-bar-fill tech" :style="{ width: result.techScore + '%' }"></span></span>
                <span class="mq-bar-val">{{ result.techScore }}%</span>
              </div>
              <div class="mq-bar-row">
                <span class="mq-bar-label">Culture fit</span>
                <span class="mq-bar-track"><span class="mq-bar-fill culture" :style="{ width: result.cultureScore + '%' }"></span></span>
                <span class="mq-bar-val">{{ result.cultureScore }}%</span>
              </div>
            </div>
            <div class="mq-result-ctas">
              <a class="mq-btn primary" href="#contact" @click="close">Get in touch ↗</a>
              <button class="mq-btn text" type="button" @click="restart">Retake quiz</button>
            </div>
          </template>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<style scoped>
.mq-trigger {
  --lime: #cbff48;
  --emerald: #00bb81;
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  font-weight: 400;
  letter-spacing: 0.02em;
  padding: 0.85rem 1.3rem;
  background: var(--lime);
  color: #0a0a0a;
  border: none;
  border-radius: 999px;
  cursor: pointer;
  box-shadow: 0 10px 30px -8px rgba(203, 255, 72, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.4);
  transition: transform 0.2s, box-shadow 0.2s, filter 0.2s;
}
.mq-trigger:hover { transform: translateY(-2px); filter: brightness(1.05); box-shadow: 0 14px 36px -8px rgba(203, 255, 72, 0.6); }
.mq-trigger.floating { position: fixed; right: 1.75rem; bottom: 1.75rem; z-index: 200; }

@media (max-width: 600px) {
  .mq-trigger.inline { display: none; }
}

.mq-overlay {
  position: fixed;
  inset: 0;
  z-index: 500;
  background: rgba(4, 10, 8, 0.72);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}
.mq-modal {
  --lime: #cbff48;
  --emerald: #00bb81;
  --aqua: #5ee9c8;
  --ink: #fff;
  --ink-2: rgba(255, 255, 255, 0.62);
  --ink-3: rgba(255, 255, 255, 0.38);
  --line: rgba(255, 255, 255, 0.1);
  width: 100%;
  max-width: 560px;
  background: #121212;
  border: 1px solid var(--line);
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 40px 100px -24px rgba(0, 0, 0, 0.7);
  animation: mqPop 0.28s cubic-bezier(0.2, 0.8, 0.3, 1);
  font-family: 'DM Sans', sans-serif;
  color: var(--ink);
}
@keyframes mqPop {
  from { opacity: 0; transform: translateY(14px) scale(0.98); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

.mq-head { display: flex; align-items: center; justify-content: space-between; padding: 1.4rem 1.6rem 0.9rem; }
.mq-head-l { display: flex; align-items: center; gap: 0.75rem; }
.mq-eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; letter-spacing: 0.16em; text-transform: uppercase; color: var(--emerald); }
.mq-eyebrow .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--emerald); box-shadow: 0 0 8px var(--emerald); }
.mq-section { font-family: 'JetBrains Mono', monospace; font-size: 0.62rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--ink-3); padding: 0.2rem 0.55rem; border: 1px solid var(--line); border-radius: 999px; }
.mq-close { width: 30px; height: 30px; border-radius: 50%; background: rgba(255, 255, 255, 0.05); border: 1px solid var(--line); color: var(--ink-2); font-size: 0.85rem; cursor: pointer; transition: 0.18s; }
.mq-close:hover { background: rgba(255, 255, 255, 0.1); color: var(--ink); }

.mq-progress { display: flex; gap: 5px; padding: 0 1.6rem 1.3rem; }
.mq-progress-seg { flex: 1; height: 3px; border-radius: 999px; background: rgba(255, 255, 255, 0.08); transition: background 0.3s; }
.mq-progress-seg.done { background: var(--emerald); }
.mq-progress-seg.active { background: var(--lime); }

.mq-body { padding: 0 1.6rem 1.6rem; display: flex; flex-direction: column; gap: 1rem; }
.mq-q { font-family: 'Playfair Display', serif; font-weight: 700; font-style: italic; font-size: 1.55rem; line-height: 1.2; letter-spacing: -0.01em; color: var(--ink); margin: 0; }
.mq-hint { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; letter-spacing: 0.04em; color: var(--ink-3); margin: -0.4rem 0 0; }
.mq-textarea { width: 100%; resize: vertical; min-height: 96px; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--line); border-radius: 12px; padding: 0.85rem 1rem; color: var(--ink); font-family: 'DM Sans', sans-serif; font-size: 0.92rem; line-height: 1.5; }
.mq-textarea::placeholder { color: var(--ink-3); }
.mq-textarea:focus { outline: none; border-color: var(--lime); }

.mq-chips { display: flex; flex-wrap: wrap; gap: 0.55rem; }
.mq-chip { font-family: 'DM Sans', sans-serif; font-size: 0.88rem; font-weight: 500; padding: 0.6rem 1rem; border-radius: 999px; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--line); color: var(--ink-2); cursor: pointer; transition: all 0.18s; }
.mq-chip:hover { border-color: rgba(255, 255, 255, 0.25); color: var(--ink); }
.mq-chip.on { background: var(--lime); color: #0a0a0a; border-color: var(--lime); font-weight: 600; }

.mq-scale { display: flex; flex-direction: column; gap: 0.9rem; padding-top: 0.5rem; }
.mq-range { -webkit-appearance: none; appearance: none; width: 100%; height: 6px; border-radius: 999px; background: linear-gradient(90deg, var(--aqua), var(--lime)); cursor: pointer; }
.mq-range::-webkit-slider-thumb { -webkit-appearance: none; width: 20px; height: 20px; border-radius: 50%; background: #0a0a0a; border: 3px solid var(--lime); cursor: pointer; box-shadow: 0 0 12px rgba(203, 255, 72, 0.5); }
.mq-range::-moz-range-thumb { width: 20px; height: 20px; border-radius: 50%; background: #0a0a0a; border: 3px solid var(--lime); cursor: pointer; }
.mq-scale-labels { display: flex; align-items: center; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-3); }
.mq-scale-val { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.3rem; color: var(--lime); text-transform: none; letter-spacing: 0; }

.mq-nav { display: flex; justify-content: space-between; gap: 0.75rem; padding-top: 0.5rem; }
.mq-btn { display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; font-weight: 600; letter-spacing: 0.04em; padding: 0.75rem 1.2rem; border-radius: 10px; cursor: pointer; border: 1px solid var(--line); background: transparent; color: var(--ink); text-decoration: none; transition: all 0.18s; }
.mq-btn.primary { background: var(--lime); color: #0a0a0a; border-color: var(--lime); }
.mq-btn.primary:hover:not(:disabled) { filter: brightness(1.06); box-shadow: 0 0 20px rgba(203, 255, 72, 0.4); }
.mq-btn.ghost:hover:not(:disabled) { border-color: rgba(255, 255, 255, 0.3); }
.mq-btn.text { border-color: transparent; color: var(--ink-3); }
.mq-btn.text:hover { color: var(--ink); }
.mq-btn:disabled { opacity: 0.35; cursor: not-allowed; }

.mq-result { padding: 0.5rem 1.6rem 1.8rem; display: flex; flex-direction: column; gap: 1.4rem; }
.mq-result-top { display: flex; align-items: baseline; gap: 1rem; }
.mq-result-big { font-family: 'Playfair Display', serif; font-weight: 700; font-style: italic; font-size: 4rem; line-height: 1; letter-spacing: -0.03em; background: linear-gradient(135deg, var(--lime), var(--emerald)); -webkit-background-clip: text; background-clip: text; color: transparent; }
.mq-result-big .pct { font-size: 0.5em; }
.mq-result-tag { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: var(--ink); padding: 0.35rem 0.75rem; border-radius: 999px; background: rgba(203, 255, 72, 0.12); border: 1px solid rgba(203, 255, 72, 0.3); }
.mq-result-msg { font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.15rem; color: var(--ink-2); margin: -0.6rem 0 0; line-height: 1.4; }
.mq-bars { display: flex; flex-direction: column; gap: 0.8rem; }
.mq-bar-row { display: grid; grid-template-columns: 100px 1fr 46px; align-items: center; gap: 0.75rem; }
.mq-bar-label { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; letter-spacing: 0.04em; color: var(--ink-2); }
.mq-bar-track { height: 6px; border-radius: 999px; background: rgba(255, 255, 255, 0.08); overflow: hidden; }
.mq-bar-fill { display: block; height: 100%; border-radius: 999px; transition: width 0.6s cubic-bezier(0.2, 0.8, 0.3, 1); }
.mq-bar-fill.tech { background: linear-gradient(90deg, var(--lime), #a8e635); }
.mq-bar-fill.culture { background: linear-gradient(90deg, var(--aqua), var(--emerald)); }
.mq-bar-val { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 600; color: var(--ink); text-align: right; }
.mq-result-ctas { display: flex; flex-wrap: wrap; gap: 0.6rem; padding-top: 0.4rem; border-top: 1px dashed var(--line); }
</style>
