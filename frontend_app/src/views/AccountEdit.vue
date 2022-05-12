<template>
  <b-container>
    <b-row>
      <h4>Общая информация</h4>
    </b-row>
    <b-row>
      <b-col>
          <b>Имя: </b> {{user.first_name}} {{user.last_name}}
          <br>
          <b>E-mail: </b> {{user.email}}
          <br>
          <b>Телефон: </b> {{user.phone_number}}
          <br>
          <b>Телеграм:</b> {{user.telegram}}
      </b-col>
    </b-row>
    <b-row>
      <h4>Возможности</h4>
    </b-row>

    <b-card-group deck>

      <b-card v-if="!user.employer">
        <template #header>
          <b v-if="user.employee">
            Вы соискатель!
          </b>
          <b v-else>
            Вы пока не соискатель
          </b>
        </template>
        <b-card-text>
           <div>
            <div v-if="!user.employee">
              Вы пока не можете резмещать резюме и откликаться на вакансии
              <br>
              <b-link @click="add_employee"> Стать соискателем! </b-link>
            </div>
            <div v-else>
              Вы можете размещать резюме и откликаться на вакансии!
            </div>
          </div>
        </b-card-text>
      </b-card>

       <b-card v-if="!user.employee">
         <template #header>
           <b v-if="user.employer">
             Вы работодатель!
           </b>
           <b v-else>
             Вы пока не работодатель
           </b>
         </template>
        <b-card-text>
          <div>
            <div v-if="!user.employer">
              Вы пока не можете размещать вакансии и просматривать резюме
              <br>
              <b-link @click="add_employer"> Стать работодателем! </b-link>
            </div>
            <div v-else>
              Вы можете размещать вакансии и просматривать резюме!
            </div>
          </div>
        </b-card-text>
      </b-card>

      <b-card>
        <template #header>
          <b v-if="user.client">
            Вы клиент!
          </b>
          <b v-else>
            Вы пока не клиент
          </b>
        </template>
        <b-card-text>
          <div v-if="!user.client">
            Вы пока не можете размещать задачи для исполнения и пользоваться услугами специалистов/фрилансеров
            <br>
            <b-link @click="add_client"> Стать клиентом! </b-link>
          </div>
          <div v-else>
            Вы можете размещать задачи для исполнения и пользоваться услугами специалистов/фрилансеров!
          </div>
        </b-card-text>
      </b-card>

      <b-card>
        <template #header>
          <b v-if="user.freelancer">
            Вы специалист/фрилансер!
          </b>
          <b v-else>
            Вы пока не специалист/фрилансер
          </b>
        </template>
        <b-card-text>
          <div v-if="!user.freelancer">
            Вы пока не можете размещать свои услуги и выполнять задачи клиентов
            <br>
            <b-link @click="add_freelancer"> Стать фрилансером! </b-link>
          </div>
          <div v-else>
            Вы можете размещать свои услуги для клиентов и искать задачи для исполнения!
          </div>
        </b-card-text>
      </b-card>

    </b-card-group>

  </b-container>
</template>

<script>
export default {
  name: "AccountEdit",
  data () {
    return {
      user: {}
    }
  },
  async mounted() {
    // await this.$store.dispatch('getMe')
    this.user = await this.$store.getters.user;
  }
}
</script>

<style scoped>

</style>