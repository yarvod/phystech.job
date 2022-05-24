import Api from '@/api/Api'

export default {
  async getEmployees () {
    return await Api().get('/employees/')
  },
  async getEmployee (id) {
    return await Api().get(`/employees/${id}/`)
  },
  async createEmployee (data) {
    return await Api().post(`/employee/`, data)
  },
  async setFavoriteVacancy (id, f_v_id) {
    return await Api().put(`/employee/${id}/`, {favorite_vacancies_id: [f_v_id]})
  },
  async setFavoriteOffer (id, f_o_id) {
    return await Api().put(`/employee/${id}/`, {favorite_offers_id: [f_o_id]})
  },
}