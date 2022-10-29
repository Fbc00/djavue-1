<template>
  <div class="home-page">
    <div class="home-page__title">HELLO WORLD!</div>
    <div class="home-page__subtitle">I am a subtitle.</div>
    <div class="home-page__information">
      I am the information of your favorite page.
    </div>
  </div>
</template>

<style lang="scss">
  .home-page {
    @apply flex flex-col items-center justify-center;

    &__title {
      @apply text-5xl font-black mb-3;
    }
    &__subtitle {
      @apply text-2xl font-bold mb-2;
    }
    &__information {
      @apply text-lg;
    }
  }
</style>
