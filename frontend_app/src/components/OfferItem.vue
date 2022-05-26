<template>
  <div>
    
    <b-card
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
      img-src="https://placekitten.com/380/200"
      img-alt="Image"
      img-top
      :title=offer.title
    >

      <template #header>
        Предложение
      </template>

      <b-card-text>
        <b>Компания: </b>
         {{offer.company_name}}
        <br>
        <b>Категория: </b>
        {{offer.category}}
        <br>
        <b-row v-if="offer.tags">
          <b-col>
            <b>Тэги:</b>
            <b-link class="m-1" v-for="tag in offer.tags" :key="tag">
              {{ tag }}
            </b-link>
          </b-col>
        </b-row>
        <b-row>
          <b-col v-if="offer.salary_min || offer.salary_max">
            <b v-if="offer.salary_min">от {{offer.salary_min}} </b>
            <b v-if="offer.salary_max">до {{offer.salary_max}} </b>
            <b v-if="offer.currency"> {{offer.currency}} </b> 
            <b v-if="offer.billing_period"> {{offer.billing_period}} </b>
          </b-col>
        </b-row>
      </b-card-text>

      <hr>

      <b-button variant="outline-primary" class="m-1"
        v-if="edit"
        @click="$router.push({name: 'offer_edit', params: {offerId: offer.id}})"
      >
        Редактировать
      </b-button>
      <div v-else>
        <b-button variant="outline-primary" class="m-1"
                @click="goOffer">
          Подробнее
        </b-button>

        <b-checkbox
          v-if="this.$store.getters.user && this.$store.getters.user.employee"
          v-model="liked"
          @change="onlike"
          :on-icon="'mdi-heart'"
          :off-icon="'mdi-home'"
        />
      </div>

      <template #footer>
        <small class="text-muted">
          <div v-if="offer.is_published">
            <b>Опубликовано: </b>
            {{offer.published|formatDate}}
          </div>
          <div v-else>
            <b>Не опубликовано</b>
          </div>
        </small>
      </template>

    </b-card>
  </div>

</template>

<script>
export default {
  name: "OfferItem",
  props: ['offer', 'edit'],
  data () {
    return {
      liked: Boolean
    }
  },
  mounted () {
    if (this.$store.getters.user && !this.edit && this.$store.getters.user.employee){
      this.setlike()
    }
  },
  methods: {
    onlike () {
      this.$store.dispatch('setOfferLike', {id: this.$store.getters.user.employee.id, f_o_id: this.offer.id})
    },
    setlike () {
      let f_o = this.$store.getters.user.favorites.offers;
      this.liked = f_o.includes(this.offer.id)
    },
    goOffer () {
      this.$router.push({name: 'offer_details', params: {offerId: this.offer.id}})
    }
  }
}
</script>

<style scoped>
</style>