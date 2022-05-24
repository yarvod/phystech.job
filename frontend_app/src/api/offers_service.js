import Api from '@/api/Api'

export default {
  async getOffers() {
    return await Api().get('/offers/')
  },
  async getOffer(id) {
    return await Api().get(`/offers/${id}/`)
  },
  async deleteOffer(id) {
    return await Api().delete(`/offers/${id}/`)
  },
  async createOffer(offer) {
    return await Api().post('/offer/', offer)
  },
  async updateOffer (offer) {
    return await Api().patch(`/offer/${offer.id}/`, offer)
  },
  async getOfferDetail(id) {
    return await Api().get(`/offer/${id}/`)
  },
}