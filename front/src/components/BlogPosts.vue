<script setup lang="ts">
import { ref } from 'vue'

const posts = ref([
  {
    title: 'Synorva',
    description: 'Design a multimodal tool that analyzes music & images, maps their emotions (valence–arousal), associates media with each other and generates coherent audio tracks from images/videos.',
    date: '2025-10-30',
    try: 'http://localhost:5174/',
    page: 'https://github.com/sup4nova/Synorva'
  },
  {
    title: 'Nuxt 3.14',
    description: 'Nuxt 3.14 is out!',
    date: '2024-11-04'
  },
  {
    title: 'Nuxt 3.13',
    description: 'Nuxt 3.13 is out!',
    date: '2024-08-22'
  }
])
</script>

<template>
  <section id="projects" class="section t-melon bg-stripes">
    <svg class="deco sticker" style="--s: 48px; right: 5%; top: 6%" aria-hidden="true"><use href="#star" /></svg>

    <div class="section__in">
      <span class="label">Projects</span>
      <h2 class="h-display section__title">Latest Posts</h2>

      <div class="posts">
        <article v-for="post in posts" :key="post.title" class="win">
          <div class="win__bar">
            <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
            <span class="win__title">{{ new Date(post.date).toDateString() }}</span>
          </div>

          <div class="win__body post">
            <div class="frame frame--checker post__img">
              <div class="ph">{{ post.title }}</div>
            </div>

            <div class="post__content">
              <h3 class="post__title">{{ post.title }}</h3>
              <p class="post__desc">{{ post.description }}</p>
              <div v-if="post.try || post.page" class="row">
                <a v-if="post.try" :href="post.try" target="_blank" rel="noreferrer" class="btn btn--accent">
                  Try it →
                </a>
                <a v-if="post.page" :href="post.page" target="_blank" rel="noreferrer" class="btn">
                  Read more →
                </a>
              </div>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.posts {
  display: grid;
  gap: 2rem;
}
.post {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}
.post__img {
  flex: none;
  width: 11rem;
}
.post__content {
  flex: 1;
  min-width: 0;
}
.post__title {
  margin: 0 0 0.4rem;
  font: 600 var(--fs-h3) / 1.25 var(--f-body);
}
.post__desc {
  margin: 0 0 1rem;
}
@media (max-width: 880px) {
  .post {
    flex-direction: column;
    align-items: stretch;
  }
  .post__img {
    width: 9rem;
  }
}
</style>
