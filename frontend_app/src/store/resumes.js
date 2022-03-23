import resumes_service from '@/api/resumes_service'

const ADD_RESUME = 'ADD_RESUME'
const REMOVE_RESUME = 'REMOVE_RESUME'
const SET_RESUMES = 'SET_RESUMES'

const state = {
  resumes: []
}

const getters = {
  resumes: state => state.resumes  // список резюме из состояния
}


// Мутации
const mutations = {
  // Добавляем резюме в список
  [ADD_RESUME] (state, payload) {
    state.resumes = [payload, ...state.resumes]
  },
  // Убираем резюме из списка
  [REMOVE_RESUME] (state, payload) {
    state.resumes = state.resumes.filter(resume => {
      return resume.id !== payload
    })
  },
  // Задаем список резюме
  [SET_RESUMES] (state, payload) {
    state.resumes = payload
  }
}


// Действия
const actions = {
  getResumes: async (context) => {
    let {data} = await resumes_service.getResumes();
    context.commit(SET_RESUMES, data)
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}