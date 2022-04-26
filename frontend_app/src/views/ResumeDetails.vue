<template>
<div class="container">
  <div class="row h2 text-center">Resume Details</div>
  <div class="row">
    <a class="cancel-link" @click="$router.back()">Назад</a>
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
import resumes_service from '@/api/resumes_service';

export default {
  name: "ResumeDetails",
  data() {
    return {
      resume: {}
    }
  },
  async mounted() {
    await this.getResume()
  },
  methods: {
    getResume() {
      resumes_service.getResume(this.$route.params.resumeId).
        then(response => {
          this.resume = response.data
      })
    }
  }


}
</script>

<style scoped>

</style>