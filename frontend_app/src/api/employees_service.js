import Api from '@/api/Api'

export default {
  async getEmployees () {
    return await Api().get('/employees/')
  },
  async getEmployee (id) {
    return await Api().get(`/employees/${id}/`)
  },
  async updateEmployee (id, f_v_id) {
    return await Api().put(`/employees/${id}/`, {favorite_vacancies_id: [f_v_id]})
  },
}