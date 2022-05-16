import Api from '@/api/Api';

export default {
  async createResume2Vacancy (data) {
    return await Api().post(`/resumes2vacancies/`, data)
  },
  async updateResume2Vacancy (data) {
    return await Api().put(`/resumes2vacancies/${data.id}/`, data)
  },
  async deleteResume2Vacancy (id) {
    return await Api().delete(`/resumes2vacancies/${id}/`)
  },
  async getResume2Vacancy (id) {
    return await Api().get(`/resumes2vacancies/${id}/`)
  },
  async getResumes2Vacancies (params) {
    return await Api().get(`/resumes2vacancies/`, {params: params})
  }
}