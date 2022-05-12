<template>
  <b-container>
    <b-row>
      <h2 class="text-center">Список Услуг</h2>
    </b-row>
    <b-row>
      <b-link @click="$router.back()">Назад</b-link>
    </b-row>
    <hr>

    <ServiceList
      :services="services"
    />

  </b-container>
</template>


<script>
import ServiceList from '@/components/ServiceList'
import { mapGetters } from "vuex";
export default {
  name: 'Services',
  computed: {
    ...mapGetters([
      'services'
    ])
  },
  async mounted() {
    await this.$store.dispatch('getServices')
  },
  components: {
		ServiceList,
  },
  data () {
    return {

    }
  }
}
</script>