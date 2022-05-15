<template>
  <div>
    <b-modal v-model="show_modal" title="Форма работодателя" hide-backdrop content-class="shadow" centered hide-footer>
      <b-form @submit.prevent="submitForm">

        <b-form-group
          id="input-company-name"
          label="Название организации:"
          label-for="input-company-name"
        >
          <b-form-input
            id="input-company-name"
            v-model="form.company_name"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-company-website"
          label="Сайт организации:"
          label-for="input-company-website"
        >
          <b-form-input
            id="input-company-website"
            v-model="form.company_website"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="text-about" label="О компании:" label-for="about">
          <b-form-textarea
            id="about"
            v-model="form.about"
            required
          >
          </b-form-textarea>
        </b-form-group>

        <br>

        <b-button variant="outline-success" type="submit">Стать работодателем!</b-button>

      </b-form>

    </b-modal>
  </div>
</template>

<script>
import employers_service from "@/api/employers_service";

export default {
  name: "AddEmployerModal",
  props: [
    'show_modal_add_employer',
    'user'
  ],
  data () {
    return {
      form: {
        company_name: '',
        company_website: '',
        about: ''
      }
    }
  },
  computed: {
    show_modal: {
      get: function() {
        return this.show_modal_add_employer
      },
      set: function(newValue) {
        this.$emit('modal_state', newValue)
        return newValue
      }
    }
  },
  methods: {
    async submitForm () {
      await employers_service.createEmployer({
        user: this.user.id,
        company_name: this.form.company_name,
        company_website: this.form.company_website,
        about: this.form.about
      }).then(
          await this.$store.dispatch('getMe')
        ).then(
          this.$emit('user_update', this.$store.getters.user)
      )
      this.show_modal = false
    }
  }
}
</script>

<style scoped>

</style>