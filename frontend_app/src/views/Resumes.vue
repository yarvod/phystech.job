<template>
  <div class="container">
    <div class="row">
      <h2 class="text-center">Список резюме</h2>
    </div>
    <div class="row">
      <router-link to="/">Home</router-link>
    </div>
    <hr>
  <!--  <div class="text-center" v-if="loading">-->
  <!--    <Loader/>-->
  <!--  </div>-->
    <ResumeList/>
  <!--  <p v-else>No Resumes!</p>-->
  </div>
</template>


<script>
import ResumeList from '@/components/ResumeList'
// import Loader from '@/components/Loader'

export default {
  name: 'Resumes',
	data() {
		return {
      loading: true,
		}
	},
  components: {
		ResumeList,
    // Loader
  },
}
</script>