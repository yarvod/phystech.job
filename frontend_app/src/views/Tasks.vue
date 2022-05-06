<template>
  <b-container>
    <b-row>
      <h2 class="text-center">Список Задач</h2>
    </b-row>
    <b-row>
      <b-link @click="$router.back()">Назад</b-link>
    </b-row>
    <hr>

    <TaskList
      :tasks="tasks"
    />

  </b-container>
</template>


<script>
import TaskList from '@/components/TaskList'
import { mapGetters } from "vuex";
export default {
  name: 'Tasks',
  computed: {
    ...mapGetters([
      'tasks'
    ])
  },
  async mounted() {
    await this.$store.dispatch('getTasks')
  },
  components: {
		TaskList,
  },
  data () {
    return {

    }
  }
}
</script>