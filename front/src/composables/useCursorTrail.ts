import { onBeforeUnmount, onMounted } from 'vue'

const N = 8
const LERP = 0.45

/** Traînée de curseur osu! : 8 pastilles qui suivent le pointeur. Desktop uniquement, jamais en reduced-motion. */
export function useCursorTrail() {
  let dots: HTMLElement[] = []
  let raf = 0
  let onMove: ((e: PointerEvent) => void) | null = null

  onMounted(() => {
    if (!matchMedia('(pointer:fine)').matches || matchMedia('(prefers-reduced-motion:reduce)').matches) return

    const pts = Array.from({ length: N }, () => ({ x: -99, y: -99 }))
    let mx = -99
    let my = -99

    dots = pts.map(() => {
      const d = document.createElement('i')
      d.className = 'cursor-trail'
      d.setAttribute('aria-hidden', 'true')
      d.style.transform = 'scale(0)'
      document.body.appendChild(d)
      return d
    })

    onMove = (e) => {
      mx = e.clientX
      my = e.clientY
    }
    addEventListener('pointermove', onMove)

    const loop = () => {
      let x = mx
      let y = my
      pts.forEach((p, i) => {
        const dot = dots[i]
        if (!dot) return
        p.x += (x - p.x) * LERP
        p.y += (y - p.y) * LERP
        dot.style.transform = `translate(${p.x}px,${p.y}px) scale(${1 - i / N})`
        dot.style.opacity = (0.75 - (i / N) * 0.7).toFixed(2)
        x = p.x
        y = p.y
      })
      raf = requestAnimationFrame(loop)
    }
    loop()
  })

  onBeforeUnmount(() => {
    cancelAnimationFrame(raf)
    if (onMove) removeEventListener('pointermove', onMove)
    dots.forEach((d) => d.remove())
    dots = []
  })
}
