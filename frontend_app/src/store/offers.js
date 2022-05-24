import offers_service from '@/api/offers_service'

const ADD_OFFER = 'ADD_OFFER'
const REMOVE_OFFER = 'REMOVE_OFFER'
const SET_OFFERS = 'SET_OFFERS'

const state = {
  offers: [],
}

const getters = {
  offers: state => state.offers,  // список offers из состояния
}


// Мутации
const mutations = {
  // Добавляем offer в список
  [ADD_OFFER] (state, offer) {
    state.offers = [offer, ...state.offers]
  },
  // Убираем offer из списка
  [REMOVE_OFFER] (state, { id }) {
    state.offers = state.offers.filter(offer => {
      return offer.id !== id
    })
  },
  // Задаем список offers
  [SET_OFFERS] (state, payload) {
    state.offers = payload
  },
}


// Действия
const actions = {
  getOffers: async (context) => {
    let {data} = await offers_service.getOffers();
    context.commit(SET_OFFERS, data)
  },
  createOffer: async (context, payload) => {
    await offers_service.createOffer(payload.offer)
      .then(
        context.dispatch('getOffers')
      )
  },
  updateOffer: async (context, payload) => {
    await offers_service.updateOffer(payload.offer)
      .then(
        context.dispatch('getOffers')
      )
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}