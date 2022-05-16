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
      <b>Зарплата: </b> {{resume.salary_min}} - {{resume.salary_max}}
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
      <div class="text-default"> {{resume.about_me}} </div>
    </b-col>
  </b-row>
  <b-row v-if="resume.education">
    <b-col>
      <b class="text-underlined">Образование:</b>
      <div class="text-default"> {{resume.education}} </div>
    </b-col>
  </b-row>
  <b-row v-if="resume.work_experiance">
    <b-col>
      <b class="text-underlined">Опыт работы:</b>
      <div class="text-default"> {{resume.work_experiance}} </div>
    </b-col>
  </b-row>
  <b-row v-if="resume.skills">
    <b-col>
      <b class="text-underlined">Навыки:</b>
      <div class="text-default"> {{resume.skills}} </div>
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
    await this.$store.dispatch('getMe');
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
.default-text {
  font-weight: normal;
}
.text-underlined {
  text-decoration: underline;
}
</style>