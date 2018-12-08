import Vue from 'vue'
import App from './App.vue'
import router from './router'
import echarts from 'echarts'
import $ from 'jquery'
import axios from 'axios'

import './plugins/element.js'
// import 'element-theme-chalk';
import './assets/css/index.css'
import { VueSpinners } from '@saeris/vue-spinners'

axios.defaults.baseURL = 'https://easy-mock.com/mock/5c09164ee1c4a705638a80bf/ke'

Vue.config.productionTip = false
Vue.prototype.$echarts = echarts 
Vue.prototype.$ = $
Vue.use(VueSpinners)
Vue.prototype.$axios = axios

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
