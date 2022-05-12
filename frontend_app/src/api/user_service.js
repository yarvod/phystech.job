import Api from './Api';

export default {
  async LogOut () {
    return await Api().post(`/auth/token/logout/`)
  },
  async LogIn (data) {
    return await Api().post('/auth/token/login/', data)
  },
  async getMe () {
    return await Api().get(`/auth/users/me/`)
  },
  async updateRole (data) {
    return await Api().put(`/auth/users/me/`, data)
  },
  async activate (data) {
    return await Api().post(`/auth/users/activation/`, data)
  },
  async createUser (data) {
    return await Api().post(`/auth/users/`, data)
  },
  async checkEmail (data) {
    return await Api().post(`/check_email/`, data)
  }
}