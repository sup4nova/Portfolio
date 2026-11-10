import { createApp } from 'vue'
import App from './App.vue'
import { router } from './router'
import 'uno.css'
import './assets/styles/sup4nova-tokens.css'
import './assets/styles/sup4nova-ui.css'
import './assets/styles/base.css'

createApp(App).use(router).mount('#app')
