import Vue from 'vue';
import Vuex from "vuex";
import vacancies from './vacancies';
import resumes from './resumes';
import services from "./services";
import tasks from "./tasks";
import auth from "./user";


Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    vacancies,
    resumes,
    services,
    tasks,
    auth,
  },
})
