import Api from '@/api/Api'

export default {
  async getEmployers () {
    return await Api().get('/employers/')
  },
  async getEmployer (id) {
    return await Api().get(`/employers/${id}/`)
  },
  async createEmployer (data) {
    return await Api().post(`/employer/`, data)
  },
  async setFavoriteResume (id, f_r_id) {
    return await Api().put(`/employer/${id}/`, {favorite_resumes_id: [f_r_id]})
  },
}