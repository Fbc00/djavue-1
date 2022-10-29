<template>
  <div class="error-page">
    <div class="error-page__title">404</div>
    <div class="error-page__subtitle">
      The page that you are looking for doesn't exists.
    </div>
    <div class="error-page__information">Please go back to your home.</div>
  </div>
</template>

<style lang="scss">
  .error-page {
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
