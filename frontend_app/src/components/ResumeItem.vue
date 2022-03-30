<template>
  <div class="col-auto mt-2 mb-2">
    <div class="border rounded shadow-sm m-2">
        <b>Title: </b>
        {{ resume.title }}
        <br>
        <b>Category: </b>
        {{resume.category}}
        <br>
        <b>Created: </b>
        {{resume.created | formatDate}}
      <hr>
      <b-button variant="outline-primary" class="m-1"
                v-if="$route.path.search('/account') !== -1">
        Редактировать
      </b-button>
      <div v-else>
        <b-button variant="outline-primary" class="m-1"
                @click="$router.push({name: 'resume_details', params: {resumeId: resume.id}})">
          Подробнее
        </b-button>
        <button class="btn btn-outline-danger m-1" size="md" name="like"> В избранное </button>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "ResumeItem",
  props: ['resume'],
}
</script>

<style scoped>

</style>