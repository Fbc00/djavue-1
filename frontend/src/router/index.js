import { createRouter, createWebHistory } from "vue-router"

import ErrorLayout from "~/layouts/ErrorLayout.vue"

import LandingPage from "~/pages/LandingPage.vue"
import ErrorPage from "~/pages/ErrorPage.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "landing",
      component: LandingPage,
    },
    {
      path: "/:pathMatch(.*)*",
      name: "not-found",
      component: ErrorPage,
      meta: {
        layout: {
          name: ErrorLayout,
        },
      },
    },
  ],
})

export default router
