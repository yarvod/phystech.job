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
    return await Api().post('/resume/', resume)
  },
  async updateResume (resume) {
    return await Api().patch(`/resume/${resume.id}/`, resume)
  },
  async getResumeDetail(id) {
    return await Api().get(`/resume/${id}/`)
  },
}