<template>

  <div class="container">
    <div class="row">
      <ResumeItem
        v-for="resume of resumes"
        :key="resume.id"
        :resume="resume"
      />
    </div>
  </div>

</template>

<script>
import ResumeItem from "@/components/ResumeItem";

export default {
  name: "ResumeList",
  props: ['resumes'],
  components: {ResumeItem},
}
</script>

<style scoped>

</style>