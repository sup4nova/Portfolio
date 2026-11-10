<template>
  <section id="contact" class="section t-melon bg-dots">
    <svg class="deco sparkle" style="--s: 40px; right: 8%; top: 12%" aria-hidden="true"><use href="#spark" /></svg>
    <svg class="deco sticker" style="--s: 52px; left: 6%; bottom: 10%; --c: var(--c-3)" aria-hidden="true"><use href="#star" /></svg>

    <div class="section__in">
      <div class="win contact">
        <div class="win__bar">
          <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="win__title">continue.exe</span>
        </div>

        <div class="win__body contact__body">
          <span class="label">World 7 · 続ける？</span>
          <h2 class="h-display glitch section__title">Continue?</h2>
          <p class="contact__text">
            Open to work: CDI, hybrid, EU + remote, from Q3 2026. IT support engineering, internal IT and
            cybersecurity-adjacent roles.
          </p>

          <div class="row contact__actions">
            <a class="btn btn--accent" href="mailto:contact@sup4nova.com">Yes · email me ↗</a>
            <a class="btn" href="#contact">🤝 Are we a match?</a>
            <a class="btn btn--ghost" href="https://github.com/sup4nova" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
          </div>

          <span class="tag tag--live">Open to work · Q3 2026</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.contact {
  max-width: 44rem;
  margin: 0 auto;
}
.contact__body {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  padding: 2.2rem 1.6rem 2.4rem;
  text-align: center;
}
.contact__text {
  max-width: 46ch;
  margin: 0 0 1.4rem;
}
.contact__actions {
  justify-content: center;
  margin-bottom: 1.4rem;
}
</style>
