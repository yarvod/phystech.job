import vacancies from './vacancies'
import resumes from './resumes'
import Vue from 'vue'
import Vuex from "vuex";

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    vacancies,
    resumes,
  },
})
