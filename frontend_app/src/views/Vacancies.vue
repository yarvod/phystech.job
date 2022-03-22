<template>
  <div class="container">
    <div class="row">
      <h2 class="text-center">Список вакансий</h2>
    </div>
    <div class="row">
      <router-link to="/">На главную</router-link>
    </div>
    <hr>
    <VacancyList
      :vacancies="vacancies_json"
    />

  </div>
</template>


<script>
import VacancyList from "@/components/VacancyList";
import { mapGetters } from "vuex";
import json from '@/views/vacancies.json';
export default {
  name: 'Vacancies',
  computed: mapGetters(['vacancies']),
  mounted () {
    this.$store.dispatch('getVacancies')
  },
  components: {
		VacancyList,
  },
  data () {
    return {
      vacancies_json: json.data
    }
  }
}
</script>