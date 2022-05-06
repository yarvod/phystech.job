<template>
  <b-container>
    <b-row>
      <h2 class="text-center">Список резюме</h2>
    </b-row>
    <b-row>
      <b-link @click="$router.back()">Назад</b-link>
    </b-row>
    <hr>

    <ResumeList
      :resumes="resumes"
    />

  </b-container>
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