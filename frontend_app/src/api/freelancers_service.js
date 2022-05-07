import Api from '@/api/Api'

export default {
  async getFreelancers () {
    return await Api().get('/freelancers/')
  },
  async getFreelancer (id) {
    return await Api().get(`/freelancers/${id}/`)
  },
  async setFavoriteTask (id, f_t_id) {
    return await Api().put(`/freelancers/${id}/`, {favorite_tasks_id: [f_t_id]})
  },
}