<template>
  <b-container>
    
    <b-row class="h2 text-center">Подробнее о  предложении</b-row>
    <b-row>
      <b-link @click="$router.back()">Назад</b-link>
    </b-row>
    <hr>
    <b-row>
      <b-col>
        <h3>{{ offer.title }}</h3>
        <br>
        <b>Адрес: </b> {{ offer.location }}
        <br>
        <b>Категория: </b>{{offer.category}}
        <br>
        <b>Работодатель: </b> {{offer.company_name}}
        <br>
        <span v-if="offer.salary_min || offer.salary_max">
          <b>Зарплата: </b>
          <span v-if="offer.salary_min">от {{offer.salary_min}} </span>
          <span v-if="offer.salary_max">до {{offer.salary_max}} </span>
          <span v-if="offer.currency"> {{offer.currency}} </span> 
          <span v-if="offer.billing_period"> {{offer.billing_period}} </span>
        </span>
        <br>
        <b>Опубликовано: </b> {{offer.published|formatDate}}
      </b-col>
    </b-row>

    <b-row v-if="offer.tags">
      <b-col>
         <b>Тэги:</b>
        <b-link class="m-1" v-for="tag in offer.tags" :key="tag">
          {{ tag }}
        </b-link>
      </b-col>
    </b-row>

    <b-row v-if="offer.about">
      <b-col>
        <b class="text-underlined">О вакансии:</b>
        <div class="text-default">{{offer.about}}</div>
      </b-col>
    </b-row>
    <b-row v-if="offer.duties">
      <b-col>
        <b class="text-underlined">Обязанности: </b> <div class="text-default">{{offer.duties}}</div>
      </b-col>
    </b-row>
    <b-row v-if="offer.requirements">
      <b-col>
        <b class="text-underlined">Требования: </b> <div class="text-default">{{offer.requirements}}</div>
      </b-col>
    </b-row>
    <b-row v-if="offer.conditions">
      <b-col>
        <b class="text-underlined">Условия: </b> <div class="text-default">{{offer.conditions}}</div>
      </b-col>
    </b-row>

    <hr>

    <b-row>
      <b-col>
        <b-checkbox
          v-if="this.user && this.user.employee && !this.user.employer"
          v-model="liked"
          @change="onlike"
        >
          like
        </b-checkbox>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import offer_service from '@/api/offers_service';
import {mapGetters} from "vuex";

export default {
  name: "OfferDetails",
  props: ['offerId'],
  data() {
    return {
      offer: {},
      liked: Boolean,
    }
  },
  computed: {
    ...mapGetters(['user'])
  },
  async mounted () {
    await this.getOffer();
  },
  methods : {
    getOffer() {
      offer_service.getOffer(this.$route.params.offerId).
        then(response => {
          this.offer = response.data;
          this.setlike();
      })
    },
    onlike () {
      this.$store.dispatch('setOfferLike', {id: this.user.employee.id, f_o_id: this.offer.id})
    },
    setlike () {
      let f_o = this.user.favorites.offers;
      this.liked = f_o.includes(this.offer.id)
    }
  },
}
</script>

<style scoped>
b {
  font-weight: bold;
  font-size: larger;
}
.default-text {
  font-weight: normal;
}
.text-underlined {
  text-decoration: underline;
}
</style>