<template>
  <div class="col-auto">
    <div class="border rounded shadow-sm">

      <div class="btn" v-on:click="$router.push('/vacancies/'+vacancy.id)">
        <b>Title: </b>
        {{ vacancy.title }}
        <br>
        <b>Company: </b>

        <button href="/" style="background: none; border: none">
           {{vacancy.company_name}}
        </button>

        <br>
        <b>Category: </b>
        {{vacancy.category}}
        <br>
        <b>Created: </b>
        {{vacancy.created | formatDate}}
      </div>
    <hr>
    <input type="submit" class="btn btn-outline-success" name="respond" value="Откликнуться">
    <input type="submit" class="btn btn-outline-danger" name="like" value="В избранное">
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