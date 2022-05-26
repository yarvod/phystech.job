import Vue from 'vue'
import VueRouter from 'vue-router'
import {store} from './store'


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
      path: '/login/:tabIndex',
      component: () => import('@/views/Login.vue'),
      name: 'login',
      props: true
    },
    // {
    //   path: '/tasks',
    //   component: () => import('@/views/Tasks.vue'),
    //   name: 'tasks'
    // },
    // {
    //   path: '/tasks/:taskId/details',
    //   component: () => import('@/views/TaskDetails.vue'),
    //   props: true,
    //   name: 'task_details',
    //   meta: {
    //     requiresAuth: true
    //   }
    // },
    // {
    //   path: '/account/tasks/:taskId/edit',
    //   component: () => import('@/views/Task.vue'),
    //   props: {isTaskEdit:true},
    //   name: 'task_edit',
    //   meta: {
    //     requiresAuth: true
    //   }
    // },
    // {
    //   path: '/account/task/add',
    //   component: () => import('@/views/Task.vue'),
    //   props: {isTaskEdit:false},
    //   name: 'task_add',
    //   meta: {
    //     requiresAuth: true
    //   }
    // },
    // {
    //   path: '/services',
    //   component: () => import('@/views/Services.vue'),
    //   name: 'services'
    // },
    // {
    //   path: '/services/:serviceId/details',
    //   component: () => import('@/views/ServiceDetails.vue'),
    //   props: true,
    //   name: 'service_details',
    //   meta: {
    //     requiresAuth: true
    //   }
    // },
    // {
    //   path: '/account/services/:serviceId/edit',
    //   component: () => import('@/views/Service.vue'),
    //   props: {isServiceEdit:true},
    //   name: 'service_edit',
    //   meta: {
    //     requiresAuth: true
    //   }
    // },
    // {
    //   path: '/account/service/add',
    //   component: () => import('@/views/Service.vue'),
    //   props: {isServiceEdit:false},
    //   name: 'service_add',
    //   meta: {
    //     requiresAuth: true
    //   }
    // },
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
        requiresAuth: true,
        requiresEmployer: true
      },
      query: true
    },
    {
      path: '/account/resumes/:resumeId/edit',
      component: () => import('@/views/Resume.vue'),
      props: {
        isResumeEdit: true
      },
      name: 'resume_edit',
      meta: {
        requiresAuth: true,
        requiresOwner: true
      }
    },
    {
      path: '/account/resume/add',
      component: () => import('@/views/Resume.vue'),
      props: {isResumeEdit:false},
      name: 'resume_add',
      meta: {
        requiresAuth: true,
        requiresEmployee: true
      }
    },
    {
      path: '/account/vacancies/:vacancyId/edit',
      component: () => import('@/views/Vacancy'),
      props: {isVacancyEdit:true},
      name: 'vacancy_edit',
      meta: {
        requiresAuth: true,
        requiresOwner: true
      }
    },
    {
      path: '/account/vacancy/add',
      component: () => import('@/views/Vacancy'),
      props: {isVacancyEdit:false},
      name: 'vacancy_add',
      meta: {
        requiresAuth: true,
        requiresEmployer: true
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
        requiresAuth: true,
        requiresEmployee: true
      }
    },
    {
      path: '/offers/:offerId/details',
      component: () => import('@/views/OfferDetails.vue'),
      props: true,
      name: 'offer_details',
      meta: {
        requiresAuth: true,
        requiresEmployee: true
      }
    },
    {
      path: '/account/:tabIndex',
      component: () => import('@/views/Account.vue'),
      name: 'account',
      meta: {
        requiresAuth: true
      },
      props: true
    },
    {
      path: '/auth/users/activate/:uid/:token',
      component: () => import('@/views/Activate'),
      name: 'user_activate'
    }
  ],
})


router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (!localStorage.getItem('token')) {
      router.push({name: 'login', params: {tabIndex: 0}})
     }
    else if (to.meta.requiresEmployee) {
      if (!store.getters.user.employee) {
        router.replace({name: from.name, query: {show_modal_add_employee: true}})
      }
      else {
        next()
      }
    }
    else {
      next()
    }
  }
  else {
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