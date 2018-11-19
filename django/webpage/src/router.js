import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import(/* webpackChunkName: "about" */ './views/Index.vue')
    },
    {
      path: '/page',
      name: 'page',
      component: () => import(/* webpackChunkName: "about" */ './views/Page.vue'),
      children: [
        {
          path: 'answer',
          name: 'answer',
          component: () => import(/* webpackChunkName: "about" */ './views/Answer.vue')
        },
        {
          path: 'graph',
          name: 'graph',
          component: () => import(/* webpackChunkName: "about" */ './views/Graph.vue')
        },
        {
          path: 'search',
          name: 'search',
          component: () => import(/* webpackChunkName: "about" */ './views/Search.vue')
        },
        {
          path: 'question',
          name: 'question',
          component: () => import(/* webpackChunkName: "about" */ './views/Question.vue')
        }
      ]
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
