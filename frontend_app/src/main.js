import Vue from 'vue';
import App from './App.vue';
import router from './router';
import {store} from './store'
import moment from 'moment'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('MM/DD/YYYY hh:mm')
  }
})
