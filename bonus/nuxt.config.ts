// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@nuxt/ui'],
  css: [
    // Inclure le fichier CSS de Bootstrap
    'bootstrap/dist/css/bootstrap.min.css'
  ],
  // Charger le JS de Bootstrap dans les plugins
  plugins: [
    { src: '~/plugins/bootstrap.js', mode: 'client' }
  ],
})