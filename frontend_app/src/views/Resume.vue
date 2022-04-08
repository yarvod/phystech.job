<template>

  <div class="container">
    <div class="row">
      <div class="col">
        <h2>Добавление резюме</h2>
      </div>
    </div>
    <hr>

    <div class="row">
      <div class="col">

        <b-form @submit="onSubmit">
          <b-form-group id="title-group" label="Название:" label-for="title">
            <b-form-input
              id="title"
              v-model="resume.title"
              placeholder="Введите название"
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="education-group" label="Образование:" label-for="education">
            <b-form-textarea
              id="education"
              v-model="resume.education"
              placeholder="Расскажите о своем образовании"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="work-experiance-group" label="Опыт работы:" label-for="work_experience">
            <b-form-textarea
              id="work-experience"
              v-model="resume.work_experience"
              placeholder="Расскажите об опыте работы"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="skills-group" label="Навыки:" label-for="skills">
            <b-form-textarea
              id="skills"
              v-model="resume.skills"
              placeholder="Расскажите о своих навыках"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="about-me-group" label="Дополнительная информация о Вас:" label-for="about_me">
            <b-form-textarea
              id="about_me"
              v-model="resume.about_me"
              placeholder="Расскажите о себе (хобби, увлечения ...)"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="check">
            <b-form-checkbox v-model="resume.ready_relocate">Готов к переезду</b-form-checkbox>
            <b-form-checkbox v-model="resume.ready_distant_work">Удаленная работа</b-form-checkbox>
          </b-form-group>

          <hr>


          <div class="row">
            <div class="col-auto">
               <b-button type="submit" variant="outline-primary">Сохранить</b-button>
            </div>
            <div class="col-auto">
              <b-form-checkbox type="checkbox" v-model="resume.is_published">Опубликовать</b-form-checkbox>
            </div>
          </div>


        </b-form>

      </div>
    </div>

  </div>

</template>

<script>
import tags_service from "@/api/tags_service";
export default {
  name: "Resume",
  props: {
    isResumeEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      resume: {},
      tags: {},
      user: {}
    }
  },
  async mounted () {
    await tags_service.getTags()
      .then(response => {this.tags = response.data})
    await this.$store.dispatch('getMe')
      .then(this.user = this.$store.getters.user)
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      if (this.isResumeEdit) {

      } else {
        this.resume.category = 'it'
        this.resume.employee = this.user.employee.id
        this.resume.tags = ['python']
        this.$store.dispatch('createResume', {resume: this.resume})
        this.onReset()
      }
    },
    onReset() {
      event.preventDefault()
      // Reset our form values
      this.resume = {}
    }
  }
}
</script>

<style scoped>

</style>