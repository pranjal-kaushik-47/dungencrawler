import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  server: {
    host: "0.0.0.0",
    port: 5173,
    origin: "0.0.0.0:5173",
    hmr: {
      host: '0.0.0.0', // Use the host machine domain
      protocol: 'ws',  // Force WebSocket protocol
    }
  },
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
