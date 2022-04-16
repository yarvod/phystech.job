<template>
  <div class="container">
    <div class="row h2 text-center">Vacancy Details</div>
    <div class="row">
      <router-link to="/vacancies">К списку вакансий</router-link>
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
        <b-button variant="outline-danger" class="m-1">В избранное</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import vacancy_service from '@/api/vacancies_service'

export default {
  name: "VacancyDetails",
  props: ['vacancyId'],
  data() {
    return {
      vacancy :{}
    }
  },
  async mounted () {
    await this.getVacancy()
  },
  methods : {
    getVacancy() {
      vacancy_service.getVacancy(this.$route.params.vacancyId).
        then(response => {
          this.vacancy = response.data
      })
    }
  }
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