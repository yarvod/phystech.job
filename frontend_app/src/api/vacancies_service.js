import Api from '@/api/Api'

export default {
  async getVacancies() {
    return await Api().get('/vacancies/')
  },
  async getVacancy(id) {
    return await Api().get(`/vacancies/${id}/`)
  },
  async deleteVacancy(id) {
    return await Api().delete(`/vacancies/${id}/`)
  },
  async createVacancy(vacancy) {
    return await Api().post('/vacancy/', vacancy)
  },
  async updateVacancy (vacancy) {
    return await Api().patch(`/vacancy/${vacancy.id}/`, vacancy)
  },
  async getVacancyDetail(id) {
    return await Api().get(`/vacancy/${id}/`)
  },
}