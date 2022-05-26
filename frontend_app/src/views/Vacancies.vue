<template>
  <div class="container">

    <AddEmployeeModal
      :show_modal_add_employee="show_modal_add_employee"
      @modal_state="show_modal_add_employee = $event"
    />

    <div class="row">
      <h2 class="text-center">Список вакансий</h2>
    </div>
    <div class="row">
      <b-link @click="$router.back()">Назад</b-link>
    </div>
    <hr>
    <PostsWrapper
      :items="items"
    />

  </div>
</template>


<script>
import AddEmployeeModal from "@/components/AddEmployeeModal.vue";
import PostsWrapper from "@/components/PostsWrapper";
import { mapGetters } from "vuex";

export default {
  name: 'Vacancies',
  components: {
		PostsWrapper,
    AddEmployeeModal
  },
  data () {
    return {
      items: []
    }
  },
  computed: {
    ...mapGetters(['vacancies', 'offers']),
    show_modal_add_employee: {
      get () {
        return eval(this.$route.query.show_modal_add_employee)
      },
      set (v) {
        this.$router.replace({name: 'vacancies'})
      }
    }
  },
  async mounted () {
    await this.$store.dispatch('getVacancies');
    await this.$store.dispatch('getOffers');
    this.items = this.vacancies.concat(this.offers)
  },

}
</script>