<template>
  <div class="container">
    <div class="row h2 text-center">Vacancy Details</div>
    <div class="row">
      <router-link to="/vacancies">К списку вакансий</router-link>
    </div>
    <hr>
    <div class="row">
      <div class="col">
        <b>Title: </b>
        {{ vacancy.title }}
        <br>
        <b>Category: </b>
        {{vacancy.category}}
        <br>
        <b>Created: </b>
        {{vacancy.created}}
      </div>
    </div>
  </div>
</template>

<script>
import vacancy_service from '@/api/vacancies_service'

export default {
  name: "VacancyDetails",
  props: ['vacancyId'],
  data() {
    return {
      vacancy :{}
    }
  },
  async mounted () {
    await this.getVacancy()
  },
  methods : {
    getVacancy() {
      vacancy_service.getVacancy(this.$route.params.vacancyId).
        then(response => {
          this.vacancy = response.data
      })
    }
  }
}
</script>

<style scoped>

</style>