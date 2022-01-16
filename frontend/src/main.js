import { createApp } from 'vue'
import App from './App.vue'
import GAuth from 'vue3-google-oauth2'
const app = createApp(App)

const gAuthOptions = { clientId: '123368583629-jqqc210j1sbhteum2b0q29c67ghfe9vl.apps.googleusercontent.com', scope: 'email', prompt: 'consent', fetch_basic_profile: false }
app.use(GAuth, gAuthOptions)

app.mount('#app')