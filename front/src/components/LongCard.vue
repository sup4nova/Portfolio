<script setup lang="ts">
import { ref, onMounted } from 'vue'
const visible = ref(false)

onMounted(() => {
  requestAnimationFrame(() => {
    visible.value = true
  })
})

function scrollToContact() {
  document.getElementById('contact')?.scrollIntoView({
    behavior: 'smooth',
    block: 'start'
  })
}
</script>

<template>
  <div style="margin-bottom: 1rem;">
    <div class="shell">
        <div class="mb-10"> </div>
        <div class="header">
          <div class="av">
            <span class="av-txt">:)</span>
          </div>
          <div class="hinfo">
            <div class="hname">Sup4nova</div>
            <div class="hrole">Cyber · Development · AI</div>
            <div class="hbadges">
              <span class="hb hb-y">Open to work</span>
              <span class="hb hb-y">Side projects</span>
              <span class="hb hb-y">FR : Native</span>
              <span class="hb hb-y">ENG : Fluent</span>
            </div>
          </div>
          <div class="hloc">
            <span class="loc-label">Based in</span>
            <span class="city">France</span>
            <span class="lang">EN / FR</span>
          </div>
        </div>

        <div class="body">
          <div class="col">
            <div class="col-title">About</div>
            <p class="bio-txt">
              I’m a curious builder shaped by code, support, 
              and the constant desire to learn what lies beyond the familiar.
              From exploring the foundations of AI to blending development and cybersecurity knowledge, 
              I create with both logic and intuition in mind.
              My journey began by helping users solve problems directly listening first, understanding 
              frustration, and learning that good technology should feel human before it feels impressive.
              That experience still guides every project I touch today.
            </p>
            <div style="margin-top: 1rem;">
              <div class="col-title">Stack</div>
              <div class="stack-grid">
                <span class="stag">Vue 3</span>
                <span class="stag">TypeScript</span>
                <span class="stag">Vite</span>
                <span class="stag">Node.js</span>
                <span class="stag">Python</span>
                <span class="stag">AI / ML</span>
                <span class="stag">Powershell</span>
                <span class="stag">Sound design</span>
                <span class="stag">Java</span>
              </div>
            </div>
          </div>

          <div class="col">
            <div class="col-title">Projects</div>
            <div class="proj-list">
              <a href="https://github.com/sup4nova/Synorva" target="_blank" rel="noopener noreferrer" class="proj">
                <div class="proj-dot proj-dot--yellow"></div>
                <div class="proj-info">
                  <div class="proj-name-row">
                    <div class="proj-name">Synorva</div>
                    <span class="proj-badge proj-badge--y">Beta · Demo</span>
                    <span class="proj-tag">Private Project</span>
                  </div>
                  <div class="proj-sub">Multimodal AI tool that analyzes music and visuals and generates coherent audio tracks</div>
                </div>
                <span class="proj-arr">↗</span>
              </a>
              <a href="https://github.com/sup4nova" target="_blank" rel="noopener noreferrer" class="proj">
                <div class="proj-dot proj-dot--dim"></div>
                <div class="proj-info">
                  <div class="proj-name-row">
                    <div class="proj-name">Jobscraper</div>
                    <span class="proj-badge proj-badge--dim">Local · Demo</span>
                    <span class="proj-tag">Private Project</span>
                  </div>
                  <div class="proj-sub">AI-powered job scraping and CV generation tool. Functional locally — AI bot &amp; Discord bot coming soon. Video demo planned.</div>
                </div>
                <span class="proj-arr">↗</span>
              </a>
              <div class="proj proj--wip proj--full">
                <div class="proj-dot proj-dot--yellow"></div>
                <div class="proj-info">
                  <div class="proj-name-row">
                    <div class="proj-name">JavaCryptoTool</div>
                    <span class="proj-badge proj-badge--y">Online</span>
                    <span class="proj-tag">School Project</span>
                  </div>
                  <div class="proj-sub">Java-based AES encryption and decryption tool featuring a web interface and servlet backend for experimenting with cryptographic operations and secure text conversion.</div>
                </div>
                <span class="proj-arr proj-arr--dim">—</span>
              </div>
            </div>
          </div>
        </div>

        <div class="body">
          <div class="col">
            <div class="col-title">Fun Facts</div>
            <div class="facts-list">
              <div class="fact"><span class="fact-icon fact-icon--y">✦</span>I used to work at a cheese shop as a summer job, and I can probably recommend the perfect cheese for any mood</div>
              <div class="fact"><span class="fact-icon fact-icon--y">✦</span>Deeply passionate about music across every genre, it's my inspiration behind my projects</div>
            </div>
          </div>

          <div class="col">
            <div class="col-title">Hobbies</div>
            <div class="facts-list">
              <div class="fact"><span class="fact-icon fact-icon--g">▸</span>Cybersecurity learning : CTFs, security conferences  &amp; bug bounty initiation </div>
              <div class="fact"><span class="fact-icon fact-icon--g">▸</span>I love hiking and solo traveling to discover new places and perspectives</div>
            </div>
          </div>
        </div>

        <div class="footer">
          <div class="links">
            <a href="https://github.com/sup4nova" target="_blank" rel="noopener noreferrer" class="lbtn lbtn-y">GitHub ↗</a>
            <button
            type="button"
            class="lbtn lbtn-o"
            @click="scrollToContact"
          >
            Contact
          </button>
          </div>
          <div class="xp-bar">
            <span class="xp-label">XP</span>
            <div class="xp-track"><div class="xp-fill"></div></div>
            <span class="xp-lvl">Lvl 21</span>
          </div>
        </div>

      </div>
    </div>
</template>

  <style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@1,700&display=swap');

@keyframes onlinePulse {
  0%, 100% { box-shadow: 0 0 0 0 #00bb8160; }
  50%       { box-shadow: 0 0 0 6px #00bb8100; }
}

@keyframes xpFill {
  from { width: 0; }
  to   { width: 72%; }
}

@keyframes cardFadeIn {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}

.shell { background: #0d0d0d; border-radius: 20px;margin: 0 auto; padding: 2px; font-family: 'DM Sans', sans-serif; max-width: 90%; margin: 0 auto; animation: cardFadeIn 0.8s cubic-bezier(0.22, 1, 0.36, 1) both 0.2s; }
.shell-inner { background: #111; border-radius: 18px; margin-top: 30px; overflow: hidden; }

.header { background: #161616; border-bottom: 1px solid #CBFF4820; padding: 1.25rem 1.5rem; display: flex; align-items: center; gap: 1.25rem; }
.av { width: 64px; height: 64px; border-radius: 50%; background: #1a1a1a; border: 2px solid #CBFF48; display: flex; align-items: center; justify-content: center; flex-shrink: 0; position: relative; }
.av-txt { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-style: italic; font-weight: 700; color: #CBFF48; }
.av-online { position: absolute; bottom: 2px; right: 2px; width: 12px; height: 12px; border-radius: 50%; background: #00bb81; border: 2px solid #161616; animation: onlinePulse 2s ease-in-out infinite; }
.hinfo { flex: 1; }
.hname { font-size: 1.3rem; font-weight: 700; color: #f0f0f0; letter-spacing: -0.02em; line-height: 1.1; }
.hrole { font-size: 0.75rem; color: #00bb81; letter-spacing: 0.06em; text-transform: uppercase; margin-top: 3px; }
.hbadges { display: flex; gap: 6px; margin-top: 8px; flex-wrap: wrap; }
.hb { font-size: 0.62rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; padding: 3px 8px; border-radius: 4px; }
.hb-y { background: #CBFF4820; color: #CBFF48; border: 1px solid #CBFF4840; }
.hb-g { background: #00bb8115; color: #00bb81; border: 1px solid #00bb8130; }
.hb-w { background: #ffffff10; color: #aaa; border: 1px solid #ffffff15; }
.hloc { text-align: right; margin-left: auto; line-height: 1.5; }
.loc-label { display: block; font-size: 0.7rem; color: #555; }
.city { display: block; font-size: 0.82rem; color: #999; }
.lang { display: block; font-size: 0.7rem; color: #333; }

.body { display: grid; grid-template-columns: 1fr 1fr; border-bottom: 1px solid #1e1e1e; }
.col { padding: 1.25rem 1.5rem; border-right: 1px solid #1e1e1e; }
.col:last-child { border-right: none; }
.col-title { font-size: 0.6rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: #444; margin-bottom: 0.9rem; display: flex; align-items: center; gap: 6px; }
.col-title::before { content: ''; display: block; width: 14px; height: 1px; background: #CBFF48; }

.bio-txt { font-size: 0.82rem; font-weight: 300; color: #aaa; line-height: 1.7; }
.bio-txt em { font-style: normal; font-weight: 500; color: #CBFF48; }

.stack-grid { display: flex; flex-wrap: wrap; gap: 5px; }
.stag { font-size: 0.68rem; font-weight: 500; padding: 4px 9px; border-radius: 5px; border: 1px solid #2a2a2a; color: #888; background: #161616; transition: color 0.2s, border-color 0.2s; }
.stag:hover { color: #CBFF48; border-color: #CBFF4840; }

.proj-list { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.proj { display: flex; align-items: center; gap: 10px; padding: 8px 10px; border-radius: 8px; background: #161616; border: 1px solid #1e1e1e; text-decoration: none; transition: border-color 0.2s; cursor: pointer; }
.proj:hover { border-color: #CBFF4840; }
.proj--wip { cursor: default; }
.proj--full { grid-column: 1 / -1; }
.proj-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
.proj-dot--green  { background: #00bb81; }
.proj-dot--yellow { background: #CBFF48; }
.proj-dot--dim    { background: #333; }
.proj-info { flex: 1; min-width: 0; }
.proj-name-row { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
.proj-name { font-size: 0.8rem; font-weight: 500; color: #ddd; line-height: 1.2; }
.proj-badge { font-size: 0.55rem; font-weight: 600; letter-spacing: 0.07em; text-transform: uppercase; padding: 2px 6px; border-radius: 3px; }
.proj-badge--y { background: #CBFF4815; color: #CBFF48; border: 1px solid #CBFF4830; }
.proj-badge--dim { background: #ffffff08; color: #555; border: 1px solid #2a2a2a; }
.proj-sub { font-size: 0.68rem; color: #555; margin-top: 1px; }
.proj-tag { font-size: 0.52rem; font-weight: 600; letter-spacing: 0.07em; text-transform: uppercase; color: #444; margin-left: auto; white-space: nowrap; }
.proj-arr { font-size: 0.75rem; color: #555; flex-shrink: 0; }
.proj-arr--dim { color: #2a2a2a; }

.facts-list { display: flex; flex-direction: column; gap: 6px; }
.fact { display: flex; align-items: flex-start; gap: 8px; font-size: 0.78rem; font-weight: 300; color: #888; line-height: 1.5; }
.fact-icon { font-size: 0.7rem; margin-top: 3px; flex-shrink: 0; }
.fact-icon--y { color: #CBFF48; }
.fact-icon--g { color: #00bb81; }

.footer { padding: 1rem 1.5rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; background: #161616; }
.links { display: flex; gap: 8px; flex-wrap: wrap; }
.lbtn { font-size: 0.75rem; font-weight: 500; padding: 6px 14px; border-radius: 6px; text-decoration: none; transition: background 0.2s, color 0.2s, border-color 0.2s; }
.lbtn-y { background: #CBFF48; color: #0a0a0a; }
.lbtn-y:hover { background: #d4f040; }
.lbtn-o { background: #1a1a1a; color: #888; border: 1px solid #2a2a2a; }
.lbtn-o:hover { color: #CBFF48; border-color: #CBFF4840; }

.xp-bar { display: flex; align-items: center; gap: 8px; }
.xp-label { font-size: 0.62rem; color: #444; letter-spacing: 0.08em; text-transform: uppercase; }
.xp-track { width: 80px; height: 4px; background: #1e1e1e; border-radius: 2px; overflow: hidden; }
.xp-fill { height: 100%; width: 72%; background: #CBFF48; border-radius: 2px; animation: xpFill 1.4s cubic-bezier(0.22, 1, 0.36, 1) both 0.6s; }
.xp-lvl { font-size: 0.62rem; color: #555; }

@media (max-width: 600px) {
  .body { grid-template-columns: 1fr; }
  .col { border-right: none; border-bottom: 1px solid #1e1e1e; }
  .header { flex-wrap: wrap; }
  .hloc { margin-left: 0; text-align: left; }
  .proj-list { grid-template-columns: 1fr; }
  .proj--full { grid-column: auto; }
}
</style>
