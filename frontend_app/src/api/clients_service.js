import Api from '@/api/Api'

export default {
  async getClients () {
    return await Api().get('/clients/')
  },
  async getClient (id) {
    return await Api().get(`/clients/${id}/`)
  },
  async setFavoriteService (id, f_s_id) {
    return await Api().put(`/client/${id}/`, {favorite_services_id: [f_s_id]})
  },
}