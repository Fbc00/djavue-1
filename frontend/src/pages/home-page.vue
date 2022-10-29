<template lang="pug">
.home-page
  .home-page__title HELLO WORLD!
  .home-page__subtitle I am a subtitle.
  .home-page__information I am the information of your favorite page.
</template>

<style lang="scss">
.home-page {
  @apply mt-16 flex flex-col items-center justify-center;

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
