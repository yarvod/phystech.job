<template>
  <b-container>
    <b-row>
      <b-col>
        <h2>Мой профиль</h2>
        <hr>
      </b-col>
    </b-row>

    <b-row>
      <b-col>
          <b-tabs
            active-nav-item-class="font-weight-bold text-uppercase"
            content-class="mt-3"
            justified
          >

            <b-tab title="Личная информация">
              <div class="container">
                <div class="row">
                  <div class="col">

                      <br>
                      <b>Username: </b> {{user.username}}
                      <br>
                      <b>Имя: </b> {{user.first_name}} {{user.last_name}}
                      <br>
                      <b>E-mail: </b> {{user.email}}
                      <br>
                      <b>Телефон: </b> {{user.phone_number}}
                      <hr>
                      <b-button variant="outline-primary" class="m-1">Редактировать</b-button>

                  </div>
                </div>
              </div>
            </b-tab>


            <b-tab title="Избранное">
              <div class="container">
                <div class="row">
                  <div class="col">
                    <p>Здесь все, что вам понравилось</p>
                  </div>
                </div>

<!--                  <div v-if="user.employer && (like_filter === 'Vacancies' || like_filter === '')">-->
<!--                    <ResumeItem-->
<!--                    v-for="resume of user.employer.favorite_resumes"-->
<!--                    :key="resume.id"-->
<!--                    :resume="resume"-->
<!--                    :edit="false"-->
<!--                    :like="true"-->
<!--                    />-->
<!--                  </div>-->

                <b-card-group v-if="user.employee && (like_filter === 'Resumes' || like_filter === '')" deck>
                  <VacancyItem
                  v-for="vacancy of user.employee.favorite_vacancies"
                  :key="vacancy.id"
                  :vacancy="vacancy"
                  :edit="false"
                  />
                </b-card-group>

              </div>
            </b-tab>


            <b-tab title="Отклики">
              <div class="container">
                <div class="row">
                  <div class="col">
                    <p>Здесь отображаются отклики на ваши заявки и посты</p>
                  </div>
                </div>
              </div>
            </b-tab>


            <b-tab title="Мои резюме" v-if="user.employee">
              <b-container class="container">
                <b-row>
                  <b-col>
                    <b-button
                        variant="outline-success"
                        @click="$router.push({name:'resume_add'})"
                    >
                      Добавить резюме
                    </b-button>
                  </b-col>
                </b-row>

                <br>

                <b-card-group deck>
                  <ResumeItem
                    v-for="resume of user.employee.resumes"
                    :key="resume.id"
                    :resume="resume"
                    :edit="true"
                  />
                </b-card-group>
              </b-container>
            </b-tab>


            <b-tab title="Мои вакансии" v-if="user.employer">
              <b-container>
                <b-row>
                  <b-col>
                    <b-button
                      variant="outline-success"
                      @click="$router.push({name:'vacancy_add'})"
                    >
                      Добавить вакансию
                    </b-button>
                  </b-col>
                </b-row>

                <br>

                <b-card-group deck>
                  <VacancyItem
                    v-for="vacancy of user.employer.vacancies"
                    :key="vacancy.id"
                    :vacancy="vacancy"
                    :edit="true"
                  />
                </b-card-group>
              </b-container>
            </b-tab>


            <b-tab title="Мои услуги" v-if="user.freelancer">
              <div class="container">
                <div class="row">
                  <div class="col">
                    <p>Вы можете разместить услуги, которые можете предоставить</p>
                  </div>
                </div>
              </div>
            </b-tab>


            <b-tab title="Мои заказы" v-if="user.client">
              <div class="container">
                <div class="row">
                  <div class="col">
                    <p>Вы можете разместить заказ на исполнение</p>
                  </div>
                </div>
              </div>
            </b-tab>


            <b-tab title="Мои подписки">
              <div class="container">
                <div class="row">
                  <div class="col">
                    <p>Вы можете подписаться на категории и получать рассылку по электронной почте</p>
                  </div>
                </div>
              </div>
            </b-tab>

          </b-tabs>
      </b-col>
    </b-row>

  </b-container>

</template>


<script>

import ResumeItem from "@/components/ResumeItem";
import VacancyItem from "@/components/VacancyItem";
export default {
  components: {VacancyItem, ResumeItem},
  data() {
    return {
      user: {
        employee: {},
        employer: {},
        freelancer: {},
        client: {}
      },
      like_filter: ''
    }
  },
  async mounted() {
      await this.$store.dispatch('getMe')
      this.user = await this.$store.getters.user;
    },
  methods: {
  }
}

</script>


<style>

</style>