import { createApp } from 'vue'
import App from './App.vue'

import "bootstrap/dist/css/bootstrap.min.css";
import { BootstrapIconsPlugin } from 'bootstrap-icons-vue';
// import "bootstrap"

import router from './router'
import store from './store'

import axios from 'axios'
axios.default.baseURI = 'http://localhost:8002'

createApp(App).use(store).use(router, axios).use(BootstrapIconsPlugin).mount('#app')
import 'bootstrap/dist/js/bootstrap.js';