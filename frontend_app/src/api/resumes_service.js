import Api from '@/api/Api'

export default {
  async getResumes () {
    return await Api().get('/resumes/')
  },
  async getResume (id) {
    return await Api().get(`/resumes/${id}/`)
  },
  async deleteResume (id) {
    return await Api().delete(`/resumes/${id}/`)
  },
  async createResume (resume) {
    return await Api().post('/resumes/', resume)
  },
}