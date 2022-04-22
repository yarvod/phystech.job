<template>
  <div class="container">
    <div class="row h2 text-center">Vacancy Details</div>
    <div class="row">
      <a class="cancel-link" @click="$router.back()">Назад</a>
    </div>
    <hr>
    <div class="row">
      <div class="col">
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
      </div>
    </div>
    <div class="row" v-if="vacancy.about">
      <div class="col">
        <b class="text-underlined">О вакансии:</b>
        <div class="text-default">{{vacancy.about}}</div>
      </div>
    </div>
    <div class="row" v-if="vacancy.duties">
      <div class="col">
        <b class="text-underlined">Обязанности: </b> <div class="text-default">{{vacancy.duties}}</div>
      </div>
    </div>
    <div class="row" v-if="vacancy.requirements">
      <div class="col">
        <b class="text-underlined">Требования: </b> <div class="text-default">{{vacancy.requirements}}</div>
      </div>
    </div>
    <div class="row" v-if="vacancy.conditions">
      <div class="col">
        <b class="text-underlined">Условия: </b> <div class="text-default">{{vacancy.conditions}}</div>
      </div>
    </div>

    <hr>

    <div class="row">
      <div class="col">
        <b-button variant="outline-success" class="m-1">Откликнуться</b-button>
        <b-checkbox
          v-if="!this.$store.getters.user || !this.$store.getters.user.employer"
          v-model="liked"
          @change="onlike"
        >
          like
        </b-checkbox>
      </div>
    </div>
  </div>
</template>

<script>
import vacancy_service from '@/api/vacancies_service'
import employees_service from "@/api/employees_service";

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
      this.$store.dispatch('setLike', {id: this.$store.getters.user.employee.id, f_v_id: this.vacancy.id})
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