import services_service from '@/api/services_service'

const ADD_SERVICE = 'ADD_SERVICE'
const REMOVE_SERVICE = 'REMOVE_SERVICE'
const SET_SERVICES = 'SET_SERVICES'

const state = {
  services: []
}

const getters = {
  services: state => state.services  // список сервисов из состояния
}


// Мутации
const mutations = {
  // Добавляем сервис в список
  [ADD_SERVICE] (state, payload) {
    state.services = [payload, ...state.services]
  },
  // Убираем сервис из списка
  [REMOVE_SERVICE] (state, payload) {
    state.services = state.services.filter(service => {
      return service.id !== payload
    })
  },
  // Задаем список сервисов
  [SET_SERVICES] (state, payload) {
    state.services = payload
  }
}


// Действия
const actions = {
  getServices: async (context) => {
    let {data} = await services_service.getServices();
    context.commit(SET_SERVICES, data)
  },
  createService: async (context, payload) => {
    await services_service.createService(payload.service)
      .then(
        context.dispatch('getServices')
      )
  },
  updateService: async (context, payload) => {
    await services_service.updateService(payload.service)
      .then(
        context.dispatch('getServices')
      )
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}