<template>
  <div class="col-auto mt-2 mb-2">
    <div class="border rounded shadow-sm">
      <div class="btn" v-on:click="$router.push({name: 'resume_details', params: {resumeId: resume.id, resume: resume}})">
        <b>Title: </b>
        {{ resume.title }}
        <br>
        <b>Category: </b>
        {{resume.category}}
        <br>
        <b>Created: </b>
        {{resume.created}}
      </div>
      <hr>
      <button class="btn btn-outline-success m-1" size="md" name="connect"> Связатся </button>
      <button class="btn btn-outline-danger m-1" size="md" name="like"> В избранное </button>
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