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

Vue.prototype.baseWeb = 'http://0.0.0.0:5001'
Vue.prototype.baseSimple = 'http://0.0.0.0:5000'

Vue.config.productionTip = false
Vue.prototype.$echarts = echarts 
Vue.prototype.$ = $
Vue.use(VueSpinners)
Vue.prototype.$axios = axios

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
