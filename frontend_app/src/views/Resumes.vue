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
      :resumes="resumes_json"
    />

  </div>
</template>


<script>
import ResumeList from '@/components/ResumeList'
import { mapGetters } from "vuex";
import json from '@/views/resumes.json'
export default {
  name: 'Resumes',
  computed: {
    ...mapGetters(['resumes'])
  },
  mounted() {
    this.$store.dispatch('getResumes')
  },
  components: {
		ResumeList,
  },
  data () {
    return {
      resumes_json: json.data
    }
  }
}
</script>