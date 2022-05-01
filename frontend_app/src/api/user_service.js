import Api from './Api';

export default {
  async getUser (id) {
    return await Api().get(`/users/${id}/`)
  },
  async LogOut () {
    return await Api().post(`/auth/token/logout/`)
  },
  async LogIn (data) {
    return await Api().post('/auth/token/login/', data)
  },
  async getMe () {
    return await Api().get(`/auth/users/me/`)
  },
  async activate (data) {
    return await Api().post(`/auth/users/activation/`, data)
  },
  async createUser (data) {
    return await Api().post(`/auth/users/`, data)
  }
}