<template>
<b-container>
  <b-row class="h2 text-center">Подробнее о резюме</b-row>
  <b-row>
    <b-link @click="$router.back()">Назад</b-link>
  </b-row>
  <hr>
  <b-row>
    <b-col>
      <b>Название: </b>
      {{ resume.title }}
      <br>
      <b>Категоря: </b>
      {{resume.category}}
      <br>
      <span v-if="resume.salary_min || resume.salary_max">
        <b>Зарплата: </b>
        <span v-if="resume.salary_min">от {{resume.salary_min}} </span>
        <span v-if="resume.salary_max">до {{resume.salary_max}} </span>
        <span v-if="resume.currency"> {{resume.currency}} </span> 
        <span v-if="resume.billing_period"> {{resume.billing_period}} </span>
      </span>
      <br>
      <b>Опубликовано: </b>
      {{resume.published}}
    </b-col>
  </b-row>

  <b-row v-if="resume.tags">
      <b-col>
         <b>Тэги:</b>
        <b-link class="m-1" v-for="tag in resume.tags" :key="tag">
          {{ tag }}
        </b-link>
      </b-col>
    </b-row>

  <b-row v-if="resume.about_me">
    <b-col>
      <b class="text-underlined">Обо мне:</b>
      <p class="linebreaks"> {{resume.about_me}} </p>
    </b-col>
  </b-row>
  <b-row v-if="resume.education">
    <b-col>
      <b class="text-underlined">Образование:</b>
      <p class="linebreaks"> {{resume.education}} </p>
    </b-col>
  </b-row>
  <b-row v-if="resume.work_experiance">
    <b-col>
      <b class="text-underlined">Опыт работы:</b>
      <p class="linebreaks"> {{resume.work_experiance}} </p>
    </b-col>
  </b-row>
  <b-row v-if="resume.skills">
    <b-col>
      <b class="text-underlined">Навыки:</b>
      <p class="linebreaks"> {{resume.skills}} </p>
    </b-col>
  </b-row>

  <hr>

  <b-row>
      <b-col>
        <b-button variant="outline-success" class="m-1">Предложить работу</b-button>
        <b-checkbox
          v-if="!this.$store.getters.user || !this.$store.getters.user.employee"
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
import resumes_service from '@/api/resumes_service';

export default {
  name: "ResumeDetails",
  data() {
    return {
      resume: {},
      liked: Boolean
    }
  },
  async mounted() {
    await this.getResume();
  },
  methods: {
    getResume() {
      resumes_service.getResume(this.$route.params.resumeId).
        then(response => {
          this.resume = response.data;
          this.setlike();
      })
    },
    onlike () {
      this.$store.dispatch('setResumeLike', {id: this.$store.getters.user.employer.id, f_r_id: this.resume.id})
    },
    setlike () {
      let f_v = this.$store.getters.user.favorites.resumes;
      this.liked = f_v.includes(this.resume.id)
    }
  }


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