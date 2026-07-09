import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { mount } from '@vue/test-utils'
import MatchQuiz from '../MatchQuiz.vue'

// MatchQuiz's template is a single <Teleport to="body">, so its content is
// rendered outside the component's own root node — query the document instead
// of the test-utils wrapper for anything past the trigger button.

function mountQuiz() {
  return mount(MatchQuiz, { attachTo: document.body })
}

function q<T extends Element = HTMLElement>(selector: string): T {
  const el = document.querySelector(selector)
  if (!el) throw new Error(`not found: ${selector}`)
  return el as T
}

function qAll<T extends Element = HTMLButtonElement>(selector: string): T[] {
  return Array.from(document.querySelectorAll(selector)) as T[]
}

async function openQuiz(wrapper: ReturnType<typeof mountQuiz>) {
  q<HTMLButtonElement>('.mq-trigger.floating').click()
  await wrapper.vm.$nextTick()
}

async function clickNext(wrapper: ReturnType<typeof mountQuiz>) {
  q<HTMLButtonElement>('.mq-btn.primary').click()
  await wrapper.vm.$nextTick()
}

beforeEach(() => {
  vi.stubGlobal('fetch', vi.fn())
})

afterEach(() => {
  vi.unstubAllGlobals()
  document.body.innerHTML = ''
})

describe('MatchQuiz', () => {
  it('is closed by default and opens on trigger click', async () => {
    const wrapper = mountQuiz()
    expect(document.querySelector('.mq-overlay')).toBeNull()

    await openQuiz(wrapper)
    expect(document.querySelector('.mq-overlay')).not.toBeNull()
    expect(document.body.textContent).toContain('What are you trying to build or solve?')
  })

  it('blocks advancing on the focus step until an option is picked', async () => {
    const wrapper = mountQuiz()
    await openQuiz(wrapper)

    await clickNext(wrapper) // goal -> focus
    expect(q<HTMLButtonElement>('.mq-btn.primary').disabled).toBe(true)

    qAll('.mq-chip')[0]!.click()
    await wrapper.vm.$nextTick()

    expect(q<HTMLButtonElement>('.mq-btn.primary').disabled).toBe(false)
  })

  it('caps multi-select chips at their max and drops the oldest pick', async () => {
    const wrapper = mountQuiz()
    await openQuiz(wrapper)
    await clickNext(wrapper) // goal -> focus (max 3)

    for (const i of [0, 1, 2]) {
      qAll('.mq-chip')[i]!.click()
      await wrapper.vm.$nextTick()
    }
    expect(qAll('.mq-chip').filter((c) => c.classList.contains('on')).length).toBe(3)

    qAll('.mq-chip')[3]!.click()
    await wrapper.vm.$nextTick()

    const chips = qAll('.mq-chip')
    expect(chips.filter((c) => c.classList.contains('on')).length).toBe(3)
    expect(chips[0]!.classList.contains('on')).toBe(false) // oldest pick dropped
    expect(chips[3]!.classList.contains('on')).toBe(true)
  })

  it('submits answers to /api/match and renders the returned score', async () => {
    const mockResult = {
      techScore: 82,
      cultureScore: 74,
      overall: 78,
      tag: 'Good overlap',
      message: 'Worth a conversation, most of it lines up.',
    }
    ;(fetch as unknown as ReturnType<typeof vi.fn>).mockResolvedValue({
      ok: true,
      json: async () => mockResult,
    })

    const wrapper = mountQuiz()
    await openQuiz(wrapper)

    await clickNext(wrapper) // goal -> focus
    qAll('.mq-chip')[0]!.click()
    await wrapper.vm.$nextTick()

    await clickNext(wrapper) // focus -> aiNative
    await clickNext(wrapper) // aiNative -> workStyle
    qAll('.mq-chip')[0]!.click()
    await wrapper.vm.$nextTick()

    await clickNext(wrapper) // workStyle -> teamValues
    qAll('.mq-chip')[0]!.click()
    await wrapper.vm.$nextTick()

    await clickNext(wrapper) // teamValues -> teamSize
    qAll('.mq-chip')[0]!.click()
    await wrapper.vm.$nextTick()

    await clickNext(wrapper) // teamSize -> submit

    await vi.waitFor(() => {
      expect(document.body.textContent).toContain('78')
    })

    expect(fetch).toHaveBeenCalledWith('/api/match', expect.objectContaining({ method: 'POST' }))
    expect(document.body.textContent).toContain('Good overlap')
  })
})
