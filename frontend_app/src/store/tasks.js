import tasks_service from '@/api/tasks_service'

const ADD_TASK = 'ADD_TASK'
const REMOVE_TASK = 'REMOVE_TASK'
const SET_TASKS = 'SET_TASKS'

const state = {
  tasks: []
}

const getters = {
  tasks: state => state.tasks  // список задач из состояния
}


// Мутации
const mutations = {
  // Добавляем задачу в список
  [ADD_TASK] (state, payload) {
    state.tasks = [payload, ...state.tasks]
  },
  // Убираем задачу из списка
  [REMOVE_TASK] (state, payload) {
    state.tasks = state.tasks.filter(service => {
      return service.id !== payload
    })
  },
  // Задаем список задач
  [SET_TASKS] (state, payload) {
    state.tasks = payload
  }
}


// Действия
const actions = {
  getTasks: async (context) => {
    let {data} = await tasks_service.getTasks();
    context.commit(SET_TASKS, data)
  },
  createTask: async (context, payload) => {
    await tasks_service.createTask(payload.task)
      .then(
        context.dispatch('getTasks')
      )
  },
  updateTask: async (context, payload) => {
    await tasks_service.updateTask(payload.task)
      .then(
        context.dispatch('getTasks')
      )
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}