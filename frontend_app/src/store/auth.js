import user_service from '@/api/user_service';

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
    await this.getMe(context);
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}