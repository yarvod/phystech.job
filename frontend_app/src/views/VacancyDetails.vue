<template>
  <b-container>
    
    <ResponseVacancyModal
      :show_modal_response_vacancy="show_modal_response_vacancy"
      :vacancy_id="vacancyId"
      :user="user"
      @modal_state="show_modal_response_vacancy = $event"
    />
    
    <b-row class="h2 text-center">Подробнее о вакансии</b-row>
    <b-row>
      <b-link @click="$router.back()">Назад</b-link>
    </b-row>
    <hr>
    <b-row>
      <b-col>
        <h3>{{ vacancy.title }}</h3>
        <br>
        <b>Адрес: </b> {{ vacancy.location }}
        <br>
        <b>Категория: </b>{{vacancy.category}}
        <br>
        <b>Работодатель: </b> {{vacancy.company_name}}
        <br>
        <span v-if="vacancy.salary_min || vacancy.salary_max">
          <b>Зарплата: </b>
          <span v-if="vacancy.salary_min">от {{vacancy.salary_min}} </span>
          <span v-if="vacancy.salary_max">до {{vacancy.salary_max}} </span>
          <span v-if="vacancy.currency"> {{vacancy.currency}} </span> 
          <span v-if="vacancy.billing_period"> {{vacancy.billing_period}} </span>
        </span>
        <br>
        <b>Опубликовано: </b> {{vacancy.published|formatDate}}
      </b-col>
    </b-row>

    <b-row v-if="vacancy.tags">
      <b-col>
         <b>Тэги:</b>
        <b-link class="m-1" v-for="tag in vacancy.tags" :key="tag">
          {{ tag }}
        </b-link>
      </b-col>
    </b-row>

    <b-row v-if="vacancy.about">
      <b-col>
        <b class="text-underlined">О вакансии:</b>
        <p class="linebreaks">{{vacancy.about}}</p>
      </b-col>
    </b-row>
    <b-row v-if="vacancy.duties">
      <b-col>
        <b class="text-underlined">Обязанности: </b> <p class="linebreaks">{{vacancy.duties}}</p>
      </b-col>
    </b-row>
    <b-row v-if="vacancy.requirements">
      <b-col>
        <b class="text-underlined">Требования: </b> <p class="linebreaks">{{vacancy.requirements}}</p>
      </b-col>
    </b-row>
    <b-row v-if="vacancy.conditions">
      <b-col>
        <b class="text-underlined">Условия: </b> <p class="linebreaks">{{vacancy.conditions}}</p>
      </b-col>
    </b-row>

    <hr>

    <b-row>
      <b-col>
        <b-button @click="response" variant="outline-success" class="m-1">Откликнуться</b-button>
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
import vacancy_service from '@/api/vacancies_service';
import ResponseVacancyModal from "@/components/ResponseVacancyModal";
import {mapGetters} from "vuex";

export default {
  name: "VacancyDetails",
  props: ['vacancyId'],
  components: {
    ResponseVacancyModal,
  },
  data() {
    return {
      vacancy: {},
      liked: Boolean,
      show_modal_response_vacancy: false,
    }
  },
  computed: {
    ...mapGetters(['user'])
  },
  async mounted () {
    await this.getVacancy();
  },
  methods : {
    getVacancy() {
      vacancy_service.getVacancy(this.$route.params.vacancyId).
        then(response => {
          this.vacancy = response.data;
          this.setlike();
      })
    },
    onlike () {
      this.$store.dispatch('setVacancyLike', {id: this.user.employee.id, f_v_id: this.vacancy.id})
    },
    setlike () {
      let f_v = this.user.favorites.vacancies;
      this.liked = f_v.includes(this.vacancy.id)
    },
    response () {
      this.show_modal_response_vacancy = !this.show_modal_response_vacancy
    }
  },
}
</script>

<style scoped>
b {
  font-weight: bold;
  font-size: larger;
}
.text-underlined {
  text-decoration: underline;
}
</style>