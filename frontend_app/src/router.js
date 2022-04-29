import Vue from 'vue'
import VueRouter from 'vue-router'
import {store} from "@/store/index";


Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    {
      path: '/',
      component: () => import('@/views/Home.vue'),
      name: 'home',
      props: true
    },
    {
      path: '/login',
      component: () => import('@/views/Login.vue'),
      name: 'login',
      props: true
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
      name: 'resume_details',
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/account/resumes/:resumeId/edit',
      component: () => import('@/views/Resume.vue'),
      props: {isResumeEdit:true},
      name: 'resume_edit',
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/account/resume/add',
      component: () => import('@/views/Resume.vue'),
      props: {isResumeEdit:false},
      name: 'resume_add',
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/account/vacancies/:vacancyId/edit',
      component: () => import('@/views/Vacancy'),
      props: {isVacancyEdit:true},
      name: 'vacancy_edit',
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/account/vacancy/add',
      component: () => import('@/views/Vacancy'),
      props: {isVacancyEdit:false},
      name: 'vacancy_add',
      meta: {
        requiresAuth: true
      }
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
      name: 'vacancy_details',
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/account',
      component: () => import('@/views/Account.vue'),
      name: 'account',
      meta: {
        requiresAuth: true
      }
    }
  ],
})


router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (!localStorage.getItem('token')) {
      router.push({name: 'login'})
     } else {
      next()
    }
  } else {
    next()
  }
})

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location, onComplete, onAbort) {
    const result = originalPush.call(
        this,
        location,
        onComplete,
        onAbort
    );
    if (result) {
        return result.catch(err => {
            if (err.name !== 'NavigationDuplicated') {
                throw err;
            }
        });
    }
    return result;
};


export default router;