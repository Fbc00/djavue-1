<template>
  <component
    :is="layout"
    v-bind="layout">
    <slot />
  </component>
</template>

<script setup>
  import { computed } from "vue"
  import { useRoute } from "vue-router"

  import DefaultLayout from "~/layouts/DefaultLayout.vue"

  const route = useRoute()
  const layout = computed(() => route?.meta?.layout?.name || DefaultLayout)
</script>
