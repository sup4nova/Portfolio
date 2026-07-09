<script setup lang="ts">
import { ref, onMounted } from 'vue'
import stars from '../assets/stars.jpg'

const visible = ref(false)

onMounted(() => {
  requestAnimationFrame(() => {
    visible.value = true
  })
})

function scrollToAbout() {
  document.getElementById('about')?.scrollIntoView({
    behavior: 'smooth',
    block: 'start'
  })
}
</script>

<template>
  <section class="hero-section" :class="{ 'hero-visible': visible }">

    <div class="hero-orb hero-orb--1"></div>
    <div class="hero-orb hero-orb--2"></div>

    <div class="hero-grid">
      <div class="hero-text">
        <h1 class="hero-title">
          <span class="line-thin anim-item anim-item--1">Discover</span>
          <span class="line-thick anim-item anim-item--2">My</span>
          <span class="line-accent anim-item anim-item--3">Projects</span>
        </h1>

        <p class="hero-sub anim-item anim-item--4">
          Explorations at the edge of
          <em>cyber</em>,
          <em>development</em> &amp;
          <em>ML-driven art</em>.
        </p>

        <div class="hero-actions anim-item anim-item--5">
          <a
            href="https://github.com/sup4nova"
            target="_blank"
            rel="noopener noreferrer"
            class="btn-primary"
          >
            View Projects ↗
          </a>
          <button
            type="button"
            class="btn-ghost"
            @click="scrollToAbout"
          >
            About Me
          </button>
        </div>
      </div>
      <div class="hero-visual anim-item anim-item--6">
        <div class="img-frame">
          <img :src="stars" alt="Sup4nova hero visual" class="hero-img" />
          <div class="img-glow"></div>
        </div>
        <div class="float-pill">✦ ML · Dev · Cyber</div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

@keyframes fadeSlideUp {
  from { opacity: 0; transform: translateY(32px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes badgePulse {
  0%, 100% { box-shadow: 0 0 0 0 #00bb8130; }
  50%       { box-shadow: 0 0 0 10px #00bb8100; }
}

@keyframes pillFloat {
  0%, 100% { transform: translateY(0) rotate(-1deg); }
  50%       { transform: translateY(-8px) rotate(0deg); }
}

@keyframes orbDrift {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33%       { transform: translate(40px, -25px) scale(1.08); }
  66%       { transform: translate(-25px, 18px) scale(0.96); }
}

@keyframes imgGlowPulse {
  0%, 100% { box-shadow: inset 0 0 40px #00bb8118, 0 0 60px #00bb8106; }
  50%       { box-shadow: inset 0 0 70px #00bb8130, 0 0 100px #00bb8114; }
}

.anim-item {
  opacity: 0;
  transform: translateY(32px);
}

.hero-visible .anim-item {
  animation: fadeSlideUp 0.75s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

.hero-visible .anim-item--0 { animation-delay: 0.05s; }
.hero-visible .anim-item--1 { animation-delay: 0.15s; }
.hero-visible .anim-item--2 { animation-delay: 0.27s; }
.hero-visible .anim-item--3 { animation-delay: 0.39s; }
.hero-visible .anim-item--4 { animation-delay: 0.54s; }
.hero-visible .anim-item--5 { animation-delay: 0.68s; }
.hero-visible .anim-item--6 { animation-delay: 0.28s; }

.hero-section {
  min-height: 92vh;
  background-color: #0a0a0a;
  padding: 3rem clamp(1.25rem, 5vw, 2.5rem) 2rem;
  display: flex;
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
  /* clip-path clips filter:blur() effects que overflow:hidden ignore sur Safari */
  clip-path: inset(0);
}

.hero-orb {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  filter: blur(90px);
  animation: orbDrift 14s ease-in-out infinite;
}

.hero-orb--1 {
  width: 420px;
  height: 420px;
  background: radial-gradient(circle, #00bb8120 0%, transparent 70%);
  top: -120px;
  right: -80px;
  animation-delay: 0s;
}

.hero-orb--2 {
  width: 320px;
  height: 320px;
  background: radial-gradient(circle, #CBFF4815 0%, transparent 70%);
  bottom: 40px;
  left: -60px;
  animation-delay: -6s;
}

.badge-wrap { margin-bottom: 2rem; }

.badge {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.72rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #00bb81;
  border: 1px solid #00bb8140;
  padding: 0.35rem 0.9rem;
  border-radius: 999px;
  background: #00bb8110;
  animation: badgePulse 2.8s ease-in-out infinite;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
  flex: 1;
}

@media (max-width: 768px) {
  .hero-grid { grid-template-columns: 1fr; }
}

@media (max-width: 480px) {
  .hero-section { padding: 2rem 1.25rem 1.5rem; }
  .hero-visual { display: none; }
}

.hero-title {
  font-family: 'Playfair Display', serif;
  line-height: 1.0;
  margin: 0 0 1.5rem;
  display: flex;
  flex-direction: column;
}

.line-thin {
  font-size: clamp(3rem, 7vw, 6rem);
  font-weight: 400;
  color: #CBFF48;
  letter-spacing: -0.02em;
}

.line-thick {
  font-size: clamp(3rem, 7vw, 6rem);
  font-weight: 700;
  color: #CBFF48;
  letter-spacing: -0.03em;
}

.line-accent {
  font-size: clamp(3rem, 7vw, 6rem);
  font-weight: 700;
  font-style: italic;
  color: #00bb81;
  letter-spacing: -0.03em;
}

.hero-sub {
  font-family: 'DM Sans', sans-serif;
  font-size: 1.05rem;
  font-weight: 300;
  color: #888;
  line-height: 1.7;
  max-width: 38ch;
  margin-bottom: 2.5rem;
}

.hero-sub em {
  font-style: normal;
  font-weight: 500;
  color: #EDEDED;
  border-bottom: 1.5px solid #CBFF48;
  padding-bottom: 1px;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-primary {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  color: #0a0a0a;
  background: #CBFF48;
  padding: 0.75rem 1.75rem;
  border-radius: 999px;
  text-decoration: none;
  transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 28px #CBFF4860;
}

.btn-ghost {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9rem;
  font-weight: 400;
  color: #aaa;
  background: transparent;
  border: 1px solid #aaaaaa25;
  padding: 0.75rem 1.75rem;
  border-radius: 999px;
  text-decoration: none;
  transition: border-color 0.2s, color 0.2s;
}

.btn-ghost:hover {
  border-color: #00bb81;
  color: #00bb81;
}

.hero-visual {
  position: relative;
  display: flex;
  justify-content: center;
}

.img-frame {
  position: relative;
  border-radius: 2rem;
  overflow: hidden;
  max-width: 480px;
  width: 100%;
}

.hero-img {
  width: 100%;
  display: block;
  border-radius: 2rem;
  transition: transform 0.5s ease;
}

.hero-img:hover {
  transform: scale(1.03);
}

.img-glow {
  position: absolute;
  inset: 0;
  border-radius: 2rem;
  animation: imgGlowPulse 4s ease-in-out infinite;
  pointer-events: none;
}

.float-pill {
  position: absolute;
  bottom: -1rem;
  left: -1.5rem;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.1em;
  color: #0a0a0a;
  background: #CBFF48;
  padding: 0.5rem 1.1rem;
  border-radius: 999px;
  white-space: nowrap;
  box-shadow: 0 4px 20px #CBFF4850;
  animation: pillFloat 3.2s ease-in-out infinite;
}
</style>
