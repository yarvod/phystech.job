<template>
    <b-card
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
      img-src="https://placekitten.com/380/200"
      img-alt="Image"
      img-top
      :title=vacancy.title
    >
      <b-card-text>
        <b>Company: </b>
         {{vacancy.company_name}}
        <br>
        <b>Category: </b>
        {{vacancy.category}}
        <br>
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
                @click="$router.push({name: 'vacancy_details', params: {vacancyId: vacancy.id}})">
          Подробнее
        </b-button>

        <b-checkbox
          v-if="this.$store.getters.user && !this.$store.getters.user.employer"
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
  methods: {
    onlike () {
      this.$store.dispatch('setLike', {id: this.$store.getters.user.employee.id, f_v_id: this.vacancy.id})
    },
    setlike () {
      let f_v = this.$store.getters.user.favorites.vacancies;
      this.liked = f_v.includes(this.vacancy.id)
    }
  },
  mounted () {
    if (this.$store.getters.user && !this.edit && !this.$store.getters.user.employer){
      this.setlike()
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