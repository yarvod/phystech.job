<template>
  <div>
    
    <AddEmployeeModal
      :show_modal_add_employee="show_modal_add_employee"
      @modal_state="show_modal_add_employee = $event"
    />
    
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
import AddEmployeeModal from "@/components/AddEmployeeModal";
export default {
  name: "OfferItem",
  props: ['offer', 'edit'],
  components: {
    AddEmployeeModal,
  },
  data () {
    return {
      liked: Boolean,
      show_modal_add_employee: false,
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
      if (!this.$store.getters.user) {
        this.$router.push({name: 'login'})
      }
      else if (this.$store.getters.user.employee) {
        this.$router.push({name: 'offer_details', params: {offerId: this.offer.id}})
      }
      else if (!this.$store.getters.user.employer) {
        this.show_modal_add_employee = ! this.show_modal_add_employee
      }
    }
  }
}
</script>

<style scoped>
</style>