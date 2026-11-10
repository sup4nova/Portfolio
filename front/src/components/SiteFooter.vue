<template>
  <footer class="footer">
    <div class="footer__in">
      <span>© 2026 Sup4nova</span>
      <span class="footer__pixel">7 worlds · 1 player</span>
      <a href="mailto:contact@sup4nova.com">contact@sup4nova.com</a>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  padding: 1.6rem 0;
  border-top: var(--line);
  background: var(--paper);
  font-size: 0.9rem;
}
.footer__in {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 0.6rem 1.5rem;
  max-width: var(--container);
  margin: 0 auto;
  padding: 0 clamp(1.2rem, 4vw, 2.5rem);
}
.footer__pixel {
  font: var(--fs-pixel) var(--f-pixel);
  letter-spacing: var(--ls-pixel);
  text-transform: uppercase;
}
</style>
