import { createRouter, createWebHistory } from "vue-router"
import HomePage from "~/pages/home-page.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "landing",
      component: HomePage,
    },
  ],
})

export default router
