import { createApp } from 'vue'
import App from './App.vue'
import { router } from './router'
import 'uno.css'

import Vuesax from 'vuesax-alpha'
import 'vuesax-alpha/dist/index.css'

createApp(App).use(router).use(Vuesax).mount('#app')
