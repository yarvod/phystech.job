import Api from '@/api/Api'

export default {
  async getCategories () {
    return await Api().get('/categories/')
  }
}