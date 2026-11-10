<template>
  <section class="section t-lemon bg-gingham">
    <svg class="deco sparkle" style="--s: 34px; left: 6%; top: 12%; --c: #fff" aria-hidden="true"><use href="#spark" /></svg>

    <div class="section__in">
      <div class="win longcard">
        <div class="win__bar">
          <span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="win__title">Tailwind CSS</span>
        </div>

        <div class="win__body longcard__body">
          <div class="frame frame--flower longcard__frame">
            <div class="ph">your illustration</div>
          </div>

          <p class="longcard__text">
            Nuxt UI integrates with the latest Tailwind CSS v4, bringing significant improvements.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.longcard {
  max-width: 48rem;
  margin: 0 auto;
}
.longcard__body {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}
.longcard__frame {
  flex: none;
  width: 12rem;
}
.longcard__text {
  margin: 0;
  font-size: 0.95rem;
}
@media (max-width: 880px) {
  .longcard__body {
    flex-direction: column;
    align-items: stretch;
  }
  .longcard__frame {
    width: 60%;
    margin: 0 auto;
  }
}
</style>
