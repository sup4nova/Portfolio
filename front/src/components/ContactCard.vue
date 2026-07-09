<script setup lang="ts">
import logo from '../assets/sup4nova-logo.png'


function openEmail() {
  const user = 'tcatnoc'
  const domain = 'moc.avon4pus'
  window.location.href = `mailto:${user.split('').reverse().join('')}@${domain.split('').reverse().join('')}`
}
</script>

<template>
  <section class="contact-section">
    <div class="contact-card">

      <div class="contact-avatar">
        <img :src="logo" alt="Sup4nova" class="avatar-img" />
        <span class="avatar-status"></span>
      </div>

      <div class="contact-info">
        <div class="contact-top">
          <h3 class="contact-name">Sup4nova</h3>
        </div>
        <p class="contact-role">Cyber · Dev · ML 𖦹 France</p>
        <p class="contact-desc"> Have a question in mind? Feel free to reach out through my LinkedIn or Email right here. </p>
      </div>

      <div class="contact-actions">
        <button @click="openEmail" class="btn-primary">
          Email ↗
        </button>
        <a href="https://linkedin.com/in/anais-b-281a272a0" target="_blank" rel="noopener noreferrer" class="btn-ghost">
          LinkedIn
        </a>
      </div>

    </div>
  </section>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;700&family=Playfair+Display:ital,wght@1,700&display=swap');

@keyframes statusPulse {
  0%, 100% { box-shadow: 0 0 0 0 #00bb8170; }
  50%       { box-shadow: 0 0 0 7px #00bb8100; }
}

@keyframes cardSlideIn {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}

.contact-section {
  margin-top: 7rem;
  margin-bottom: 7rem; 
  display: flex;
  justify-content: center;
}

.contact-card {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  background: #0d0d0d;
  border: 1px solid #CBFF4815;
  border-radius: 1.5rem;
  padding: 1.5rem 2rem;
  width: 90%;
  max-width: 1200px;
  transition: box-shadow 0.3s, transform 0.3s, border-color 0.3s;
  animation: cardSlideIn 0.8s cubic-bezier(0.22, 1, 0.36, 1) both 0.1s;
}

.contact-card:hover {
  transform: translateY(-4px);
  border-color: #00bb8130;
  box-shadow: 0 20px 48px #00bb8112;
}

.contact-avatar {
  position: relative;
  flex-shrink: 0;
  width: 64px;
  height: 64px;
}

.avatar-img {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #CBFF48;
  background: #f7f6f0;
}

.avatar-status {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #00bb81;
  border: 2px solid #0d0d0d;
  animation: statusPulse 2s ease-in-out infinite;
}

.contact-info {
  flex: 1;
  font-family: 'DM Sans', sans-serif;
}

.contact-top {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 2px;
}

.contact-name {
  font-family: 'Playfair Display', serif;
  font-size: 1.15rem;
  font-style: italic;
  font-weight: 700;
  color: #CBFF48;
  margin: 0;
}

.contact-badge {
  font-size: 0.62rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #0a0a0a;
  background: #CBFF48;
  padding: 2px 8px;
  border-radius: 4px;
}

.contact-role {
  font-size: 0.75rem;
  color: #00bb81;
  letter-spacing: 0.04em;
  margin: 0 0 0.5rem;
}

.contact-desc {
  font-size: 0.85rem;
  font-weight: 300;
  color: #555;
  line-height: 1.6;
  margin: 0;
}

.contact-desc em {
  font-style: normal;
  font-weight: 500;
  color: #EDEDED;
  border-bottom: 1.5px solid #CBFF48;
  padding-bottom: 1px;
}

.contact-actions {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  flex-shrink: 0;
}

.btn-primary {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.8rem;
  font-weight: 500;
  color: #0a0a0a;
  background: #CBFF48;
  padding: 0.55rem 1.25rem;
  border-radius: 999px;
  border: none;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
  transition: box-shadow 0.2s, transform 0.2s;
  white-space: nowrap;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 18px #CBFF4850;
}

.btn-ghost {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.8rem;
  font-weight: 400;
  color: #555;
  border: 1px solid #33333320;
  padding: 0.55rem 1.25rem;
  border-radius: 999px;
  text-decoration: none;
  text-align: center;
  transition: border-color 0.2s, color 0.2s;
  white-space: nowrap;
}

.btn-ghost:hover {
  border-color: #00bb81;
  color: #00bb81;
}

@media (max-width: 600px) {
  .contact-card { flex-direction: column; text-align: center; }
  .contact-top { justify-content: center; }
  .contact-actions { flex-direction: row; }
}
</style>
