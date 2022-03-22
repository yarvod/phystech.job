<template>
<div class="container">
  <div class="row h2 text-center">Resume Details</div>
  <div class="row">
    <router-link to="/resumes">К списку резюме</router-link>
  </div>
  <hr>
  <div class="row">
    <div class="col">
      <b>Title: </b>
      {{ resume.title }}
      <br>
      <b>Category: </b>
      {{resume.category}}
      <br>
      <b>Created: </b>
      {{resume.created}}
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "ResumeDetails",
  props: ['resume', 'id']
}
</script>

<style scoped>

</style>