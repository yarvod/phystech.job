<template>
  <b-container>

    <b-row>
      <b-col>
        <h2>Мой профиль</h2>
        <hr>
      </b-col>
    </b-row>

    <AddEmployerModal
        :show_modal_add_employer="show_modal_add_employer"
        @modal_state="show_modal_add_employer = $event"
    />
    <AddEmployeeModal
        :show_modal_add_employee="show_modal_add_employee"
        @modal_state="show_modal_add_employee = $event"
    />

    <b-row>
      <b-col>
          <b-tabs
            v-model="tabIndexCurrent"
            active-nav-item-class="font-weight-bold text-uppercase"
            content-class="mt-3"
            justified
          >

            <b-tab title="Аккаунт">
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
                      <div v-if="!user.employee">
                       Вы пока не можете резмещать резюме и откликаться на вакансии
                       <br>
                       <b-button
                          variant="outline-success"
                          @click="show_modal_add_employee = !show_modal_add_employee"
                          v-b-modal.modal-center
                        >
                          Стать соискателем!
                        </b-button>
                      </div>

                      <div v-else>
                        Вы можете размещать резюме и откликаться на вакансии!
                        <br>
                        <b-button @click="$router.push({name: 'resume_add'})" variant="outline-success" class="m-1">Разместить резюме!</b-button>
                        <b-button @click="$router.push({name: 'vacancies'})" variant="outline-success" class="m-1">Найти работу!</b-button>
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
                          <b-button
                              variant="outline-success"
                              @click="show_modal_add_employer = !show_modal_add_employer"
                              v-b-modal.modal-center
                          >
                            Стать работодателем!
                          </b-button>
                        </div>
                        <div v-else>
                          Вы можете размещать вакансии и просматривать резюме!
                          <br>
                          <b-button @click="$router.push({name: 'vacancy_add'})" variant="outline-success" class="m-1">Разместить вакансию!</b-button>
                          <b-button @click="$router.push({name: 'resumes'})" variant="outline-success" class="m-1">Найти работника!</b-button>
                        </div>
                      </div>
                    </b-card-text>
                  </b-card>

<!--                  <b-card>-->
<!--                    <template #header>-->
<!--                      <b v-if="user.client">-->
<!--                        Вы клиент!-->
<!--                      </b>-->
<!--                      <b v-else>-->
<!--                        Вы пока не клиент-->
<!--                      </b>-->
<!--                    </template>-->
<!--                    <b-card-text>-->
<!--                      <div v-if="!user.client">-->
<!--                        Вы пока не можете размещать задачи для исполнения и пользоваться услугами фрилансеров-->
<!--                        <br>-->
<!--                        <b-button variant="outline-success" @click="add_client"> Стать клиентом! </b-button>-->
<!--                      </div>-->
<!--                      <div v-else>-->
<!--                        Вы можете размещать задачи для исполнения и пользоваться услугами фрилансеров!-->
<!--                      </div>-->
<!--                    </b-card-text>-->
<!--                  </b-card>-->

<!--                  <b-card>-->
<!--                    <template #header>-->
<!--                      <b v-if="user.freelancer">-->
<!--                        Вы фрилансер!-->
<!--                      </b>-->
<!--                      <b v-else>-->
<!--                        Вы пока не фрилансер-->
<!--                      </b>-->
<!--                    </template>-->
<!--                    <b-card-text>-->
<!--                      <div v-if="!user.freelancer">-->
<!--                        Вы пока не можете размещать свои услуги и выполнять задачи клиентов-->
<!--                        <br>-->
<!--                        <b-button variant="outline-success" @click="add_freelancer"> Стать фрилансером! </b-button>-->
<!--                      </div>-->
<!--                      <div v-else>-->
<!--                        Вы можете размещать свои услуги для клиентов и искать задачи для исполнения!-->
<!--                      </div>-->
<!--                    </b-card-text>-->
<!--                  </b-card>-->

                </b-card-group>



                <hr>
                <b-row>
                  <b-button variant="outline-primary" class="m-1" @click="$router.push({name: 'account_edit'})">Редактировать</b-button>
                </b-row>
              </b-container>
            </b-tab>


            <b-tab title="Избранное">
              <b-container>
                <b-row>
                  <b-col>
                    <p>Здесь все, что вам понравилось</p>
                  </b-col>
                </b-row>
                
                <PostsWrapper
                  v-if="favorite_items.some(el => el !== undefined)"
                  :items="favorite_items"
                />

<!--                <b-card-group v-if="user.freelancer && (like_filter === 'Tasks' || like_filter === '')" deck>-->
<!--                  <TaskItem-->
<!--                    v-for="task of user.freelancer.favorite_tasks"-->
<!--                    :key="task.id"-->
<!--                    :task="task"-->
<!--                    :edit="false"-->
<!--                  />-->
<!--                </b-card-group>-->

<!--                <b-card-group v-if="user.client && (like_filter === 'Services' || like_filter === '')" deck>-->
<!--                  <ServiceItem-->
<!--                    v-for="service of user.client.favorite_services"-->
<!--                    :key="service.id"-->
<!--                    :service="service"-->
<!--                    :edit="false"-->
<!--                  />-->
<!--                </b-card-group>-->

              </b-container>
            </b-tab>


            <b-tab title="Отклики">
              <b-container>
                <b-row>
                  <b-col>
                    <p>Здесь отображаются отклики на ваши заявки и посты</p>
                  </b-col>
                </b-row>
                
                  <b-card-group deck>
                      <ResponseItem
                        v-for="item of responses"
                        :key="item.id"
                        :item="item"
                        :user="user"
                        :responces="responses"
                        @user_update="user = $event"
                        @item_update="item = $event"
                        @responces_update="response = $event"
                      />
                  </b-card-group>
                
              </b-container>
            </b-tab>


            <b-tab title="Мои резюме" v-if="user.employee">
              <b-container>
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

                <b-row>
                  <b-col 
                    cols="md-4" 
                    class="mb-4"
                    v-for="resume of user.employee.resumes"
                    :key="resume.id"
                  >
                    <ResumeItem
                      :resume="resume"
                      :edit="true"
                    />
                  </b-col>
      
                </b-row>
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

                <b-row>
                  <b-col
                    cols="md-4"
                    class="mb-4"
                    v-for="vacancy of user.employer.vacancies"
                    :key="vacancy.id"
                  >
                    <VacancyItem
                      :vacancy="vacancy"
                      :edit="true"
                    />
                  </b-col>
                 
                </b-row>
              </b-container>
            </b-tab>


<!--            <b-tab title="Мои услуги" v-if="user.freelancer">-->
<!--              <b-container>-->
<!--                <b-row>-->
<!--                  <b-col>-->
<!--                    <b-button-->
<!--                      variant="outline-success"-->
<!--                      @click="$router.push({name:'service_add'})"-->
<!--                    >-->
<!--                      Добавить услугу-->
<!--                    </b-button>-->
<!--                  </b-col>-->
<!--                </b-row>-->

<!--                <br>-->

<!--                <b-card-group deck>-->
<!--                  <ServiceItem-->
<!--                    v-for="service of user.freelancer.services"-->
<!--                    :key="service.id"-->
<!--                    :service="service"-->
<!--                    :edit="true"-->
<!--                  />-->
<!--                </b-card-group>-->
<!--              </b-container>-->
<!--            </b-tab>-->


<!--            <b-tab title="Мои задачи" v-if="user.client">-->
<!--              <b-container>-->
<!--                <b-row>-->
<!--                  <b-col>-->
<!--                    <b-button-->
<!--                      variant="outline-success"-->
<!--                      @click="$router.push({name:'task_add'})"-->
<!--                    >-->
<!--                      Добавить задачу-->
<!--                    </b-button>-->
<!--                  </b-col>-->
<!--                </b-row>-->

<!--                <br>-->

<!--                <b-card-group deck>-->
<!--                  <TaskItem-->
<!--                    v-for="task of user.client.tasks"-->
<!--                    :key="task.id"-->
<!--                    :task="task"-->
<!--                    :edit="true"-->
<!--                  />-->
<!--                </b-card-group>-->
<!--              </b-container>-->
<!--            </b-tab>-->

          </b-tabs>
      </b-col>
    </b-row>

  </b-container>
</template>


<script>

import ResumeItem from "@/components/ResumeItem";
import VacancyItem from "@/components/VacancyItem";
// import ServiceItem from "@/components/ServiceItem";
// import TaskItem from "@/components/TaskItem";
import PostsWrapper from "@/components/PostsWrapper";
import ResponseItem from "@/components/ResponseItem";
import AddEmployerModal from "@/components/AddEmployerModal";
import AddEmployeeModal from "@/components/AddEmployeeModal.vue";
import employees_service from "@/api/employees_service";
import clients_service from "@/api/clients_service";
import employers_service from "@/api/employers_service";
import freelancers_service from "@/api/freelancers_service";
import { mapGetters } from "vuex";
export default {
  components: {VacancyItem,
    ResumeItem,
    // ServiceItem,
    // TaskItem,
    AddEmployerModal,
    AddEmployeeModal,
    ResponseItem,
    PostsWrapper,
  },
  data() {
    return {
      // user: {
      //   employee: {},
      //   employer: {},
      //   freelancer: {},
      //   client: {}
      // },
      responses: [],
      like_filter: '',
      show_modal_add_employer: false,
      show_modal_add_employee: false,
      loading_favorites: false,
    }
  },
  async mounted() {
    this.loading_favorites = true;
    this.fill_responses()
  },
  computed: {
    ...mapGetters(['user']),
    tabIndexCurrent: {
      set (v) {
        this.$router.push({name: 'account', params: {tabIndex: v}})
      },
      get () {
        return Number(this.$route.params.tabIndex)
      }
    },
    favorite_items () {
      let res = [];
      if (this.user.employer && (this.like_filter === 'Resumes' || this.like_filter === '')) {
        res = res.concat(this.user.employer.favorite_resumes)
      }
      if (this.user.employee && (this.like_filter === 'Vacancies' || this.like_filter === '')) {
        res = res.concat(this.user.employee.favorite_vacancies)
        res = res.concat(this.user.employee.favorite_offers)
      }
      return res
    }
  },
  methods: {
    add_employee () {
      employees_service.createEmployee({user: this.user.id})
    },
    add_client () {
      clients_service.createClient({user: this.user.id})
    },
    add_employer () {
      employers_service.createEmployer({user: this.user.id})
    },
    add_freelancer () {
      freelancers_service.createFreelancer({user: this.user.id})

    },
    fill_responses () {
      if (this.user.employee) {
        this.responses = this.responses.concat(this.user.employee.r2v)
      }
      if (this.user.employer) {
        this.responses = this.responses.concat(this.user.employer.r2v)
      }
    }
  }
}

</script>


<style>

</style>