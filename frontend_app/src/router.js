import Home from '@/views/Home';
import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/posts',
    component: () => import('@/views/Posts.vue')
  },
  {
    path: '/account',
    component: () => import('@/views/PersonalAccount.vue')
  }
]


const router = createRouter({
  history: createWebHistory(),
  routes,
});
  
export default router;