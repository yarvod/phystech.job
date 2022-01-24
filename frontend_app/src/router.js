import Home from '@/views/Home';
import { createWebHistory, createRouter } from "vue-router";

const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/todos',
        component: () => import('@/views/Todos.vue')
    }
]


const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  export default router;