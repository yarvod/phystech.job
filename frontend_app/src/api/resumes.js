import Api from '@/api/Api'

export default {
  async getResumes () {
    return await Api().get('/resumes/')
  },
  list () {
    return Api().get('/resumes/').then(response => {
      return response.data
    })
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