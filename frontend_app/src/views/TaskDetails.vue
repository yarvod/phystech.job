<template>
  <b-container>
    <b-row class="h2 text-center">Подробнее о задаче</b-row>
    <b-row>
      <b-link @click="$router.back()">Назад</b-link>
    </b-row>
    <hr>
    <b-row>
      <b-col>
        <h3>{{ task.title }}</h3>
        <br>
        <b>Адрес: </b> {{ task.location }}
        <br>
        <b>Категория: </b>{{task.category}}
        <br>
        <b>Зарплата: </b> {{task.salary}}
        <br>
        <b>Опубликовано: </b> {{task.published|formatDate}}
      </b-col>
    </b-row>

    <b-row v-if="task.tags">
      <b-col>
         <b>Тэги:</b>
        <b-link class="m-1" v-for="tag in task.tags" :key="tag">
          {{ tag }}
        </b-link>
      </b-col>
    </b-row>

    <b-row v-if="task.about">
      <b-col>
        <b class="text-underlined">О задаче:</b>
        <div class="text-default">{{task.about}}</div>
      </b-col>
    </b-row>

    <hr>

    <b-row>
      <b-col>
        <b-button variant="outline-success" class="m-1">Откликнуться</b-button>
        <b-checkbox
          v-if="this.$store.getters.user && this.$store.getters.user.client"
          v-model="liked"
          @change="onlike"
        >
          like
        </b-checkbox>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import tasks_service from "@/api/tasks_service";

export default {
  name: "TaskDetails",
  props: ['taskId'],
  data() {
    return {
      task: {},
      liked: Boolean,
    }
  },
  async mounted () {
    await this.$store.dispatch('getMe');
    await this.getTask();
  },
  methods : {
    getTask() {
      tasks_service.getTask(this.$route.params.taskId).
        then(response => {
          this.task = response.data;
          this.setlike();
      })
    },
    onlike () {
      this.$store.dispatch('setTaskLike', {id: this.$store.getters.user.client.id, f_t_id: this.task.id})
    },
    setlike () {
      let f_t = this.$store.getters.user.favorites.tasks;
      this.liked = f_t.includes(this.task.id)
    }
  },
}
</script>

<style scoped>
b {
  font-weight: bold;
  font-size: larger;
}
.default-text {
  font-weight: normal;
}
.text-underlined {
  text-decoration: underline;
}
</style>