import vacancies_service from '@/api/vacancies_service'

const ADD_VACANCY = 'ADD_VACANCY'
const REMOVE_VACANCY = 'REMOVE_VACANCY'
const SET_VACANCIES = 'SET_VACANCIES'

const state = {
  vacancies: [],
}

const getters = {
  vacancies: state => state.vacancies,  // список вакансий из состояния
}


// Мутации
const mutations = {
  // Добавляем вакансию в список
  [ADD_VACANCY] (state, vacancy) {
    state.vacancies = [vacancy, ...state.vacancies]
  },
  // Убираем вакансию из списка
  [REMOVE_VACANCY] (state, { id }) {
    state.vacancies = state.vacancies.filter(vacancy => {
      return vacancy.id !== id
    })
  },
  // Задаем список вакансйи
  [SET_VACANCIES] (state, payload) {
    state.vacancies = payload
  },
}


// Действия
const actions = {
  getVacancies: async (context) => {
    let {data} = await vacancies_service.getVacancies();
    context.commit(SET_VACANCIES, data)
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}