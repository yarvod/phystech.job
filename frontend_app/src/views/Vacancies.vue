<template>
  <div class="container">
    <div class="row">
      <h2 class="text-center">Список вакансий</h2>
    </div>
    <div class="row">
      <b-link @click="$router.back()">Назад</b-link>
    </div>
    <hr>
    <PostsWrapper
      :items="items"
    />

  </div>
</template>


<script>
import PostsWrapper from "@/components/PostsWrapper";
import { mapGetters } from "vuex";

export default {
  name: 'Vacancies',
  components: {
		PostsWrapper,
  },
  data () {
    return {
      items: []
    }
  },
  computed: mapGetters(['vacancies', 'offers']),
  async mounted () {
    await this.$store.dispatch('getVacancies');
    await this.$store.dispatch('getOffers');
    this.items = this.vacancies.concat(this.offers)
  },

}
</script>