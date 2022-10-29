import { createRouter, createWebHistory } from "vue-router"

import DefaultLayout from "~/layouts/DefaultLayout.vue"
import ErrorLayout from "~/layouts/ErrorLayout.vue"

import HomePage from "~/pages/HomePage.vue"
import ErrorPage from "~/pages/ErrorPage.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage,
      meta: {
        layout: {
          name: DefaultLayout,
        },
      },
    },
    {
      path: "/:pathMatch(.*)*",
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
