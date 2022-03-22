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
export default {
  name: "VacancyDetail",
  props: ['vacancy', 'id']
}
</script>

<style scoped>

</style>