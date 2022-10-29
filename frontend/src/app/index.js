import { createApp } from "vue"
import { router } from "~/router"
import App from "~/app/App.vue"

import "~/assets/scss/index.scss"

const app = createApp(App)

app.use(router)

app.mount("#app")

export { app }
