<template>
  <div>
    <b-modal v-model="show_modal" title="Форма соискателя" hide-backdrop content-class="shadow" centered hide-footer>
      <div v-if="!user.employer">
        <p>
        Вы сможете размещать свои резюме и откликаться на вакансии!
        </p>
        <b-form @submit.prevent="submitForm">
          <b-button variant="outline-success" type="submit">Стать соискателем!</b-button>
        </b-form>
      </div>

      <div v-else>
        <p>Вы работодатель и не можете добавлять резюме смотреть чужие вакансии :(</p>
        <b-button @click="show_modal = false" variant="outline-danger">Закрыть</b-button>
      </div>

    </b-modal>
  </div>
</template>

<script>
import employees_service from "@/api/employees_service";
import { mapGetters } from "vuex";

export default {
  name: "AddEmployeeModal",
  props: [
    'show_modal_add_employee',
  ],
  data () {
    return {
      form: {
      }
    }
  },
  computed: {
    ...mapGetters(['user']),
    show_modal: {
      get: function() {
        return this.show_modal_add_employee
      },
      set: function(newValue) {
        this.$emit('modal_state', newValue)
        return newValue
      }
    }
  },
  methods: {
    async submitForm () {
      await employees_service.createEmployee({
        user: this.$store.getters.user.id
      }).then(
          await this.$store.dispatch('getMe'),
          this.show_modal = false
        )
    }
  }
}
</script>

<style scoped>

</style>