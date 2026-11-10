<script setup lang="ts">
import { onBeforeUnmount, ref, watch } from 'vue'

const links = [
  { label: 'About', href: '#about' },
  { label: 'Journey', href: '#journey' },
  { label: 'Stack', href: '#stack' },
  { label: 'Projects', href: '#projects' },
  { label: 'AI', href: '#ai' },
  { label: 'Contact', href: '#contact' },
]

// menu déroulant sous 960px (les liens ne tiennent plus dans la pilule)
const open = ref(false)

function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') open.value = false
}
watch(open, (v) => {
  if (v) addEventListener('keydown', onKey)
  else removeEventListener('keydown', onKey)
})
onBeforeUnmount(() => removeEventListener('keydown', onKey))
</script>

<template>
  <header class="nav-wrap">
    <div class="nav">
      <a href="#home" class="nav__logo" @click="open = false">Sup4nova</a>

      <nav id="nav-links" class="nav__links" :class="{ 'is-open': open }" aria-label="Main">
        <a v-for="link in links" :key="link.href" :href="link.href" @click="open = false">{{ link.label }}</a>
        <a href="#contact" class="btn btn--ghost nav__cta nav__cta--menu" @click="open = false">🤝 Are we a match?</a>
      </nav>

      <a href="#contact" class="btn btn--ghost nav__cta nav__cta--bar">🤝 Are we a match?</a>

      <button
        type="button"
        class="nav__burger"
        :aria-expanded="open"
        aria-controls="nav-links"
        :aria-label="open ? 'Close menu' : 'Open menu'"
        @click="open = !open"
      >
        <span aria-hidden="true"></span>
      </button>
    </div>
  </header>
</template>

<style scoped>
/* pilule flottante, sans emprise dans le flux : le Hero compense avec son padding-top */
.nav-wrap {
  position: fixed;
  top: 0.8rem;
  left: 0;
  right: 0;
  z-index: 10;
  padding: 0 clamp(0.8rem, 4vw, 2.5rem);
  pointer-events: none;
}
.nav {
  position: relative;
  display: flex;
  align-items: center;
  gap: 1.4rem;
  max-width: var(--container);
  margin: 0 auto;
  padding: 0.45rem 0.5rem 0.45rem 1.1rem;
  background: var(--paper);
  border: var(--line);
  border-radius: var(--r-pill);
  box-shadow: 3px 3px 0 rgba(60, 198, 184, 0.5);
  pointer-events: auto;
}
.nav__logo {
  font: 400 1.15rem var(--f-display);
  letter-spacing: var(--ls-display);
  text-decoration: none;
  border-radius: var(--r-sm);
}
.nav__links {
  display: flex;
  gap: 1.1rem;
  margin-left: auto;
  white-space: nowrap;
  font-size: 0.9rem;
}
.nav__links > a:not(.btn) {
  text-decoration: none;
}
.nav__links > a:not(.btn):hover {
  text-decoration: underline;
}
.nav__logo:focus-visible,
.nav__links a:focus-visible,
.nav__burger:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}
.nav__cta {
  padding: 0.5em 1.1em;
  font-size: 0.85rem;
}
.nav__cta--menu,
.nav__burger {
  display: none;
}

/* burger : 3 barres dessinées avec un seul span */
.nav__burger {
  position: relative;
  flex: none;
  width: 44px;
  height: 44px;
  padding: 0;
  border: var(--line);
  border-radius: 50%;
  background: var(--c-2, #bdeedc);
  cursor: pointer;
}
.nav__burger span,
.nav__burger span::before,
.nav__burger span::after {
  position: absolute;
  left: 50%;
  width: 18px;
  height: 2px;
  margin-left: -9px;
  border-radius: 2px;
  background: var(--ink);
  transition: transform var(--dur) var(--ease), opacity var(--dur) var(--ease);
}
.nav__burger span {
  top: 50%;
  margin-top: -1px;
}
.nav__burger span::before,
.nav__burger span::after {
  content: '';
  left: 0;
  margin: 0;
}
.nav__burger span::before {
  top: -6px;
}
.nav__burger span::after {
  top: 6px;
}
.nav__burger[aria-expanded='true'] span {
  background: transparent;
}
.nav__burger[aria-expanded='true'] span::before {
  transform: translateY(6px) rotate(45deg);
}
.nav__burger[aria-expanded='true'] span::after {
  transform: translateY(-6px) rotate(-45deg);
}

@media (max-width: 960px) {
  .nav {
    gap: 0.6rem;
  }
  .nav__cta--bar {
    margin-left: auto;
  }
  .nav__burger {
    display: block;
  }
  .nav__links {
    position: absolute;
    top: calc(100% + 0.6rem);
    left: 0;
    right: 0;
    display: none;
    flex-direction: column;
    gap: 0;
    margin: 0;
    padding: 0.5rem;
    background: var(--paper);
    border: var(--line);
    border-radius: var(--r-lg);
    box-shadow: var(--sh-hard, 5px 5px 0 rgba(60, 198, 184, 0.5));
    font-size: 1rem;
  }
  .nav__links.is-open {
    display: flex;
  }
  .nav__links > a:not(.btn) {
    display: flex;
    align-items: center;
    min-height: 48px;
    padding: 0 1rem;
    border-radius: var(--r-md);
  }
  .nav__links > a:not(.btn):hover {
    background: color-mix(in srgb, var(--c-2, #bdeedc) 55%, transparent);
    text-decoration: none;
  }
}
/* petits écrans : le CTA passe dans le menu */
@media (max-width: 560px) {
  .nav__cta--bar {
    display: none;
  }
  .nav__burger {
    margin-left: auto;
  }
  .nav__cta--menu {
    display: inline-flex;
    justify-content: center;
    margin: 0.4rem 0.4rem 0.2rem;
  }
}
</style>
