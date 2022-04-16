<template>
  <div class="container">
    <div class="row">
      <h2 class="text-center">Список резюме</h2>
    </div>
    <div class="row">
      <router-link to="/">Home</router-link>
    </div>
    <hr>

    <ResumeList
      :resumes="resumes"
    />

  </div>
</template>


<script>
import ResumeList from '@/components/ResumeList'
import { mapGetters } from "vuex";
export default {
  name: 'Resumes',
  computed: {
    ...mapGetters([
      'resumes'
    ])
  },
  async mounted() {
    await this.$store.dispatch('getResumes')
  },
  components: {
		ResumeList,
  },
  data () {
    return {

    }
  }
}
</script>