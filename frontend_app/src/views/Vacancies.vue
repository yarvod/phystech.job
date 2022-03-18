<template>
  <div class="container">
    <div class="row">
      <h2 class="text-center">Список вакансий</h2>
    </div>
    <div class="row">
      <router-link to="/">Home</router-link>
    </div>
    <hr>
  <!--  <div class="text-center" v-if="loading">-->
  <!--    <Loader/>-->
  <!--  </div>-->
    <VacancyList/>
  <!--  <p v-else>No Resumes!</p>-->
  </div>
</template>


<script>
// import Loader from '@/components/Loader'
import VacancyList from "@/components/VacancyList";

export default {
  name: 'Vacancies',
	data() {
		return {
      loading: true,
		}
	},
  components: {
		VacancyList,
    // Loader
  },
}
</script>