import Vue from 'vue'
import VueRouter from 'vue-router'

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
      name: 'resume_edit'
    },
    {
      path: '/account/resume/add',
      component: () => import('@/views/Resume.vue'),
      props: {isResumeEdit:false},
      name: 'resume_add'
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
      name: 'account'
    }
  ],
})

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
//     next({ name: 'LogIn', query: { to: to.path } });
//   } else {
//     next()
//   }
// })

export default router;