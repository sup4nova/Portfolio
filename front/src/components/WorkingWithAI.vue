<!-- WorkingWithAI.vue -->

<template>
  <section class="ai-section">
    <span class="bg-grid"></span>
    <span class="bg-glow"></span>

    <header class="section-header">
      <div class="head-l">
        <h2 class="section-title">How I use <em class="t-it">AI</em> on my projects</h2>
        <p class="section-sub">
           AI is part of my workflow. It doesn't replace my thinking, but helps me move faster on the parts that don't need it. I stay in control of what matters and let AI handle what it's good at.
        </p>
      </div>
      <aside class="tools-card">
        <span class="tools-gh">Tools</span>
        <ul class="tools-list">
          <li><span>Claude AI</span></li>
          <li><span>ChatGPT</span></li>
        </ul>
      </aside>
    </header>


    <ol class="lanes">
      <li class="lane" style="--accent:#cbff48">
        <span class="accent-strip"></span>
        <div class="lane-head"><span class="lane-tag"><span class="lane-sym">◉</span> Owned</span></div>
        <h3 class="lane-title">Architecture &amp; decisions</h3>
        <p class="lane-body">Data modeling, tech choices, system design and technical documentation — I own these. AI isn't reliable enough here, and the judgment has to be mine.</p>
      </li>
      <li class="lane" style="--accent:#5ee9c8">
        <span class="accent-strip"></span>
        <div class="lane-head"><span class="lane-tag"><span class="lane-sym">◐</span> Delegated</span></div>
        <h3 class="lane-title">Repetitive work</h3>
        <p class="lane-body">Boilerplate, repetitive front-end implementation, code audits and quick second opinions. AI earns its place when the task is well-defined and the output is verifiable.</p>
      </li>
      <li class="lane" style="--accent:#00bb81">
        <span class="accent-strip"></span>
        <div class="lane-head"><span class="lane-tag"><span class="lane-sym">◇</span> Exploring</span></div>
        <h3 class="lane-title">Learning &amp; new ground</h3>
        <p class="lane-body">Ramping up on unfamiliar tech and areas outside my specialty — like UI/UX. AI helps me get oriented fast; I refine and validate with my own judgment.</p>
      </li>
    </ol>
  </section>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

.ai-section {
  --lime:#cbff48; --emerald:#00bb81; --aqua:#5ee9c8;
  --ink:#fff; --ink-2:rgba(255,255,255,.62); --ink-3:rgba(255,255,255,.38);
  --line:rgba(255,255,255,.08); --line-2:rgba(255,255,255,.14);
  --bg:#151515; --bg-soft:rgba(255,255,255,.018);
  position:relative; isolation:isolate; padding:4.5rem clamp(1.25rem,5vw,3rem) 4rem;
  margin:4rem auto; width:90%; max-width:1200px;
  background:var(--bg); border:1px solid var(--line); border-radius:24px;
  overflow:hidden; color:var(--ink);
}


.section-header {
  position:relative; z-index:1; margin:0 auto 2.5rem;
  display:grid; grid-template-columns:1fr 260px; gap:2.5rem; align-items:end;
  padding-bottom:1.75rem; border-bottom:1px solid var(--line);
}

.head-l { display:flex; flex-direction:column; gap:.85rem; }

.section-eyebrow {
  display:inline-flex; align-items:center; gap:.65rem;
  font-family:'JetBrains Mono',monospace; font-size:.7rem; font-weight:500;
  letter-spacing:.22em; text-transform:uppercase; color:var(--emerald);
}

.dot {
  width:7px; height:7px; border-radius:50%;
  background:var(--emerald); box-shadow:0 0 10px var(--emerald);
  animation:pulse 1.8s infinite;
}

@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.35} }

.section-title {
  font-family:'Playfair Display',serif; font-weight:700;
  font-size:clamp(2.1rem,4.2vw,3.4rem); line-height:1.04;
  letter-spacing:-.025em; color:var(--ink); margin:0; max-width:18ch;
}

.t-it { color:var(--lime); font-style:italic; font-weight:400; }

.section-sub {
  font-family:'DM Sans',sans-serif; font-size:1.02rem; line-height:1.55;
  color:var(--ink-2); max-width:62ch; margin:.25rem 0 0;
}

.section-sub b { color:var(--ink); font-weight:600; }

.tools-card {
  display:flex; flex-direction:column; gap:.8rem; padding:1.25rem 1.4rem;
  background:linear-gradient(180deg,rgba(255,255,255,.025),transparent);
  border:1px solid var(--line); border-radius:14px;
}

.tools-gh {
  font-family:'JetBrains Mono',monospace; font-size:.62rem;
  letter-spacing:.22em; text-transform:uppercase; color:var(--ink-3);
}

.tools-list {
  list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:.55rem;
}

.tools-list li {
  display:flex; align-items:center; gap:.65rem;
  font-family:'DM Sans',sans-serif; font-size:1rem; font-weight:500; color:var(--ink-2);
}

.tool-dot {
  width:8px; height:8px; border-radius:50%;
  background:var(--lime); box-shadow:0 0 10px var(--lime);
}

.tools-list li:nth-child(2) .tool-dot { background:var(--aqua); box-shadow:0 0 10px var(--aqua); }

.tools-meta {
  font-family:'JetBrains Mono',monospace; font-size:.66rem; letter-spacing:.1em;
  text-transform:uppercase; color:var(--ink-3); padding-top:.6rem;
  border-top:1px dashed var(--line);
}

.spectrum {
  position:relative; z-index:1; margin:0 auto 1.75rem;
  display:flex; flex-direction:column; gap:.7rem;
}

.spectrum-track {
  display:block; height:6px; border-radius:999px;
  background:rgba(255,255,255,.06); position:relative; overflow:hidden;
}

.spectrum-fill {
  position:absolute; inset:0;
  background:linear-gradient(90deg,var(--lime) 0%,var(--aqua) 50%,var(--emerald) 100%);
  opacity:.85;
}

.spectrum-labels {
  display:flex; justify-content:space-between; gap:1rem;
  font-family:'JetBrains Mono',monospace; font-size:.68rem;
  letter-spacing:.08em; text-transform:uppercase; color:var(--ink-2);
}

.sl { display:inline-flex; align-items:center; gap:.45rem; }
.sl-dot { width:7px; height:7px; border-radius:50%; }
.sl-dot.mine { background:var(--lime); }
.sl-dot.manual { background:var(--aqua); }
.sl-dot.assisted { background:var(--emerald); }

.lanes {
  position:relative; z-index:1; margin:0 auto;
  list-style:none; padding:0; display:grid;
  grid-template-columns:repeat(3,1fr); gap:1.25rem;
}

.lane {
  --accent:var(--lime);
  position:relative; display:flex; flex-direction:column; gap:.85rem;
  padding:1.6rem 1.6rem 1.5rem 1.85rem;
  background:linear-gradient(180deg,var(--bg-soft),transparent 70%);
  border:1px solid var(--line); border-radius:16px; overflow:hidden;
  transition:transform .3s cubic-bezier(.2,.7,.3,1),border-color .25s;
}

.lane:hover { transform:translateY(-4px); border-color:var(--line-2); }
.lane:hover .accent-strip { transform:scaleY(1); opacity:1; }
.lane:hover .lane-title { color:var(--accent); }

.accent-strip {
  position:absolute; left:0; top:1.6rem; bottom:1.6rem; width:3px;
  background:var(--accent); border-radius:999px; opacity:.45;
  transform:scaleY(.5); transform-origin:top;
  transition:transform .35s cubic-bezier(.2,.7,.3,1),opacity .25s;
}

.lane-head { display:flex; align-items:center; justify-content:space-between; gap:.5rem; }

.lane-tag {
  display:inline-flex; align-items:center; gap:.45rem;
  padding:.28rem .7rem; border-radius:999px;
  font-family:'JetBrains Mono',monospace; font-size:.66rem; font-weight:600;
  letter-spacing:.16em; text-transform:uppercase; color:var(--accent);
  background:color-mix(in srgb,var(--accent) 12%,transparent);
  border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);
}

.lane-sym { font-size:.8rem; }
.lane-idx { font-family:'JetBrains Mono',monospace; font-size:.64rem; letter-spacing:.12em; color:var(--ink-3); }

.lane-title {
  font-family:'Playfair Display',serif; font-size:1.5rem; font-weight:700;
  line-height:1.12; letter-spacing:-.012em; color:var(--ink); margin:0;
  transition:color .25s; text-wrap:pretty;
}

.lane-body {
  font-family:'DM Sans',sans-serif; font-size:.92rem; line-height:1.55;
  color:var(--ink-2); margin:0; flex:1;
}

.meter {
  margin-top:.4rem; padding-top:1rem; border-top:1px dashed var(--line);
  display:flex; flex-direction:column; gap:.5rem;
}

.meter-row { display:flex; align-items:center; gap:.6rem; }

.meter-end {
  font-family:'JetBrains Mono',monospace; font-size:.6rem; letter-spacing:.12em;
  text-transform:uppercase; color:var(--ink-3); white-space:nowrap;
}

.meter-end.me { color:var(--accent); }

.meter-bar {
  position:relative; flex:1; height:5px; border-radius:999px;
  background:rgba(255,255,255,.08);
}

.meter-fill {
  position:absolute; left:0; top:0; bottom:0; border-radius:999px;
  background:linear-gradient(90deg,var(--accent),color-mix(in srgb,var(--accent) 50%,var(--emerald)));
}

.meter-knob {
  position:absolute; top:50%; width:11px; height:11px; border-radius:50%;
  background:#0a0a0a; border:2px solid var(--accent);
  transform:translate(-50%,-50%);
  box-shadow:0 0 10px color-mix(in srgb,var(--accent) 60%,transparent);
}

.meter-readout {
  font-family:'JetBrains Mono',monospace; font-size:.66rem;
  letter-spacing:.06em; color:var(--ink-2); align-self:flex-end;
}

.learned {
  position:relative; z-index:1; margin:2.5rem auto 0;
  padding:2.5rem 2.75rem;
  background:radial-gradient(600px 240px at 88% 0%,rgba(203,255,72,.07),transparent 60%),
    linear-gradient(180deg,rgba(255,255,255,.022),transparent);
  border:1px solid var(--line); border-radius:20px; overflow:hidden;
}

.quote-mark {
  position:absolute; top:-1.5rem; left:1.5rem;
  font-family:'Playfair Display',serif; font-style:italic; font-weight:700;
  font-size:9rem; line-height:1; color:rgba(203,255,72,.10);
  pointer-events:none; user-select:none;
}

.learned blockquote {
  margin:0; position:relative; z-index:1;
  font-family:'Playfair Display',serif; font-weight:400; font-style:italic;
  font-size:clamp(1.25rem,2.4vw,1.85rem); line-height:1.4;
  letter-spacing:-.01em; color:var(--ink); max-width:56ch; text-wrap:pretty;
}

.learned blockquote em { font-style:italic; color:var(--aqua); }

.learned blockquote .hl {
  font-style:normal;
  background:linear-gradient(180deg,transparent 62%,rgba(203,255,72,.42) 62%);
  padding:0 4px;
}

.learned figcaption {
  display:flex; align-items:center; gap:.85rem;
  margin-top:1.75rem; position:relative; z-index:1;
}

.fc-avatar {
  width:38px; height:38px; border-radius:50%; display:flex;
  align-items:center; justify-content:center;
  background:linear-gradient(135deg,var(--lime),var(--emerald));
  color:#04141a; font-family:'Playfair Display',serif; font-style:italic;
  font-weight:700; font-size:1.05rem;
}

.fc-text { font-family:'JetBrains Mono',monospace; font-size:.78rem; letter-spacing:.06em; color:var(--ink-3); }
.fc-text b { color:var(--ink); font-weight:500; }

@media (max-width:980px) {
  .section-header { grid-template-columns:1fr; gap:1.5rem; }
  .lanes { grid-template-columns:1fr; }
  .spectrum-labels { flex-direction:column; gap:.4rem; }
}

@media (max-width:640px) {
  .ai-section { padding:3rem 1.25rem; }
  .learned { padding:2rem 1.5rem; }
}
</style>
