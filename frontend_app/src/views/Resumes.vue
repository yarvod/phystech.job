<template>
  <b-container>

    <AddEmployerModal
      :show_modal_add_employer="show_modal_add_employer"
      @modal_state="show_modal_add_employer = $event"
    />

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
import ResumeItem from '@/components/ResumeItem';
import AddEmployerModal from '@/components/AddEmployerModal.vue';
import { mapGetters } from "vuex";
export default {
  name: 'Resumes',
  computed: {
    ...mapGetters([
      'resumes'
    ]),
    show_modal_add_employer: {
      get () {
        return eval(this.$route.query.show_modal_add_employer)
      },
      set (v) {
        this.$router.replace({name: 'resumes'})
      }
    }
  },
  async mounted() {
    await this.$store.dispatch('getResumes')
  },
  components: {
		ResumeItem,
    AddEmployerModal
  },
  data () {
    return {

    }
  }
}
</script>