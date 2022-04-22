<template>

  <b-card-group deck>
    <ResumeItem
      v-for="resume of resumes"
      :key="resume.id"
      :resume="resume"
      :edit="false"
    />
  </b-card-group>

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