<template>

  <div class="container">
    <div class="row">
      <div class="col">
        <h2 v-if="isResumeEdit">Редактирование резюме</h2>
        <h2 v-else>Добавление резюме</h2>
      </div>
    </div>
    <router-link to="/account">Назад</router-link>

    <hr>

    <div class="row">
      <div class="col">

        <b-form @submit="onSubmit">
          <b-form-group id="title-group" label="Название:" label-for="title">
            <b-form-input
              id="title"
              :value="resume.title"
              v-model="resume.title"
              placeholder="Введите название"
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="education-group" label="Образование:" label-for="education">
            <b-form-textarea
              id="education"
              :value="resume.education"
              v-model="resume.education"
              placeholder="Расскажите о своем образовании"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="work-experiance-group" label="Опыт работы:" label-for="work_experience">
            <b-form-textarea
              id="work-experience"
              :value="resume.work_experiance"
              v-model="resume.work_experiance"
              placeholder="Расскажите об опыте работы"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="skills-group" label="Навыки:" label-for="skills">
            <b-form-textarea
              id="skills"
              :value="resume.skills"
              v-model="resume.skills"
              placeholder="Расскажите о своих навыках"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="about-me-group" label="Дополнительная информация о Вас:" label-for="about_me">
            <b-form-textarea
              id="about_me"
              :value="resume.about_me"
              v-model="resume.about_me"
              placeholder="Расскажите о себе (хобби, увлечения ...)"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group>
            <b-form-checkbox
                v-model="resume.ready_relocate"
                value="true"
                unchecked-value="false"
            >
              Готов к переезду
            </b-form-checkbox>
            <b-form-checkbox
                v-model="resume.ready_distant_work"
                value="true"
                unchecked-value="false"
            >
              Удаленная работа
            </b-form-checkbox>
          </b-form-group>

          <hr>

          <div class="row">
            <div class="col-auto">
               <b-button type="submit" variant="outline-primary" @click="onSubmit">Сохранить</b-button>
            </div>
            <div class="col-auto">
              <b-form-checkbox
                  v-model="resume.is_published"
                  value="true"
                  unchecked-value="false"
              >
                Опубликовать
              </b-form-checkbox>
            </div>
            <div v-if="isResumeEdit" class="col-auto offset-7 text-right">
              <b-button variant="outline-danger" @click="onDelete()">Удалить</b-button>
            </div>
          </div>


        </b-form>

      </div>
    </div>

  </div>

</template>

<script>
import tags_service from "@/api/tags_service";
import resumes_service from "@/api/resumes_service";
import router from "@/router";
export default {
  name: "Resume",
  props: [
    'isResumeEdit',
  ],
  data() {
    return {
      resume: {
        title: '',
        about_me: '',
        is_published: false,
        ready_relocate: false,
        ready_distant_work: false,
        work_experiance: ''
      },
      tags: {},
      user: {}
    }
  },
  async mounted () {
    await tags_service.getTags()
      .then(response => {this.tags = response.data})
    await this.$store.dispatch('getMe')
      .then(this.user = this.$store.getters.user)
    if (this.$route.params.resumeId) {
      let {data} = await resumes_service.getResume(this.$route.params.resumeId);
      this.resume = data
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      console.log('edit ', this.isResumeEdit)
      if (this.isResumeEdit) {
        this.resume.category = 'it'
        this.resume.employee = this.user.employee.id
        this.resume.tags = ['python']
        console.log('resume ', this.resume)
        this.$store.dispatch('updateResume', {resume: this.resume})
      } else {
        this.resume.category = 'it'
        this.resume.employee = this.user.employee.id
        this.resume.tags = ['python']
        this.$store.dispatch('createResume', {resume: this.resume})
        this.onReset()
      }
      router.push({name: 'account'})
    },
    onReset() {
      event.preventDefault()
      // Reset our form values
      this.resume = {}
    },
    onDelete() {

    }
  }
}
</script>

<style scoped>

</style>