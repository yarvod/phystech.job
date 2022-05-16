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
import AddEmployeeModal from "@/components/AddEmployeeModal";

export default {
  name: "VacancyItem",
  props: ['vacancy', 'edit'],
  components: {
    AddEmployeeModal
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
      this.$store.dispatch('setVacancyLike', {id: this.$store.getters.user.employee.id, f_v_id: this.vacancy.id})
    },
    setlike () {
      let f_v = this.$store.getters.user.favorites.vacancies;
      this.liked = f_v.includes(this.vacancy.id)
    },
    goVacancy () {
      if (this.$store.getters.user.employee) {
        this.$router.push({name: 'vacancy_details', params: {vacancyId: this.vacancy.id}})
      }
      else if (!this.$store.getters.user.employer) {
        this.show_modal_add_employee = ! this.show_modal_add_employee
      }
    }
  }
}
</script>

<!--        <input id="heart" v-model="liked" type="checkbox"/>-->
<!--        <label for="heart">❤</label>-->

<style scoped>
body {
  display: flex;
  justify-content: center;
  margin: 0;
  height: 10vh;
}


[id="heart"] {
  position: absolute;
  left: -100vw;
}

[for="heart"] {
  color: #aab8c2;
  cursor: pointer;
  font-size: 1.5em;
  align-self: center;
  transition: color 0.2s ease-in-out;
}

[for="heart"]:hover {
  color: grey;
}

[for="heart"]::selection {
  color: gray;
  background: transparent;
}

[for="heart"]::moz-selection {
  color: gray;
  background: transparent;
}

[id="heart"]:checked + label {
  color: #e2264d;
  will-change: font-size;
  animation: heart 1s cubic-bezier(.17, .89, .32, 1.49);
}



@keyframes heart {0%, 10% {font-size: 0;}}
</style>