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
  data () {
    return {
      vacancies: [
        {
          title: 'Vacancy test 1',
          company_name: 'Company test 1',
          category: 'IT test',
          created: '2022.03.12'
        },
        {
          title: 'Vacancy test 2',
          company_name: 'Company test 2',
          category: 'IT test',
          created: '2022.03.12'
        },
        {
          title: 'Vacancy test 3',
          company_name: 'Company test 3',
          category: 'IT test',
          created: '2022.03.12'
        },
        {
          title: 'Vacancy test 4',
          company_name: 'Company test 4',
          category: 'IT test',
          created: '2022.03.12'
        }
      ]
    }
  },
}
</script>

<style scoped>

</style>