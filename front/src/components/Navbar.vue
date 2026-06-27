<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import logo from '../assets/sup4nova-logo.png'

const activeSection = ref('home')

const sections = [
  { id: 'home',     label: 'Home' },
  { id: 'about',    label: 'About' },
  { id: 'projects', label: 'Projects' },
  { id: 'contact',  label: 'Contact' },
]

let observer: IntersectionObserver | null = null

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
})

onUnmounted(() => observer?.disconnect())

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
    .shooting-star-fx {
      position: fixed;
      height: 2px;
      width: 90px;
      border-radius: 999px;
      pointer-events: none;
      z-index: 9999;
      transform-origin: left center;
      background: linear-gradient(to right, transparent 0%, #CBFF48 65%, #ffffff 100%);
      box-shadow: 0 0 5px #CBFF48, 0 0 10px #CBFF4860, 0 0 2px #fff;
      animation: starFly 0.65s ease-out forwards;
    }
  `
  document.head.appendChild(style)
  starCSSInjected = true
}

function spawnStar(x: number, y: number, angle: number) {
  injectStarCSS()
  const star = document.createElement('div')
  star.className = 'shooting-star-fx'
  star.style.left = `${x}px`
  star.style.top  = `${y}px`
  star.style.setProperty('--star-angle', `${angle}deg`)
  document.body.appendChild(star)
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

    </div>
  </nav>
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

.logo-text {
  font-family: 'Playfair Display', serif;
  font-size: 1rem;
  font-style: italic;
  font-weight: 700;
  color: #CBFF48;
  letter-spacing: -0.01em;
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

@media (max-width: 600px) {
  .navbar { padding: 0 1rem; }
  .logo-text { display: none; }
  .navbar-links { gap: 0; }
  .nav-link { padding: 0.4rem 0.6rem; font-size: 0.8rem; }
}

@media (max-width: 360px) {
  .nav-link { padding: 0.4rem 0.45rem; font-size: 0.75rem; }
}
</style>
