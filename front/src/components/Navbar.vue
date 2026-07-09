<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import logo from '../assets/sup4nova-logo.png'
import MatchQuiz from './MatchQuiz.vue'

const activeSection = ref('home')
const menuOpen = ref(false)

const sections = [
  { id: 'home',     label: 'Home' },
  { id: 'about',    label: 'About' },
  { id: 'projects', label: 'Projects' },
  { id: 'contact',  label: 'Contact' },
]

function toggleMenu() { menuOpen.value = !menuOpen.value }
function closeMenu()  { menuOpen.value = false }

let observer: IntersectionObserver | null = null

function onKey(e: KeyboardEvent) { if (e.key === 'Escape') closeMenu() }
function onResize() { if (window.innerWidth > 600) closeMenu() }

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) activeSection.value = entry.target.id
      })
    },
    { rootMargin: '-10% 0px -80% 0px', threshold: 0 }
  )
  sections.forEach(({ id }) => {
    const el = document.getElementById(id)
    if (el) observer!.observe(el)
  })

  window.addEventListener('keydown', onKey)
  window.addEventListener('resize', onResize)
})

onUnmounted(() => {
  observer?.disconnect()
  starLayer?.remove()
  starLayer = null
  window.removeEventListener('keydown', onKey)
  window.removeEventListener('resize', onResize)
  document.body.style.overflow = ''
})

watch(menuOpen, (open) => {
  document.body.style.overflow = open ? 'hidden' : ''
})

let starLayer: HTMLDivElement | null = null
let starCSSInjected = false

function injectStarCSS() {
  if (starCSSInjected) return
  const style = document.createElement('style')
  style.textContent = `
    @keyframes starFly {
      0%   { opacity: 0; transform: rotate(var(--star-angle)) translateX(0)    scaleX(0.15); }
      18%  { opacity: 1; transform: rotate(var(--star-angle)) translateX(30px)  scaleX(1); }
      100% { opacity: 0; transform: rotate(var(--star-angle)) translateX(500px) scaleX(0.7); }
    }
    .shooting-star-layer {
      position: fixed; inset: 0; overflow: hidden;
      pointer-events: none; z-index: 9999;
    }
    .shooting-star-fx {
      position: absolute; height: 2px; width: 90px; border-radius: 999px;
      transform-origin: left center;
      background: linear-gradient(to right, transparent 0%, #CBFF48 65%, #ffffff 100%);
      box-shadow: 0 0 5px #CBFF48, 0 0 10px #CBFF4860, 0 0 2px #fff;
      animation: starFly 0.65s ease-out forwards;
    }
  `
  document.head.appendChild(style)
  starCSSInjected = true
}

function getStarLayer() {
  if (starLayer && starLayer.isConnected) return starLayer
  starLayer = document.createElement('div')
  starLayer.className = 'shooting-star-layer'
  document.body.appendChild(starLayer)
  return starLayer
}

function spawnStar(x: number, y: number, angle: number) {
  injectStarCSS()
  const star = document.createElement('div')
  star.className = 'shooting-star-fx'
  star.style.left = `${x}px`
  star.style.top  = `${y}px`
  star.style.setProperty('--star-angle', `${angle}deg`)
  getStarLayer().appendChild(star)
  star.addEventListener('animationend', () => star.remove(), { once: true })
}

function navigate(id: string, event: MouseEvent) {
  event.preventDefault()
  const el = event.currentTarget as HTMLElement
  const rect = el.getBoundingClientRect()

  const targetEl = document.getElementById(id)
  const targetTop = targetEl?.getBoundingClientRect().top ?? Infinity
  const goingDown = targetTop > rect.bottom

  if (goingDown) {
    spawnStar(rect.left + rect.width / 2, rect.top + rect.height / 2, 90)
  }

  closeMenu()

  setTimeout(() => {
    targetEl?.scrollIntoView({ behavior: 'smooth' })
  }, goingDown ? 180 : 0)
}
</script>

<template>
  <nav class="navbar">
    <div class="navbar-inner">

      <a href="#home" class="navbar-logo" @click="navigate('home', $event)">
        <img :src="logo" alt="Sup4nova logo" class="logo-img" />
      </a>

      <div class="navbar-links">
        <button
          v-for="s in sections"
          :key="s.id"
          class="nav-link"
          :class="{ active: activeSection === s.id }"
          @click="navigate(s.id, $event)"
        >
          {{ s.label }}
        </button>
      </div>

      <MatchQuiz />

      <button
        class="nav-toggle"
        :class="{ open: menuOpen }"
        :aria-expanded="menuOpen"
        aria-controls="mobile-menu"
        aria-label="Ouvrir le menu"
        @click="toggleMenu"
      >
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </button>

    </div>

    <transition name="menu">
      <div v-if="menuOpen" id="mobile-menu" class="mobile-menu">
        <button
          v-for="s in sections"
          :key="s.id"
          class="mobile-link"
          :class="{ active: activeSection === s.id }"
          @click="navigate(s.id, $event)"
        >
          <span>{{ s.label }}</span>
          <span class="m-arrow">↗</span>
        </button>
      </div>
    </transition>
  </nav>

  <transition name="fade">
    <div v-if="menuOpen" class="nav-backdrop" @click="closeMenu"></div>
  </transition>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=Playfair+Display:ital,wght@1,700&display=swap');

@keyframes navSlideDown {
  from { opacity: 0; transform: translateY(-100%); }
  to   { opacity: 1; transform: translateY(0); }
}

.navbar {
  background: #0a0a0acc;
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid #ffffff08;
  position: sticky;
  top: 0;
  z-index: 100;
  padding: 0 2.5rem;
  animation: navSlideDown 0.5s cubic-bezier(0.22, 1, 0.36, 1) both;
}

.navbar-inner {
  width: auto;
  max-width: 1200px;
  margin: 0 auto;
  height: 3.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-logo {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  text-decoration: none;
}

.logo-img {
  height: 2rem;
  width: auto;
  border-radius: 6px;
}

.navbar-links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.nav-link {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.85rem;
  font-weight: 400;
  color: #888;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.4rem 0.9rem;
  border-radius: 999px;
  transition: color 0.2s, background 0.2s;
}

.nav-link:hover {
  color: #EDEDED;
  background: #ffffff08;
}

.nav-link.active {
  color: #CBFF48;
  background: #CBFF4814;
}

.nav-toggle {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 40px;
  height: 40px;
  padding: 0;
  background: none;
  border: 1px solid #ffffff14;
  border-radius: 10px;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s;
}

.nav-toggle:hover {
  border-color: #CBFF4840;
  background: #ffffff06;
}

.nav-toggle .bar {
  display: block;
  width: 20px;
  height: 2px;
  margin: 0 auto;
  background: #CBFF48;
  border-radius: 2px;
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.2s;
}

.nav-toggle.open .bar:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.nav-toggle.open .bar:nth-child(2) { opacity: 0; }
.nav-toggle.open .bar:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

.mobile-menu {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 0.75rem;
  background: #0d0d0df2;
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-top: 1px solid #ffffff08;
  border-bottom: 1px solid #ffffff10;
  box-shadow: 0 24px 48px #00000060;
}

.mobile-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 0.85rem 1rem;
  font-family: 'DM Sans', sans-serif;
  font-size: 1rem;
  font-weight: 500;
  color: #cfcfcf;
  background: #ffffff05;
  border: 1px solid #ffffff0a;
  border-radius: 12px;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, border-color 0.2s;
}

.mobile-link:hover {
  background: #ffffff0a;
  color: #EDEDED;
}

.mobile-link.active {
  color: #CBFF48;
  background: #CBFF4810;
  border-color: #CBFF4830;
}

.m-arrow { font-size: 0.9rem; opacity: 0.5; }
.mobile-link.active .m-arrow { opacity: 1; }

.nav-backdrop {
  position: fixed;
  inset: 0;
  background: #000000a6;
  z-index: 90;
}

.menu-enter-active,
.menu-leave-active { transition: opacity 0.25s ease, transform 0.25s cubic-bezier(0.22, 1, 0.36, 1); }
.menu-enter-from,
.menu-leave-to { opacity: 0; transform: translateY(-8px); }

.fade-enter-active,
.fade-leave-active { transition: opacity 0.25s ease; }
.fade-enter-from,
.fade-leave-to { opacity: 0; }

@media (max-width: 600px) {
  .navbar { padding: 0 1rem; }
  .navbar-links { display: none; }
  .nav-toggle  { display: inline-flex; }
}
</style>