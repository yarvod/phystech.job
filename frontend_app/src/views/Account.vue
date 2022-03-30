<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <h2>Мой профиль</h2>
        <hr>
      </div>
    </div>

    <div class="row">
      <div class="col">
          <b-tabs
            active-nav-item-class="font-weight-bold text-uppercase"
            content-class="mt-3"
            justified
          >
            <b-tab title="Личная информация" active>
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
                      <b>Телефон: </b> {{user.phonenumber}}
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
                    <p>I'm the second tab</p>
                  </div>
                </div>

                <div class="row">
                  <VacancyItem
                    v-for="vacancy of user.employee.liked_vacancies"
                    :key="vacancy.id"
                    :vacancy="vacancy"
                  />
                </div>

              </div>
            </b-tab>

            <b-tab title="Мои резюме">
              <div class="container">
                <div class="row">
                  <div class="col">
                    <b-button variant="outline-success">Добавить резюме</b-button>
                  </div>
                </div>

                <div class="row">
                  <ResumeItem
                    v-for="resume of user.employee.resumes"
                    :key="resume.id"
                    :resume="resume"
                  />
                </div>

              </div>
            </b-tab>

            <b-tab title="Отклики">
              <div class="container">
                <div class="row">
                  <div class="col">
                    <p>I'm the second tab</p>
                  </div>
                </div>
              </div>
            </b-tab>

          </b-tabs>
      </div>
    </div>

  </div>

</template>


<script>

import ResumeItem from "@/components/ResumeItem";
import VacancyItem from "@/components/VacancyItem";
export default {
  components: {VacancyItem, ResumeItem},
  data() {
    return {
      user: {
        employee: {}
      }
    }
  },
  async mounted() {
      await this.$store.dispatch('getMe')
      this.user = await this.$store.getters.user
    }
}

</script>


<style>

</style>