<template>
  <b-container>
    <b-row>
      <h2 class="text-center">Список резюме</h2>
    </b-row>
    <b-row>
      <b-link @click="$router.back()">Назад</b-link>
    </b-row>
    <hr>

    <b-row>
      <b-col 
        cols="md-4" 
        class="mb-4"
        v-for="resume of resumes"
        :key="resume.id"
      >
        <ResumeItem
          :resume="resume"
          :edit="false"
        />
      </b-col>
      
    </b-row>

  </b-container>
</template>


<script>
import ResumeItem from '@/components/ResumeItem'
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
		ResumeItem
  },
  data () {
    return {

    }
  }
}
</script>