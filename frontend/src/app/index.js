import { createApp } from "vue"
import App from "~/app/app.vue"
import router from "~/router"

import "~/assets/index.scss"

const app = createApp(App)

app.use(router)

app.mount("#app")

export { app }
