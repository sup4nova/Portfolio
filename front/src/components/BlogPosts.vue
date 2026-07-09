<!-- BlogPosts.vue -->

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import asset1 from '../assets/asset1.svg'
import asset2 from '../assets/asset2.svg'
import asset3 from '../assets/asset3.svg'
import asset4 from '../assets/asset4.svg'

const posts = ref([
  {
    title: 'Synorva',
    tag: '2025 R&D Project',
    badge: 'Demo Online',
    badgeType: 'yellow',
    description: 'Design a multimodal tool that analyzes music & images, maps their emotions (valence–arousal), associates media with each other and generates coherent audio tracks from images/videos.',
    image: asset1,
    tryUrl: 'https://github.com/sup4nova/Synorva',
    pageUrl: 'https://sup4nova.com/projects/synorva',
    slideUrl: 'https://sup4nova.com/projects/synorva/slides'
  },
  {
    title: 'Jobscraper',
    tag: '2026 Side Projects',
    badge: 'Demo Online',
    badgeType: 'yellow',
    description: 'A web scraper for extracting job listings from various online platforms.',
    image: asset2,
    tryUrl: 'https://github.com/sup4nova/Jobscraper',
    pageUrl: 'https://sup4nova.com/projects/jobscraper',
    slideUrl: 'https://sup4nova.com/projects/jobscraper/slides'

  },
  {
    title: 'JavaCryptoTool',
    tag: '2024 Course Project',
    badge: "Online",
    badgeType: 'yellow',
    description: 'A Java-based application that provides a suite of cryptographic tools for encryption, decryption, hashing, and key management.',
    image: asset3,
    tryUrl: 'https://github.com/sup4nova/JavaCryptoTool',
    pageUrl: 'https://sup4nova.com/projects/javacryptotool/',
    slideUrl: 'https://sup4nova.com/projects/javacryptotool/slides'
  },
  {
    title: 'RandomSpotifyGenerator',
    tag: '2026 Side Project',
    badge: "Upcoming",
    badgeType: 'dim',
    description: 'A webapp that generates random Spotify playlists or picks random tracks, artists, or albums from your library, helping you rediscover your music and break out of listening habits.',
    image: asset4,
    sneakpeekUrl: 'https://sup4nova.com/projects/random-spotify-generator/sneakpeek',
  }
])

const sectionRef = ref<HTMLElement | null>(null)
const revealed = ref(false)

onMounted(() => {
  const observer = new IntersectionObserver(
    ([entry]) => { if (entry?.isIntersecting) { revealed.value = true; observer.disconnect() } },
    { threshold: 0.1 }  
  )
  if (sectionRef.value) observer.observe(sectionRef.value)
})
</script>

<template>
<section ref="sectionRef" id="projects" class="posts-section" :class="{ 'posts-revealed': revealed }">
    <div class="section-header reveal-item" style="--delay: 0s">
      <span class="section-eyebrow">✦ Latest</span>
      <h2 class="section-title">Projects & Posts</h2>
        <p class="section-sub">
          A selection of my latest projects, writings, and experiments across software development, ML, and beyond.<br>
          Only demos are live for now and the projects are under continuous development. The code is on my GitHub but feel free to reach out for more!</p>
    </div>

    <div class="posts-grid">
      <article
        v-for="(post, index) in posts"
        :key="index"
        class="post-card reveal-item"
        :class="{ 'post-card--featured': index === 0 }"
        :style="`--delay: ${0.15 + index * 0.12}s`"
      >
        <div v-if="post.image" class="post-img-wrap">
          <img :src="post.image" :alt="post.title" class="post-img" />
        </div>
        <div v-else class="post-img-placeholder">
          <span>✦</span>
        </div>

        <div class="post-body">
          <div class="post-meta">
            <span class="post-tag">{{ post.tag }}</span>
            <span v-if="post.badge" :class="['post-status', `post-status--${post.badgeType}`]">{{ post.badge }}</span>
          </div>

          <h3 class="post-title">{{ post.title }}</h3>
          <p class="post-desc">{{ post.description }}</p>

          <div class="post-actions">
            <a
              v-if="post.tryUrl"
              :href="post.tryUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="btn-ghost"
            >
              GitHub ↗
            </a>
            <a
              v-if="post.sneakpeekUrl"
              :href="post.sneakpeekUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="btn-ghost"
            >
              Sneak Peek ↗
            </a>
            <a
              v-if="post.slideUrl"
              :href="post.slideUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="btn-ghost"
            >
              Slides ↗
            </a>
            <a
              v-if="post.pageUrl"
              :href="post.pageUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="btn-primary"
            >
              Try the Demo ↗
            </a>
          </div>
        </div>
      </article>
    </div>

  </section>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

@keyframes revealUp {
  from { opacity: 0; transform: translateY(28px); }
  to   { opacity: 1; transform: translateY(0); }
}

.reveal-item {
  opacity: 0;
  transform: translateY(28px);
}

.posts-revealed .reveal-item {
  animation: revealUp 0.7s cubic-bezier(0.22, 1, 0.36, 1) forwards var(--delay, 0s);
}



.posts-section{
  min-height: 92vh;
  background-color: #151515;
  border: 1px solid rgba(255,255,255,.08);
  padding: 2.5rem clamp(1.25rem, 5vw, 2.5rem);
  border-radius: 24px;
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  overflow: hidden;
}

.section-header {
  margin-bottom: 3rem;
}

.section-eyebrow {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.72rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #00bb81;
  display: block;
  margin-bottom: 0.5rem;
}


.section-sub {
  font-family:'DM Sans',sans-serif; font-size:1.02rem; line-height:1.55;
  color:var(--ink-3, #aaa); margin:.25rem 0 0;
}

.section-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 700;
  color: #CBFF48;
  margin: 0;
  letter-spacing: -0.02em;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  align-items: stretch;
}

.post-card:not(.post-card--featured):not(:last-child) .post-img-wrap {
  height: 180px;
  flex-shrink: 0;
}

.post-card:not(.post-card--featured):not(:last-child) .post-img {
  height: 180px;
}

.post-card {
  background: #000000;  
  border-radius: 1.5rem;
  overflow: hidden;
  border: 1px solid #1a1a1a0e;
  display: flex;
  flex-direction: column;
  transition: transform 0.25s, box-shadow 0.25s;
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 48px #00bb8112, 0 0 0 1px #00bb8118;
}

.post-card--featured {
  grid-column: span 2;
  flex-direction: row;
}

.post-card:last-child {
  grid-column: span 2;  
  flex-direction: row;
}

.post-card:last-child .post-img-wrap {
  width: 25%;
  max-width: 25%;
  flex-shrink: 0;
}

.post-img-wrap {
  overflow: hidden;
  flex-shrink: 0;
  align-self: stretch;
}

.post-card--featured .post-img-wrap {
  width: 25%;
}

.post-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.4s ease;
}

.post-card:hover .post-img {
  transform: scale(1.04);
}

.post-img-placeholder {
  background: linear-gradient(135deg, #00bb8115, #CBFF4825);
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  color: #00bb8160;
  flex-shrink: 0;
}

.post-card--featured .post-img-placeholder {
  width: 45%;
  height: auto;
}

.post-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  flex: 1;
}

.post-meta {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.post-tag {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.68rem;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #0a0a0a;
  background: #CBFF48;
  padding: 0.2rem 0.65rem;
  border-radius: 999px;
}

.post-status {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.6rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
}

.post-status--yellow {
  background: #CBFF4818;
  color: #CBFF48;
  border: 1px solid #CBFF4835;
}

.post-status--dim {
  background: #ffffff08;
  color: #555;
  border: 1px solid #2a2a2a;
}

.post-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.4rem;
  font-weight: 700;
  color: #f0f0f0;
  margin: 0;
  line-height: 1.25;
}

.post-desc {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9rem;
  font-weight: 300;
  color: #aaa;
  line-height: 1.7;
  margin: 0;
  flex: 1;
}

.post-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-top: 0.5rem;
}

.btn-primary {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.82rem;
  font-weight: 500;
  color: #0a0a0a;
  background: #CBFF48;
  padding: 0.55rem 1.25rem;
  border-radius: 999px;
  text-decoration: none;
  transition: box-shadow 0.2s, transform 0.2s;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 18px #CBFF4850;
}

.btn-ghost {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.82rem;
  font-weight: 400;
  color: #888;
  background: transparent;
  border: 1px solid #33333325;
  padding: 0.55rem 1.25rem;
  border-radius: 999px;
  text-decoration: none;
  transition: border-color 0.2s, color 0.2s;
}

.btn-ghost:hover {
  border-color: #00bb81;
  color: #00bb81;
}

@media (min-width: 769px) and (max-width: 1100px) {
  .posts-grid { grid-template-columns: 1fr 1fr; }

  .post-card--featured,
  .post-card:last-child {
    grid-column: 1 / -1;
    flex-direction: column;
  }

  .post-card--featured .post-img-wrap,
  .post-card:last-child .post-img-wrap {
    width: 100%;
    max-width: 100%;
    height: 200px;
  }
}

@media (max-width: 768px) {
  .posts-grid { grid-template-columns: 1fr; }

  .post-card--featured,
  .post-card:last-child {
    grid-column: auto;
    flex-direction: column;
  }

  .post-card--featured .post-img-wrap,
  .post-card:last-child .post-img-wrap {
    width: 100%;
    max-width: 100%;
    height: 180px;
  }
}

</style>
