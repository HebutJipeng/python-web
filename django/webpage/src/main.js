import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
// import 'element-theme-chalk';
import './assets/css/index.css'
import { VueSpinners } from '@saeris/vue-spinners'

Vue.config.productionTip = false
Vue.use(VueSpinners)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
