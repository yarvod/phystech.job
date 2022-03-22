<template>
  <div class="col-auto mt-2 mb-2">
    <div class="border rounded shadow-sm m-2">

      <div class="btn" v-on:click="$router.push({name: 'vacancy_details', params: {vacancyId: vacancy.id, vacancy: vacancy}})">
        <b>Title: </b>
        {{ vacancy.title }}
        <br>
        <b>Company: </b>
         {{vacancy.company_name}}
        <br>
        <b>Category: </b>
        {{vacancy.category}}
        <br>
        <b>Created: </b>
        {{vacancy.created}}
      </div>
      <hr>
      <button class="btn btn-outline-success m-1" size="md" name="respond"> Откликнуться </button>
      <button class="btn btn-outline-danger m-1" size="md" name="like"> В избранное </button>

    </div>
  </div>

</template>

<script>
export default {
  name: "VacancyItem",
  props: {
    vacancy: Object,
  },

}
</script>

<style scoped>

</style>