<script setup lang="ts">
const year = new Date().getFullYear()
</script>

<template>
  <footer class="footer">

    <div class="footer-inner">

      <div class="footer-left">
        <span class="footer-logo">Sup4nova</span>
      </div>

      <div class="footer-links">
        <a href="https://github.com/sup4nova" target="_blank" rel="noopener noreferrer" class="flink">GitHub</a>
        <span class="fsep">·</span>
        <RouterLink to="/about" class="flink">About</RouterLink>
        <span class="fsep">·</span>
        <RouterLink to="/contact" class="flink">Contact</RouterLink>
      </div>

      <div class="footer-right">
        <span class="footer-copy">© {{ year }} Sup4nova</span>
      </div>

    </div>
    
  </footer>
</template>

<style scoped>

.footer {
  border-top: 1px solid #1a1a1a10;
  padding: 2rem 2.5rem 0;
  font-family: 'DM Sans', sans-serif;
}

.footer-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  padding-bottom: 1.5rem;
}

.footer-left {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.footer-logo {
  font-family: 'Playfair Display', serif;
  font-size: 1rem;
  font-style: italic;
  font-weight: 700;
  color: #CBFF48;
  letter-spacing: -0.01em;
}

.footer-tagline {
  font-size: 0.7rem;
  color: #00bb81;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.footer-links {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.flink {
  font-size: 0.8rem;
  font-weight: 400;
  color: #888;
  text-decoration: none;
  transition: color 0.2s;
}

.flink:hover {
  color: #CBFF48;
}

.fsep {
  font-size: 0.7rem;
  color: #ccc;
}

.footer-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 2px;
}

.footer-copy {
  font-size: 0.75rem;
  color: #aaa;
}

.footer-made {
  font-size: 0.7rem;
  color: #ccc;
}

.heart {
  color: #00bb81;
}

@keyframes gradientShift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* bottom accent bar */
.footer-bar {
  max-width: 1280px;
  margin: 0 auto;
  height: 3px;
  background: linear-gradient(90deg, #00bb81, #CBFF48, #00bb81, #CBFF48);
  background-size: 300% 100%;
  border-radius: 999px;
  animation: gradientShift 4s ease infinite;
}

@media (max-width: 600px) {
  .footer-inner { flex-direction: column; align-items: flex-start; }
  .footer-right { align-items: flex-start; }
}
</style>
