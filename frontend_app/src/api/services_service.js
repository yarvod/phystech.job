import Api from '@/api/Api'

export default {
  async getServices () {
    return await Api().get('/services/')
  },
  async getService (id) {
    return await Api().get(`/services/${id}/`)
  },
  async deleteService (id) {
    return await Api().delete(`/services/${id}/`)
  },
  async createService (service) {
    return await Api().post('/service/', service)
  },
  async updateService (service) {
    return await Api().patch(`/service/${service.id}/`, service)
  },
}