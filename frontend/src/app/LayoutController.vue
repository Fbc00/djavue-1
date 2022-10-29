<template>
  <component
    :is="layout"
    v-bind="route?.meta?.layout">
    <slot />
  </component>
</template>

<script setup>
  import { computed } from "vue"
  import { useRoute } from "vue-router"

  const DefaultLayout = "WhiteEmptyLayout"
  const route = useRoute()
  const layout = computed(() => route?.meta?.layout?.name || DefaultLayout)
</script>
