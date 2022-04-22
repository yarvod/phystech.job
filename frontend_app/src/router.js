import Vue from 'vue'
import VueRouter from 'vue-router'
import {store} from "@/store/index";


Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    {
      path: '/',
      component: () => import('@/views/Home.vue'),
      name: 'home'
    },
    {
      path: '/resumes',
      component: () => import('@/views/Resumes.vue'),
      name: 'resumes'
    },
    {
      path: '/resumes/:resumeId/details',
      component: () => import('@/views/ResumeDetails.vue'),
      props: true,
      name: 'resume_details'
    },
    {
      path: '/account/resumes/:resumeId/edit',
      component: () => import('@/views/Resume.vue'),
      props: {isResumeEdit:true},
      name: 'resume_edit',
      // meta: {
      //   requiresAuth: true
      // }
    },
    {
      path: '/account/resume/add',
      component: () => import('@/views/Resume.vue'),
      props: {isResumeEdit:false},
      name: 'resume_add',
      // meta: {
      //   requiresAuth: true
      // }
    },
    {
      path: '/account/vacancies/:vacancyId/edit',
      component: () => import('@/views/Vacancy'),
      props: {isVacancyEdit:true},
      name: 'vacancy_edit',
      // meta: {
      //   requiresAuth: true
      // }
    },
    {
      path: '/account/vacancy/add',
      component: () => import('@/views/Vacancy'),
      props: {isVacancyEdit:false},
      name: 'vacancy_add',
      // meta: {
      //   requiresAuth: true
      // }
    },
    {
      path: '/vacancies',
      component: () => import('@/views/Vacancies.vue'),
      name: 'vacancies'
    },
    {
      path: '/vacancies/:vacancyId/details',
      component: () => import('@/views/VacancyDetails.vue'),
      props: true,
      name: 'vacancy_details'
    },
    {
      path: '/account',
      component: () => import('@/views/Account.vue'),
      name: 'account',
      // meta: {
      //   requiresAuth: true
      // }
    }
  ],
})


// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     // this route requires auth, check if logged in
//     // if not, redirect to login page.
//     if (!store.getters.user) {
//       next({ name: 'home' , params: {show_login: true}})
//     } else {
//       next() // go to wherever I'm going
//     }
//   } else {
//     next() // does not require auth, make sure to always call next()!
//   }
// })

export default router;