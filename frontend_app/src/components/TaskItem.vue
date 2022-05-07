<template>
    <b-card
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
      img-src="https://placekitten.com/500/350"
      img-alt="Image"
      img-top
      :title=task.title
    >
      <b-card-text>
        <b>Category: </b>
        {{task.category}}
        <br>
      </b-card-text>

      <hr>

      <b-button variant="outline-primary" class="m-1"
        v-if="edit"
        @click="$router.push({name: 'task_edit', params: {taskId: task.id}})"
      >
        Редактировать
      </b-button>
      <div v-else>
        <b-button variant="outline-primary" class="m-1"
                @click="$router.push({name: 'task_details', params: {taskId: task.id}})">
          Подробнее
        </b-button>

        <b-checkbox
          v-if="this.$store.getters.user && this.$store.getters.user.freelancer"
          v-model="liked"
          @change="onlike"
        >
          like
        </b-checkbox>
      </div>
      
      <template #footer>
        <small class="text-muted">
          <div v-if="task.is_published">
            <b>Опубликовано: </b>
            {{task.published|formatDate}}
          </div>
          <div v-else>
            <b>Не опубликовано</b>
          </div>
        </small>
      </template>

    </b-card>

</template>

<script>

export default {
  name: "TaskItem",
  props: ['task', 'edit'],
  data () {
    return {
      liked: Boolean
    }
  },
  methods: {
    onlike () {
      this.$store.dispatch('setTaskLike', {id: this.$store.getters.user.freelancer.id, f_t_id: this.task.id})
    },
    setlike () {
      let f_s = this.$store.getters.user.favorites.tasks;
      this.liked = f_s.includes(this.task.id)
    }
  },
  mounted () {
    if (this.$store.getters.user && !this.edit && !this.$store.getters.user.freelancer) {
      this.setlike()
    }
  }





}
</script>

<!--        <input id="heart" v-model="liked" type="checkbox"/>-->
<!--        <label for="heart">❤</label>-->

<style scoped>
body {
  display: flex;
  justify-content: center;
  margin: 0;
  height: 10vh;
}


[id="heart"] {
  position: absolute;
  left: -100vw;
}

[for="heart"] {
  color: #aab8c2;
  cursor: pointer;
  font-size: 1.5em;
  align-self: center;
  transition: color 0.2s ease-in-out;
}

[for="heart"]:hover {
  color: grey;
}

[for="heart"]::selection {
  color: gray;
  background: transparent;
}

[for="heart"]::moz-selection {
  color: gray;
  background: transparent;
}

[id="heart"]:checked + label {
  color: #e2264d;
  will-change: font-size;
  animation: heart 1s cubic-bezier(.17, .89, .32, 1.49);
}



@keyframes heart {0%, 10% {font-size: 0;}}
</style>