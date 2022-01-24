<template>
    <div>
        <h2>To Do List</h2>
        <router-link to="/">Home</router-link>
        <hr>
        <AddTodo 
            v-on:add-todo="addTodo"
        />
        <select v-model="filter">
            <option value="all">All</option>
            <option value="completed">Completed</option>
            <option value="not-completed">Not completed</option>
        </select>
        <hr>
        <br>
        <Loader v-if="loading" />
        <ToDoList
            v-else-if="filteredTodos.length" 
            v-bind:todos="filteredTodos"
            v-on:remove-todo="removeTodo"
        />
        <p v-else>No todos!</p>
    </div>
</template>


<script>
import ToDoList from '@/components/ToDoList'
import AddTodo from '@/components/AddTodo'
import Loader from '@/components/Loader'

export default {
  name: 'App',
	data() {
		return {
			todos: [],
            loading: true,
            filter: 'all'
		}
	},
	mounted() {
		fetch('https://jsonplaceholder.typicode.com/todos?_limit=5')
			.then(response => response.json())
			.then(json => {
                this.todos = json
                this.loading = false
            })

	},
	methods: {
		removeTodo(id) {
			this.todos = this.todos.filter(t => t.id !== id)
		},
		addTodo(newTodo) {
			this.todos.push(newTodo)
		} 
	},
  components: {
		ToDoList: ToDoList,
		AddTodo: AddTodo,
        Loader
  },
  computed: {
      filteredTodos() {
          if (this.filter === 'all') {
              return this.todos;
          }

          if (this.filter === 'completed') {
              return this.todos.filter(t => t.completed)
          }

          if (this.filter === 'not-completed') {
              return this.todos.filter(t => !t.completed)
          }
      }
  }
//   watch: {
//       filter(val) {
//           console.log(val)
//       }
//   }
}
</script>