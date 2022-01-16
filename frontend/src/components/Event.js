// import Vue from 'vue'
// export const EventBus = new Vue()

import { createApp } from 'vue'
import App from '../App.vue'
import mitt from 'mitt';
const emitter = mitt();
const app = createApp(App);
app.config.globalProperties.emitter = emitter;