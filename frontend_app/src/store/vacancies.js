import vacancies from '@/api/vacancies'

const ADD_VACANCY = 'ADD_VACANCY'
const REMOVE_VACANCY = 'REMOVE_VACANCY'
const SET_VACANCY = 'SET_VACANCY'

const state = {
  vacancies: []
}

const getters = {
  vacancies: state => state.vacancies  // список вакансий из состояния
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
  [SET_VACANCY] (state, { vacancies }) {
    state.vacancies = vacancies
  }
}


// Действия
const actions = {
  getVacancies ({ commit }) {
    vacancies.list().then(vacancies => {
      commit(SET_VACANCY, { vacancies })
    })
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}