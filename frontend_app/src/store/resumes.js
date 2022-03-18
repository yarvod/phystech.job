import resumes from '@/api/resumes'

const ADD_RESUME = 'ADD_RESUME'
const REMOVE_RESUME = 'REMOVE_RESUME'
const SET_RESUME = 'SET_RESUME'

const state = {
  resumes: []
}

const getters = {
  resumes: state => state.resumes  // список резюме из состояния
}


// Мутации
const mutations = {
  // Добавляем резюме в список
  [ADD_RESUME] (state, resume) {
    state.resumes = [resume, ...state.resumes]
  },
  // Убираем резюме из списка
  [REMOVE_RESUME] (state, { id }) {
    state.resumes = state.resumes.filter(resume => {
      return resume.id !== id
    })
  },
  // Задаем список резюме
  [SET_RESUME] (state, { resumes }) {
    state.resumes = resumes
  }
}


// Действия
const actions = {
  getResumes ({ commit }) {
    resumes.list().then(resumes => {
      commit(SET_RESUME, { resumes })
    })
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}