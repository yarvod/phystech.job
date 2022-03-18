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
import { mapGetters } from 'vuex'
export default {
  name: "ResumeList",
  components: {ResumeItem},
  computed: mapGetters(['resumes']),
  beforeMount () {
    this.$store.dispatch('getResumes')
  },
}
</script>

<style scoped>

</style>