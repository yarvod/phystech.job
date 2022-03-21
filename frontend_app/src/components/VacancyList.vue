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

export default {
  name: "VacancyList",
  components: {VacancyItem},
  props: ['vacancies']
}
</script>

<style scoped>

</style>