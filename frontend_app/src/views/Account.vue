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
        :user="user"
        @modal_state="show_modal_add_employer = $event"
        @user_update="user = $event"
    />

    <b-row>
      <b-col>
          <b-tabs
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
                       <b-button variant="outline-success" @click="add_employee"> Стать соискателем! </b-button>
                      </div>

                      <div v-else>
                       Вы можете размещать резюме и откликаться на вакансии!
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
                        Вы пока не можете размещать задачи для исполнения и пользоваться услугами фрилансеров
                        <br>
                        <b-button variant="outline-success" @click="add_client"> Стать клиентом! </b-button>
                      </div>
                      <div v-else>
                        Вы можете размещать задачи для исполнения и пользоваться услугами фрилансеров!
                      </div>
                    </b-card-text>
                  </b-card>

                  <b-card>
                    <template #header>
                      <b v-if="user.freelancer">
                        Вы фрилансер!
                      </b>
                      <b v-else>
                        Вы пока не фрилансер
                      </b>
                    </template>
                    <b-card-text>
                      <div v-if="!user.freelancer">
                        Вы пока не можете размещать свои услуги и выполнять задачи клиентов
                        <br>
                        <b-button variant="outline-success" @click="add_freelancer"> Стать фрилансером! </b-button>
                      </div>
                      <div v-else>
                        Вы можете размещать свои услуги для клиентов и искать задачи для исполнения!
                      </div>
                    </b-card-text>
                  </b-card>

                </b-card-group>



                <hr>
                <b-row>
                  <b-button variant="outline-primary" class="m-1">Редактировать</b-button>
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

                  <b-card-group v-if="user.employer && (like_filter === 'Vacancies' || like_filter === '')" deck>
                    <ResumeItem
                      v-for="resume of user.employer.favorite_resumes"
                      :key="resume.id"
                      :resume="resume"
                      :edit="false"
                    />
                  </b-card-group>

                <b-card-group v-if="user.employee && (like_filter === 'Resumes' || like_filter === '')" deck>
                  <VacancyItem
                  v-for="vacancy of user.employee.favorite_vacancies"
                  :key="vacancy.id"
                  :vacancy="vacancy"
                  :edit="false"
                  />
                </b-card-group>

                <b-card-group v-if="user.freelancer && (like_filter === 'Tasks' || like_filter === '')" deck>
                  <TaskItem
                    v-for="task of user.freelancer.favorite_tasks"
                    :key="task.id"
                    :task="task"
                    :edit="false"
                  />
                </b-card-group>

                <b-card-group v-if="user.client && (like_filter === 'Services' || like_filter === '')" deck>
                  <ServiceItem
                    v-for="service of user.client.favorite_services"
                    :key="service.id"
                    :service="service"
                    :edit="false"
                  />
                </b-card-group>

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
              <b-container>
                <b-row>
                  <b-col>
                    <b-button
                      variant="outline-success"
                      @click="$router.push({name:'service_add'})"
                    >
                      Добавить услугу
                    </b-button>
                  </b-col>
                </b-row>

                <br>

                <b-card-group deck>
                  <ServiceItem
                    v-for="service of user.freelancer.services"
                    :key="service.id"
                    :service="service"
                    :edit="true"
                  />
                </b-card-group>
              </b-container>
            </b-tab>


            <b-tab title="Мои задачи" v-if="user.client">
              <b-container>
                <b-row>
                  <b-col>
                    <b-button
                      variant="outline-success"
                      @click="$router.push({name:'task_add'})"
                    >
                      Добавить задачу
                    </b-button>
                  </b-col>
                </b-row>

                <br>

                <b-card-group deck>
                  <TaskItem
                    v-for="task of user.client.tasks"
                    :key="task.id"
                    :task="task"
                    :edit="true"
                  />
                </b-card-group>
              </b-container>
            </b-tab>

          </b-tabs>
      </b-col>
    </b-row>

  </b-container>
</template>


<script>

import ResumeItem from "@/components/ResumeItem";
import VacancyItem from "@/components/VacancyItem";
import ServiceItem from "@/components/ServiceItem";
import TaskItem from "@/components/TaskItem";
import ResponseItem from "@/components/ResponseItem";
import AddEmployerModal from "@/components/AddEmployerModal";
import employees_service from "@/api/employees_service";
import clients_service from "@/api/clients_service";
import employers_service from "@/api/employers_service";
import freelancers_service from "@/api/freelancers_service";
export default {
  components: {VacancyItem,
    ResumeItem,
    ServiceItem,
    TaskItem,
    AddEmployerModal,
    ResponseItem,
  },
  data() {
    return {
      user: {
        employee: {},
        employer: {},
        freelancer: {},
        client: {}
      },
      responses: [],
      like_filter: '',
      show_modal_add_employer: false
    }
  },
  async mounted() {
    await this.load_user()
  },
  methods: {
    async load_user () {
      await this.$store.dispatch('getMe')
      this.user = this.$store.getters.user
      this.fill_responses()

    },
    add_employee () {
      employees_service.createEmployee({user: this.user.id})
        .then(
          this.load_user()
      )
    },
    add_client () {
      clients_service.createClient({user: this.user.id})
        .then(
          this.load_user()
      )
    },
    add_employer () {
      employers_service.createEmployer({user: this.user.id})
        .then(
            this.load_user()
        )
    },
    add_freelancer () {
      freelancers_service.createFreelancer({user: this.user.id})
        .then(
          this.load_user()
      )

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