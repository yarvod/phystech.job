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
  components: {ResumeItem},
  data () {
    return {
      resumes: [
        {
          title: 'Resume test 1',
          category: 'IT test',
          created: '2022.03.12'
        },
        {
          title: 'Resume test 2',
          category: 'IT test',
          created: '2022.03.12'
        },
        {
          title: 'Resume test 3',
          category: 'IT test',
          created: '2022.03.12'
        },
        {
          title: 'Resume test 4',
          category: 'IT test',
          created: '2022.03.12'
        }
      ]
    }
  },
}
</script>

<style scoped>

</style>