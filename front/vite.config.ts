import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import UnoCSS from 'unocss/vite'
import { presetWind, presetIcons } from 'unocss'

export default defineConfig({
  plugins: [
    vue(),
    UnoCSS({ presets: [presetWind(), presetIcons()] }),
  ],
  resolve: {
    alias: {
      '@': '/src',
    },
  },
})