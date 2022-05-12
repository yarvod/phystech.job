<template>
  <div class="container">
    <div class="row">
      <h2 class="text-center">Список вакансий</h2>
    </div>
    <div class="row">
      <b-link @click="$router.back()">Назад</b-link>
    </div>
    <hr>
    <VacancyList
      :vacancies="vacancies"
    />

  </div>
</template>


<script>
import VacancyList from "@/components/VacancyList";
import { mapGetters } from "vuex";

export default {
  name: 'Vacancies',
  computed: mapGetters(['vacancies']),
  async mounted () {
    await this.$store.dispatch('getVacancies')
  },
  components: {
		VacancyList,
  },
  data () {
    return {

    }
  }
}
</script>