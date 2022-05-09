<template>
  <b-container>
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
        <b>Зарплата: </b> {{vacancy.salary_min}} - {{vacancy.salary_max}}
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
        <div class="text-default">{{vacancy.about}}</div>
      </b-col>
    </b-row>
    <b-row v-if="vacancy.duties">
      <b-col>
        <b class="text-underlined">Обязанности: </b> <div class="text-default">{{vacancy.duties}}</div>
      </b-col>
    </b-row>
    <b-row v-if="vacancy.requirements">
      <b-col>
        <b class="text-underlined">Требования: </b> <div class="text-default">{{vacancy.requirements}}</div>
      </b-col>
    </b-row>
    <b-row v-if="vacancy.conditions">
      <b-col>
        <b class="text-underlined">Условия: </b> <div class="text-default">{{vacancy.conditions}}</div>
      </b-col>
    </b-row>

    <hr>

    <b-row>
      <b-col>
        <b-button variant="outline-success" class="m-1">Откликнуться</b-button>
        <b-checkbox
          v-if="!this.$store.getters.user || !this.$store.getters.user.employer"
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
import vacancy_service from '@/api/vacancies_service'

export default {
  name: "VacancyDetails",
  props: ['vacancyId'],
  data() {
    return {
      vacancy: {},
      liked: Boolean,
    }
  },
  async mounted () {
    await this.$store.dispatch('getMe');
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
      this.$store.dispatch('setVacancyLike', {id: this.$store.getters.user.employee.id, f_v_id: this.vacancy.id})
    },
    setlike () {
      let f_v = this.$store.getters.user.favorites.vacancies;
      this.liked = f_v.includes(this.vacancy.id)
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