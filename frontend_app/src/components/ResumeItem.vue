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
<!--        <input id="toggle-heart" type="checkbox"/>-->
<!--        <label for="toggle-heart" aria-label="like">❤</label>-->
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
  name: "ResumeItem",
  props: ['resume']
}
</script>

<style scoped>

</style>