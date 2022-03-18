<template>

  <div class="container">
    <div class="row">
      <VacancyItem
        v-for="vacancy of vacancies"
        :key="vacancy.id"
        :vacancy="vacancy"
      />
    </div>
  </div>

</template>

<script>
import VacancyItem from "@/components/VacancyItem";
import { mapGetters } from 'vuex'
export default {
  name: "VacancyList",
  components: {VacancyItem},
  computed: mapGetters(['vacancies']),
  mounted () {
    this.$store.dispatch('getVacancies')
  },
}
</script>

<style scoped>

</style>