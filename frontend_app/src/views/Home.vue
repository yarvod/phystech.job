<template>

  <b-container class="mt-5">

    <AddEmployeeModal
      :show_modal_add_employee="show_modal_add_employee"
      @modal_state="show_modal_add_employee = $event"
    />
    <AddEmployerModal
      :show_modal_add_employer="show_modal_add_employer"
      @modal_state="show_modal_add_employer = $event"
    />

      <b-card-group deck>
        <b-card
            title="Я хочу найти сотрудника"
            class="mt-2"
        >
          <b-card-text>
            Я работодатель и ищу работника в свою супер компанию
          </b-card-text>
          <button class="btn btn-outline-success" @click="$router.push({name: 'vacancy_add'})"> Разместить вакансию </button>
          <br>
          <router-link to="/resumes">К списку резюме</router-link>
        </b-card>

        <b-card
            title="Я хочу найти работу"
            class="mt-2"
        >
          <b-card-text>
            Я работник и хочу получить самую лучшую должность :)
          </b-card-text>
          <button class="btn btn-outline-success" @click="$router.push({name: 'resume_add'})"> Разместить резюме </button>
          <br>
          <router-link to="/vacancies">К списку вакансий</router-link>
        </b-card>

      </b-card-group>


<!--      <b-card-group deck>-->

<!--        <b-card-->
<!--            title="Я хочу найти исполнителя"-->
<!--            class="mt-2"-->
<!--        >-->
<!--          <b-card-text>-->
<!--            У меня есть задача, для которой требуется услуга специалиста-->
<!--          </b-card-text>-->
<!--          <button class="btn btn-outline-success" @click="$router.push({name: 'task_add'})"> Разместить задачу </button>-->
<!--          <br>-->
<!--          <router-link to="/services">К списку услуг специалистов</router-link>-->
<!--        </b-card>-->

<!--        <b-card-->
<!--            title="Я хочу предоставить свою услугу"-->
<!--            class="mt-2"-->
<!--        >-->
<!--          <b-card-text>-->
<!--            Я специалист и могу предоставить свою услугу-->
<!--          </b-card-text>-->
<!--          <button class="btn btn-outline-success" @click="$router.push({name: 'service_add'})"> Разместить услугу </button>-->
<!--          <br>-->
<!--          <router-link to="/tasks">К списку задач для иполнения</router-link>-->
<!--        </b-card>-->

<!--      </b-card-group>-->


  </b-container>


</template>


<script>
import AddEmployeeModal from '@/components/AddEmployeeModal.vue';
import AddEmployerModal from '@/components/AddEmployerModal.vue';
export default {
  components: {
    AddEmployeeModal,
    AddEmployerModal
  },
  computed: {
    show_modal_add_employee: {
      get () {
        return eval(this.$route.query.show_modal_add_employee)
      },
      set (v) {
        this.$router.replace({name: 'home'})
      }
    },
    show_modal_add_employer: {
      get () {
        return eval(this.$route.query.show_modal_add_employer)
      },
      set (v) {
        this.$router.replace({name: 'home'})
      }
    }
  }
}
</script>

<style>
</style>