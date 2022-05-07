import Api from '@/api/Api'

export default {
  async getTasks () {
    return await Api().get('/tasks/')
  },
  async getTask (id) {
    return await Api().get(`/tasks/${id}/`)
  },
  async deleteTask (id) {
    return await Api().delete(`/tasks/${id}/`)
  },
  async createTask (task) {
    return await Api().post('/task/', task)
  },
  async updateTask (task) {
    return await Api().patch(`/task/${task.id}/`, task)
  },
}