<template>
  <div class="col-3">
    <div class="border rounded shadow-sm">
      <b>Title: </b>
      {{ resume.title }}
      <br>
      <b>Category: </b>
      {{resume.category}}
      <br>
      <b>Created: </b>
      {{resume.created | formatDate}}
      <hr>
      <input type="submit" class="btn btn-outline-success" name="respond" value="Связаться">
      <input type="submit" class="btn btn-outline-danger" name="like" value="В избранное">
    </div>
  </div>
</template>

<script>
export default {
  name: "ResumeItem",
  props: {
    resume: Object,
  },

}
</script>

<style scoped>

</style>