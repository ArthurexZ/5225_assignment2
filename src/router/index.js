import Vue from 'vue'
import Router from 'vue-router'
import Register from '@/components/register/register.vue'
import Home from '@/components/home/home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
  ]
})
