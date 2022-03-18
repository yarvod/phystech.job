import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      component: () => import('@/views/Home.vue')
    },
    {
      path: '/resumes',
      component: () => import('@/views/Resumes.vue')
    },
    {
      path: '/vacancies',
      component: () => import('@/views/Vacancies.vue')
    },
    {
      path: '/account',
      component: () => import('@/views/PersonalAccount.vue')
    }
  ]
})
