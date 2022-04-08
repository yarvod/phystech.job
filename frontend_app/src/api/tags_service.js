import Api from '@/api/Api'

export default {
  async getTags () {
    return await Api().get('/tags/')
  },
  async getTag (id) {
    return await Api().get(`/tags/${id}/`)
  },
  async createTag (resume) {
    return await Api().post('/tags/', resume)
  },
}