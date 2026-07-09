<script setup lang="ts">
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Navigation } from 'vue3-carousel'

const certifications = [
  { code: 'ᯓ★', tag: 'AI', title: 'Google AI Essentials', issuer: 'Google (Coursera)', year: '2025', credId: 'Course completed', url: 'https://www.coursera.org/learn/google-introduction-to-ai' },
  { code: 'ᯓ★', tag: 'AI/Creative', title: 'Machine Learning for Musicians and Artists', issuer: 'Goldsmiths, University of London (Kadenze)', year: '2025', credId: 'Course completed', url: 'https://www.kadenze.com/courses/machine-learning-for-musicians-and-artists/info' },
  { code: 'ᯓ★', tag: 'Cybersecurity', title: 'Introduction to Cybersecurity', issuer: 'Cisco Networking Academy', year: '2023', credId: 'Course completed', url: 'https://www.netacad.com/fr/courses/introduction-to-cybersecurity?courseLang=en-US' },
  { code: 'ᯓ★', tag: 'Cybersecurity', title: 'Cybersecurity Essentials', issuer: 'Cisco Networking Academy', year: '2024', credId: 'Course completed', url: 'https://www.netacad.com/courses/cybersecurity-essentials?courseLang=en-US' },
  { code: 'ᯓ★', tag: 'Cybersecurity', title: 'SecNumacadémie', issuer: 'ANSSI', year: '2024', credId: 'In progress', url: 'https://secnumacademie.gouv.fr/' },
  { code: 'ᯓ★', tag: 'Cybersecurity', title: 'GDPR MOOC', issuer: 'CNIL', year: '2023', credId: 'Course completed', url: 'https://www.cnil.fr/fr/comprendre-le-rgpd/le-mooc-de-la-cnil' },
]

const mostRecent = Math.max(...certifications.map(c => parseInt(c.year))).toString()
</script>

<template>
  <section class="certs-section">
    <span class="bg-grid"></span>
    <span class="bg-glow"></span>

    <header class="section-header">
      <div class="head-l">
        <span class="section-eyebrow">
          <span class="dot"></span>
          <span>Courses &amp; Learning</span>
        </span>
        <h2 class="section-title">
          <span>Courses &amp; Learning</span>
        </h2>
        <p class="section-sub">
          Followed <b>{{ certifications.length }} courses</b> · most recent <b>{{ mostRecent }}</b>.
        </p>
      </div>
      <div class="head-r">
      </div>
    </header>

    <div class="certs-carousel">
      <Carousel
        :items-to-show="3"
        :wrap-around="true"
        :autoplay="3000"
        :transition="500"
        :breakpoints="{
          1024: { itemsToShow: 3, snapAlign: 'center' },
          768:  { itemsToShow: 2, snapAlign: 'center' },
          0:    { itemsToShow: 1, snapAlign: 'center' }
        }"
      >
        <Slide v-for="(cert, i) in certifications" :key="i">
          <article class="cert-card">
            <div class="row top">
              <div class="seal">
                <span class="seal-code">{{ cert.code }}</span>
                <span class="seal-ring"></span>
              </div>
              <div class="meta">
                <span class="meta-tag">{{ cert.tag }}</span>
                <span class="meta-year">{{ cert.year }}</span>
              </div>
            </div>
            <div class="block">
              <h3 class="cert-title">{{ cert.title }}</h3>
              <p class="cert-issuer"><span class="bullet"></span><span>{{ cert.issuer }}</span></p>
            </div>
            <footer class="card-foot">
              <span class="cred-id">
                <span class="cred-id-v">{{ cert.credId }}</span>
              </span>
              <a class="verify" :href="cert.url" target="_blank" rel="noopener noreferrer">
              what is it? <span class="arr">↗</span>
              </a>
            </footer>
            <span class="corner-glyph">✦</span>
            <span class="grain"></span>
          </article>
        </Slide>

        <template #addons>
          <Navigation />        
        </template>
      </Carousel>
    </div>
  </section>
</template>

<style scoped>
.certs-section {
  --lime: #cbff48;
  --emerald: #00bb81;
  --ink: #fff;
  --ink-2: rgba(255,255,255,.62);
  --ink-3: rgba(255,255,255,.38);
  --line: rgba(255,255,255,.08);
  --line-2: rgba(255,255,255,.14);
  --bg: #151515;
  --bg-card: #0a0a0a;
  position: relative;
  isolation: isolate;
  padding: 4.5rem clamp(1.25rem, 5vw, 3rem) 4rem;
  margin: 4rem auto;
  width: 90%;
  max-width: 1200px;
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 24px;
  overflow: hidden;
}

.section-header {
  position: relative;
  z-index: 1;
  margin: 0 auto 3rem;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 2rem;
  padding-bottom: 1.75rem;
  border-bottom: 1px solid var(--line);
}

.head-l { display: flex; flex-direction: column; gap: .65rem; }

.section-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: .65rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: .7rem;
  font-weight: 500;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--emerald);
}

.dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--emerald);
  box-shadow: 0 0 10px var(--emerald);
  animation: pulse 1.8s infinite;
}

@keyframes pulse { 0%,100% { opacity: 1 } 50% { opacity: .35 } }

.section-title {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  font-size: clamp(2.2rem, 4.4vw, 3.6rem);
  line-height: 1;
  letter-spacing: -.025em;
  color: var(--lime);
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: .4rem .55rem;
}

.t-amp { color: var(--emerald); font-style: italic; font-weight: 400; }
.t-it  { color: var(--ink);    font-style: italic; font-weight: 400; }

.section-sub { font-size: .95rem; color: var(--ink-2); margin: .25rem 0 0; }
.section-sub b { color: var(--ink); font-weight: 500; }

.head-r {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  font-family: 'Playfair Display', serif;
  line-height: 1;
  color: var(--ink);
}

.count {
  font-size: 4rem;
  font-weight: 700;
  font-style: italic;
  background: linear-gradient(180deg, var(--lime), var(--emerald));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  letter-spacing: -.04em;
}

.count-lbl {
  font-family: 'JetBrains Mono', monospace;
  font-size: .65rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--ink-3);
  margin-top: .4rem;
}

.certs-carousel {
  position: relative;
  z-index: 1;
  margin: 0 auto;
  padding: .5rem 0 3.5rem;
}

.cert-card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  background: linear-gradient(180deg, rgba(255,255,255,.022), transparent 60%), var(--bg-card);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 1.75rem 1.75rem 1.5rem;
  margin: 0 .6rem;
  min-height: 280px;
  width: 100%;
  text-align: left;
  cursor: default;
  overflow: hidden;
  transition: transform .35s cubic-bezier(.2,.7,.3,1), border-color .25s, box-shadow .35s;
}

.cert-card::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  border-radius: inherit;
  background: radial-gradient(420px 220px at 100% 0%, rgba(203,255,72,.08), transparent 60%);
  opacity: 0;
  transition: opacity .35s;
}

.cert-card:hover {
  transform: translateY(-6px);
  border-color: var(--line-2);
  box-shadow: 0 18px 48px -16px rgba(0,0,0,.6), 0 0 0 1px rgba(203,255,72,.18);
}

.cert-card:hover::before { opacity: 1; }

.grain {
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: .35;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .25 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='.20'/></svg>");
}

.row.top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  position: relative;
  z-index: 1;
}

.seal {
  position: relative;
  width: 54px;
  height: 54px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 35% 30%, rgba(255,255,255,.10), transparent 60%), #0e0e0e;
  border: 1px solid var(--line-2);
  border-radius: 50%;
  font-family: 'JetBrains Mono', monospace;
  font-size: .78rem;
  font-weight: 600;
  letter-spacing: .04em;
  color: var(--lime);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.06);
}

.seal-code { position: relative; z-index: 1; }

.seal-ring {
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 1px dashed rgba(203,255,72,.18);
  animation: spin 28s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

.meta { display: flex; flex-direction: column; align-items: flex-end; gap: .4rem; }

.meta-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: .62rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--emerald);
  padding: .25rem .6rem;
  border: 1px solid rgba(0,187,129,.30);
  border-radius: 999px;
  background: rgba(0,187,129,.06);
}

.meta-year {
  font-size: .7rem;
  font-weight: 500;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #0a0a0a;
  background: var(--lime);
  padding: .22rem .7rem;
  border-radius: 999px;
}

.block {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: .45rem;
  flex: 1;
}

.block-idx {
  font-family: 'JetBrains Mono', monospace;
  font-size: .68rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ink-3);
}

.cert-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.35rem;
  font-weight: 700;
  line-height: 1.2;
  color: var(--ink);
  letter-spacing: -.012em;
  margin: 0;
}

.cert-issuer {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  font-size: .85rem;
  font-weight: 400;
  color: var(--ink-2);
  margin: .1rem 0 0;
}

.bullet {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--emerald);
  box-shadow: 0 0 8px var(--emerald);
  flex-shrink: 0;
}

.card-foot {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding-top: 1rem;
  border-top: 1px dashed var(--line);
}

.cred-id {
  display: inline-flex;
  align-items: baseline;
  gap: .5rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: .7rem;
  color: var(--ink-3);
  letter-spacing: .04em;
  min-width: 0;
  overflow: hidden;
}

.cred-id-k {
  font-size: .58rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--ink-3);
  flex-shrink: 0;
}

.cred-id-v {
  color: var(--ink-2);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.verify {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: .7rem;
  font-weight: 500;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ink);
  text-decoration: none;
  padding: .45rem .75rem;
  border: 1px solid var(--line-2);
  border-radius: 999px;
  transition: all .2s;
  white-space: nowrap;
  flex-shrink: 0;
}

.verify .arr { transition: transform .2s; display: inline-block; }
.verify:hover { border-color: var(--lime); color: var(--lime); }
.verify:hover .arr { transform: translate(2px, -2px); }

.corner-glyph {
  position: absolute;
  top: 50%;
  right: -1.5rem;
  font-family: 'Playfair Display', serif;
  font-size: 8rem;
  font-style: italic;
  color: rgba(203,255,72,.04);
  pointer-events: none;
  transition: color .35s, transform .5s cubic-bezier(.2,.7,.3,1);
  z-index: 0;
  transform: translateY(-50%);
}

.cert-card:hover .corner-glyph {
  color: rgba(203,255,72,.10);
  transform: translateY(-50%) rotate(-8deg) scale(1.05);
}

.section-foot {
  position: relative;
  z-index: 1;
  margin: 1rem auto 0;
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem 1rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink-2);
}

.legend { display: inline-flex; align-items: center; gap: .55rem; }
.legend.ghost { color: var(--ink-3); margin-left: auto; }
.legend-dot { width: 7px; height: 7px; border-radius: 50%; }
.legend-dot.live { background: var(--emerald); box-shadow: 0 0 10px var(--emerald); }
.legend-dot.warn { background: var(--lime);    box-shadow: 0 0 10px var(--lime); }
.sep { color: var(--ink-3); }

:deep(.carousel__prev),
:deep(.carousel__next) {
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  background: rgba(16, 10, 10, 0.04);
  border: 1px solid var(--line-2);
  color: var(--ink-2);
  backdrop-filter: blur(8px);
  transition: .2s;
  font-size: 1rem;
}

:deep(.carousel__prev:hover),
:deep(.carousel__next:hover) {
  background: var(--lime);
  border-color: var(--lime);
  color: #0a0a0a;
  box-shadow: 0 0 24px rgba(203,255,72,.4);
}



</style>
