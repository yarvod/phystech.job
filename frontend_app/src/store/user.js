import user_service from '@/api/user_service';
import employees_service from "@/api/employees_service";
import employers_service from '../api/employers_service';
import clients_service from "@/api/clients_service";
import freelancers_service from "@/api/freelancers_service";

const state = {
  user: {},
  isAuthenticated: false,
  token: ''
}

const getters = {
  isAuthenticated: state => state.isAuthenticated,
  token: state => state.token,
  user: state => state.user.data
}

const mutations = {
  storeToken(state) {
    if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
    } else {
        state.token = ''
        state.isAuthenticated = false
    }
  },
  setToken (state, token) {
    state.token = token
    state.isAuthenticated = true
  },
  removeToken(state) {
    state.token = ''
    state.isAuthenticated = false;
  },
  setUser(state, user) {
    state.user = user
  }
}


const actions = {
  async LogOut (context) {
    await user_service.LogOut();
    context.commit('setUser', {});
    context.commit('removeToken');
  },
  async getMe (context) {
    let user = await user_service.getMe();
    context.commit('setUser', user);

  },
  async LogIn (context, data) {
    await user_service.LogIn(data);
    await context.getMe(context);
  },
  async setVacancyLike (context, payload) {
    await employees_service.setFavoriteVacancy(payload.id, payload.f_v_id)
    await this.dispatch('getMe')
  },
  async setResumeLike (context, payload) {
    await employers_service.setFavoriteResume(payload.id, payload.f_r_id)
    await this.dispatch('getMe')
  },
  async setServiceLike (context, payload) {
    await clients_service.setFavoriteService(payload.id, payload.f_s_id)
    await this.dispatch('getMe')
  },
  async setTaskLike (context, payload) {
    await freelancers_service.setFavoriteTask(payload.id, payload.f_t_id)
    await this.dispatch('getMe')
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}