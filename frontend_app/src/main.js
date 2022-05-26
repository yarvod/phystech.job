import Vue from 'vue';
import App from './App.vue';
import router from './router';
import {store} from './store'
import moment from 'moment'
import axios from "axios";

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import { BootstrapVue, IconsPlugin, ModalPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common["Authorization"] = "Token " + token
}

Vue.config.productionTip = false

Vue.use(Vuetify)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(ModalPlugin)

new Vue({
  axios,
  store,
  router,
  render: h => h(App)
}).$mount('#app')

Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('MM/DD/YYYY hh:mm')
  }
})
