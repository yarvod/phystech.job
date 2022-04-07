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

        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
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

          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>

      </div>
    </div>

  </div>

</template>

<script>
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
      show: true
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      alert(JSON.stringify(this.form))
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values

      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style scoped>

</style>