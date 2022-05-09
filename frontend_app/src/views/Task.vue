<template>

  <b-container>
    <b-row>
      <b-col>
        <h2 v-if="isTaskEdit">Редактирование задачи</h2>
        <h2 v-else>Добавление задачи</h2>
      </b-col>
    </b-row>
    <b-link @click="$router.back()">Назад</b-link>

    <hr>

    <b-row>
      <b-col>

        <b-form @submit="onSubmit">
          <b-form-group id="title-group" label="Название:" label-for="title">
            <b-form-input
              id="title"
              :value="task.title"
              v-model="task.title"
              placeholder="Введите название"
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="about-group" label="Информация о задаче:" label-for="about">
            <b-form-textarea
              id="about"
              :value="task.about"
              v-model="task.about"
              placeholder="Расскажите о задаче"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="location-group" label="Локация:" label-for="location">
            <b-form-input
              id="location"
              type="text"
              :value="task.location"
              v-model="task.location"
              placeholder="Укажите место"
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group label="Оплата:" label-for="salary">
            <b-form-input
                id="salary"
                type="number"
                step="1000"
                min="0"
                v-model="task.salary"
            ></b-form-input>
          </b-form-group>

          <TagMultiSelect
              :options="tags"
              :value="task.tags"
              v-model="task.tags"
          />

          <hr>

          <b-row>
            <b-col cols="auto">
               <b-button type="submit" variant="outline-primary" @click="onSubmit">Сохранить</b-button>
            </b-col>
            <b-col cols="auto">
              <b-form-checkbox
                  v-model="task.is_published"
                  value="true"
                  unchecked-value="false"
              >
                Опубликовать
              </b-form-checkbox>
            </b-col>
            <b-col v-if="isTaskEdit" class="offset-7 text-right">
              <b-button variant="outline-danger" @click="onDelete()">Удалить</b-button>
            </b-col>
          </b-row>


        </b-form>

      </b-col>
    </b-row>

  </b-container>



</template>

<script>
import tags_service from "@/api/tags_service";
import router from "@/router";
import tasks_service from "@/api/tasks_service";
import TagMultiSelect from "@/components/TagMultiSelect";
export default {
  name: "Task",
  props: [
    'isTaskEdit',
  ],
  components: {
    TagMultiSelect
  },
  data() {
    return {
      task: {
        title: '',
        about: '',
        salary: null,
        location: '',
        category: null,
        tags: [],
        is_published: false
      },
      tags: [],
      tag_search: '',
      user: {}
    }
  },
  async mounted () {
    let raw_tags = [];
    await tags_service.getTags()
      .then(response => {raw_tags = response.data})
    for (var key in raw_tags) {
      this.tags.push(raw_tags[key].title)
    }
    await this.$store.dispatch('getMe')
      .then(this.user = this.$store.getters.user)
    if (this.$route.params.taskId) {
      if (this.isTaskEdit) {
        this.task = this.user.client.tasks.find(task => task.id === this.$route.params.taskId)
      }
      else {
        let {data} = await tasks_service.getTask(this.$route.params.taskId);
        this.task = data;
      }
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      if (this.isTaskEdit) {
        this.task.category = 'it'
        this.task.client = this.user.client.id
        this.$store.dispatch('updateTask', {task: this.task})
      } else {
        this.task.category = 'it'
        this.task.client = this.user.client.id
        this.$store.dispatch('createTask', {task: this.task})
        this.onReset()
      }
      router.push({name: 'account'})  // FIXME: redirect to previous page
    },
    onReset() {
      event.preventDefault()
      // Reset our form values
      this.task = {}
    },
    onDelete() {

    }
  }
}
</script>

<style scoped>

</style>