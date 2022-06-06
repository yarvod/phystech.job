<template>
  <b-container>
    <b-row>
      <h2>Редактирование профиля</h2>
    </b-row>
    <b-row>
      <b-link @click="$router.back()">Назад</b-link>
    </b-row>
    

    <b-row>
      <b-col>

        <b-form @submit.prevent="submit">

          <b-form-group id="input-fio" label="Имя, Фамилия:" label-for="input-name" label-size="lg">
            <b-form-checkbox
              id="input-name"
              v-model="form.show_name"
            >
              Показывать в 
              <span v-if="form.employee"> резюме </span>
              <span v-else-if="form.employer"> вакансиях </span>
            </b-form-checkbox>
            <br>
            <b-form-input
              id="input-name"
              v-model="form.first_name"
              placeholder="Имя"
              required
            ></b-form-input>
            <b-form-input
              class="mt-1"
              id="input-name"
              v-model="form.last_name"
              placeholder="Фамилия"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="group-socials" label="Социальные сети:" label-for="input-socials" label-size="lg">
            <b-form-checkbox
              id="input-socials"
              v-model="form.show_socials"
            >
              Показывать в 
              <span v-if="form.employee"> резюме </span>
              <span v-else-if="form.employer"> вакансиях </span>
            </b-form-checkbox>

            <br>

            <b-form-group id="input-socials" label="Почта:" label-for="input-email">
              <b-form-input
                id="input-email"
                v-model="form.email"
                :disabled="true"
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-socials" label="Телеграм:" label-for="input-telegram">
              <b-form-input
                id="input-telegram"
                v-model="form.telegram"
                placeholder="@username"
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-socials" label="Номер телефона:" label-for="input-phone">
              <b-form-input
                id="input-phone"
                type="tel"
                placeholder="Example: 89991231212"
                v-model="form.phone_number"
              ></b-form-input>
            </b-form-group>

          </b-form-group>

          <b-button type="submit" variant="primary">
            Сохранить
          </b-button>
        </b-form>

      </b-col>
    </b-row>
    
    

  </b-container>
</template>

<script>
import { mapGetters } from 'vuex';
import user_service from '../api/user_service';

export default {
  name: "AccountEdit",
  components: {
  },
  data () {
    return {
      form: {}
    }
  },
  computed: {
    ...mapGetters(['user'])
  },
  mounted() {
    this.form = {...this.user}
  },
  methods: {
    async submit () {
      await user_service.updateMe(this.form)
        .then(this.$store.dispatch('getMe'))
      this.$router.back()
    }
  }
}
</script>

<style scoped>

</style>