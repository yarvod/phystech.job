<template>
  <div class="col-auto mt-2 mb-2">
    <div class="border rounded shadow-sm m-2">
      <b>Title: </b>
      {{ vacancy.title }}
      <br>
      <b>Company: </b>
       {{vacancy.company_name}}
      <br>
      <b>Category: </b>
      {{vacancy.category}}
      <br>
      <div v-if="vacancy.is_published">
        <b>Опубликовано: </b>
        {{vacancy.published|formatDate}}
      </div>
      <div v-else>
        <b>Не опубликовано</b>
      </div>
      <hr>
      <b-button variant="outline-primary" class="m-1"
        v-if="$route.path.search('/account') !== -1"
        @click="$router.push({name: 'vacancy_edit', params: {vacancyId: vacancy.id}})"
      >
        Редактировать
      </b-button>
      <div v-else>
        <b-button variant="outline-primary" class="m-1"
                @click="$router.push({name: 'vacancy_details', params: {vacancyId: vacancy.id}})">
          Подробнее
        </b-button>
        <b-form-checkbox
          id="checkbox-1"
          v-model="like"
          name="checkbox-1"
        >
          like
        </b-form-checkbox>
      </div>

    </div>
  </div>

</template>

<script>
export default {
  name: "VacancyItem",
  props: ['vacancy'],
  data () {
    return {
      like: Boolean
    }
  }

}
</script>

<style scoped>

</style>