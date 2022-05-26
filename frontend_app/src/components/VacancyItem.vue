<template>
  <div>
    
    <b-card
      tag="article"
      class="mb-2"
      img-src="https://placekitten.com/380/200"
      img-alt="Image"
      img-top
      :title=vacancy.title
    >

      <template #header>
        Вакансия
      </template>

      <b-card-text>
        <b>Компания: </b>
         {{vacancy.company_name}}
        <br>
        <b>Категория: </b>
        {{vacancy.category}}
        <br>
        <b-row v-if="vacancy.tags">
          <b-col>
            <b>Тэги:</b>
            <b-link class="m-1" v-for="tag in vacancy.tags" :key="tag">
              {{ tag }}
            </b-link>
          </b-col>
        </b-row>
        <b-row>
          <b-col v-if="vacancy.salary_min || vacancy.salary_max">
            <b v-if="vacancy.salary_min">от {{vacancy.salary_min}} </b>
            <b v-if="vacancy.salary_max">до {{vacancy.salary_max}} </b>
            <b v-if="vacancy.currency"> {{vacancy.currency}} </b> 
            <b v-if="vacancy.billing_period"> {{vacancy.billing_period}} </b>
          </b-col>
        </b-row>
      </b-card-text>

      <hr>

      <b-button variant="outline-primary" class="m-1"
        v-if="edit"
        @click="$router.push({name: 'vacancy_edit', params: {vacancyId: vacancy.id}})"
      >
        Редактировать
      </b-button>
      <div v-else>
        <b-button variant="outline-primary" class="m-1"
                @click="goVacancy">
          Подробнее
        </b-button>

        <b-checkbox
          v-if="this.$store.getters.user && this.$store.getters.user.employee"
          v-model="liked"
          @change="onlike"
        >
          like
        </b-checkbox>
      </div>

      <template #footer>
        <small class="text-muted">
          <div v-if="vacancy.is_published">
            <b>Опубликовано: </b>
            {{vacancy.published|formatDate}}
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
  name: "VacancyItem",
  props: ['vacancy', 'edit'],
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
      this.$store.dispatch('setVacancyLike', {id: this.$store.getters.user.employee.id, f_v_id: this.vacancy.id})
    },
    setlike () {
      let f_v = this.$store.getters.user.favorites.vacancies;
      this.liked = f_v.includes(this.vacancy.id)
    },
    goVacancy () {
      this.$router.push({name: 'vacancy_details', params: {vacancyId: this.vacancy.id}})
    }
  }
}
</script>

<style scoped>
</style>