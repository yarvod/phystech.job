<template>
  <div>
    <b-modal v-model="show_modal" title="Отклик на вакансию" hide-backdrop content-class="shadow" centered hide-footer>
      <b-form @submit.prevent="submitForm">
        
        <b-button @click="$router.push({name: 'resume_add'})" variant="outline-success">Добавить резюме</b-button>
        <br>
        <b-form-group label="Выберете резюме для отклика:">
          <b-container>
            <b-row
              v-for="resume of user.employee.resumes"
              :key="resume.id"
              class="border rounded m-2"
            >
              <b-col class="m-2">
                <b-form-radio
                  v-model="selected_resume_id"
                  :value="resume.id"
                >
                  <b>{{ resume.title }}</b>. Категория: {{resume.category}}
                </b-form-radio>
              </b-col>
            </b-row>
            
          </b-container>
          
        </b-form-group>
        
        <b-form-group id="input-message" label="Сообщение работодателю:" label-for="message">
          <b-form-textarea
            class="mt-1"
            id="message"
            v-model="message"
            placeholder="Короткое сообщение работодателю"
          >
          </b-form-textarea>
        </b-form-group>

        <b-button variant="outline-success" type="submit">Откликнуться!</b-button>

      </b-form>

    </b-modal>
  </div>
</template>

<script>
import r2v_service from "@/api/r2v_service";

export default {
  name: "ResponseVacancyModal",
  props: [
    'show_modal_response_vacancy',
    'user',
    'vacancy_id',
  ],
  data () {
    return {
      selected_resume_id: null,
      message: '',
    }
  },
  computed: {
    show_modal: {
      get: function() {
        return this.show_modal_response_vacancy
      },
      set: function(newValue) {
        this.$emit('modal_state', newValue)
        return newValue
      }
    }
  },
  methods: {
    async submitForm () {
      await r2v_service.createResume2Vacancy({
        from_resume: this.selected_resume_id,
        to_vacancy: this.vacancy_id,
        employee_message: this.message
      }).then(
        await this.$store.dispatch('getMe')
      )
      this.show_modal = false
    }
  }
}
</script>

<style scoped>

</style>