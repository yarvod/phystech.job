import Api from '@/api/Api'

export default {
  async getCurrencies () {
    return await Api().get('/currencies/')
  }
}