import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      component: () => import('@/views/Home.vue'),
      name: 'home'
    },
    {
      path: '/resumes',
      component: () => import('@/views/Resumes.vue')
    },
    {
      path: '/resumes/:resumeId/details',
      component: () => import('@/views/ResumeDetails.vue'),
      props: true,
      name: 'resume_details'
    },
    {
      path: '/vacancies',
      component: () => import('@/views/Vacancies.vue')
    },
    {
      path: '/vacancies/:vacancyId/details',
      component: () => import('@/views/VacancyDetails.vue'),
      props: true,
      name: 'vacancy_details'
    },
    {
      path: '/account',
      component: () => import('@/views/PersonalAccount.vue')
    }
  ]
})
