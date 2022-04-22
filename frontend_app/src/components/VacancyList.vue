<template>

  <b-card-group deck>
    <VacancyItem
        v-for="vacancy of vacancies"
        :key="vacancy.id"
        :vacancy="vacancy"
        :edit="false"
    />
  </b-card-group>

</template>

<script>
import VacancyItem from "@/components/VacancyItem";

export default {
  name: "VacancyList",
  components: {VacancyItem},
  props: ['vacancies'],
}
</script>

<style scoped>

</style>