<template>
  <b-container>
    <b-row class="h2 text-center">Подробнее об услуге</b-row>
    <b-row>
      <b-link @click="$router.back()">Назад</b-link>
    </b-row>
    <hr>
    <b-row>
      <b-col>
        <h3>{{ service.title }}</h3>
        <br>
        <b>Адрес: </b> {{ service.location }}
        <br>
        <b>Категория: </b>{{service.category}}
        <br>
        <b>Стоимость: </b> {{service.salary}}
        <br>
        <b>Опубликовано: </b> {{service.published|formatDate}}
      </b-col>
    </b-row>

    <b-row v-if="service.tags">
      <b-col>
         <b>Тэги:</b>
        <b-link class="m-1" v-for="tag in service.tags" :key="tag">
          {{ tag }}
        </b-link>
      </b-col>
    </b-row>

    <b-row v-if="service.about">
      <b-col>
        <b class="text-underlined">Об услуге:</b>
        <div class="text-default">{{service.about}}</div>
      </b-col>
    </b-row>

    <hr>

    <b-row>
      <b-col>
        <b-button variant="outline-success" class="m-1">Откликнуться</b-button>
        <b-checkbox
          v-if="this.$store.getters.user && this.$store.getters.user.client"
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
import services_service from '@/api/services_service'

export default {
  name: "ServiceDetails",
  props: ['serviceId'],
  data() {
    return {
      service: {},
      liked: Boolean,
    }
  },
  async mounted () {
    await this.$store.dispatch('getMe');
    await this.getService();
  },
  methods : {
    getService() {
      services_service.getService(this.$route.params.serviceId).
        then(response => {
          this.service = response.data;
          this.setlike();
      })
    },
    onlike () {
      this.$store.dispatch('setServiceLike', {id: this.$store.getters.user.client.id, f_s_id: this.service.id})
    },
    setlike () {
      let f_s = this.$store.getters.user.favorites.services;
      this.liked = f_s.includes(this.service.id)
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