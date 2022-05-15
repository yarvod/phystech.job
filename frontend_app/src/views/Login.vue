<template>
  <b-container>
    <b-row class="mt-2">
      <b-col>

        <b-tabs content-class="mt-3" fill>

            <b-tab title="Вход">
              <h5>Вход с паролем:</h5>
              <br>
              <div class="text-center">
                <b-form @submit.prevent="submitLogin">
                  <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
                    <b-form-input v-model="login_email" placeholder="email" type="text" required></b-form-input>
                  </b-input-group>
                    <br>
                  <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
                    <b-form-input v-model="login_password" placeholder="password" type="password" required></b-form-input>
                  </b-input-group>
                  <div v-if="login_error">
                    <br>
                    <b-alert variant="danger" v-model="showLoginError" dismissible>
                      {{ login_error }}
                    </b-alert>
                  </div>
                  <br>
                  <b-button size="md" class="my-2 my-sm-0" type="submit">Войти</b-button>
                </b-form>
              </div>
  
              <br>
              
              <b-container>
                <b-row>
                  <h5>Вход через социальную сеть:</h5>
                </b-row>
                <b-row>
                  <b-col>
                    <p>В разработке...</p>
                  </b-col>
                </b-row>
              </b-container>
              
            </b-tab>

            <b-tab title="Регистрация">

              <b-form ref="RegForm" @submit.prevent="submitRegistration">

                <h4> Выберете, что вас интересует: </h4>
                <hr>
                <b-card-group id="type" deck>
                  <b-card>
                    <template #header>
                      <b-form-checkbox v-model="reg_form.as_employer" :disabled="disableEmployer"
                      >
                        Я хочу найти сотрудника
                      </b-form-checkbox>
                    </template>

                    <b-card-text>
                      Я работодатель и ищу работника в свою супер компанию
                    </b-card-text>
                  </b-card>

                  <b-card>
                    <template #header>
                      <b-form-checkbox v-model="reg_form.as_employee" :disabled="disableEmployee"
                      >
                        Я хочу найти новую работу
                      </b-form-checkbox>
                    </template>

                    <b-card-text>
                      Я работник и хочу получить самую лучшую должность :)
                    </b-card-text>
                  </b-card>

                  <b-card>
                    <template #header>
                      <b-form-checkbox v-model="reg_form.as_freelancer">Я хочу предоставить свою услугу</b-form-checkbox>
                    </template>

                    <b-card-text>
                      Я специалист и могу предоставить свою услугу
                    </b-card-text>
                  </b-card>

                  <b-card>
                    <template #header>
                      <b-form-checkbox v-model="reg_form.as_client">Я хочу найти исполнителя</b-form-checkbox>
                    </template>
                    <b-card-text>
                      У меня есть задача, для которой требуется услуга специалиста
                    </b-card-text>
                  </b-card>
                </b-card-group>
                <br>
                <b-alert variant="danger" :show="Boolean(roleError)"> {{roleError}} </b-alert>
                
                <b-form-group v-if="reg_form.as_employer" id="input-comp" label="Ваша компания:" label-for="input-company">
                  <b-form-input
                    id="input-company"
                    v-model="reg_form.company_name"
                    placeholder="Как называется ваша компания/команда/организация?"
                    required
                  ></b-form-input>
                  <b-form-input
                    class="mt-1"
                    id="input-company"
                    v-model="reg_form.company_website"
                    placeholder="Ваш веб-сайт"
                  ></b-form-input>
                  <b-form-textarea
                    class="mt-1"
                    id="about"
                    v-model="reg_form.about"
                    placeholder="Расскажите о компании"
                    required
                  >
                  </b-form-textarea>
                </b-form-group>
  
                <br>
                
                <h4>Регистрация через соц. сеть:</h4>
                <hr>
                <p>В разработке...</p>

                <br>
                <h4>Или регистрация через форму:</h4>
                <hr>

                  <b-form-group
                    id="input-email"
                    label="Почта:"
                    label-for="input-1"
                    description="We'll never share your email with anyone else."
                  >
                    <b-form-input
                      id="input-1"
                      v-model="reg_form.email"
                      type="email"
                      placeholder="Enter email"
                      required
                    ></b-form-input>
                  </b-form-group>
                  <b-alert :show="Boolean(reg_form.email) && !validatedEmail" variant="danger">
                      Почта не корректна!
                  </b-alert>
                  <b-alert :show="emailExists" variant="danger">
                      Уже существует пользователь с такой почтой
                  </b-alert>

                  <b-form-group
                    id="input-password"
                    label="Пароль:"
                    label-for="input-pass"
                  >
                    <b-form-input
                      id="input-pass1"
                      v-model="reg_form.password"
                      type="password"
                      placeholder="Enter a password"
                      aria-describedby="password-help-block"
                      name="password1"
                      required
                    ></b-form-input>
                    <b-form-text id="password-help-block">
                      Your password must be 8-20 characters long, contain letters and numbers, and must not
                      contain spaces, special characters, or emoji.
                    </b-form-text>

                    <b-form-input
                      id="input-pass2"
                      class="mt-1"
                      v-model="reg_form.confirmPassword"
                      type="password"
                      placeholder="Enter a password again"
                      required
                    ></b-form-input>
                    <br>
                    <b-alert :show="Boolean(passwordError)" variant="danger">
                      {{ passwordError }}
                    </b-alert>

                  </b-form-group>

                  <b-form-group id="input-fio" label="Имя, Фамилия:" label-for="input-name">
                    <b-form-input
                      id="input-name"
                      v-model="reg_form.first_name"
                      placeholder="Имя"
                      required
                    ></b-form-input>
                    <b-form-input
                      class="mt-1"
                      id="input-name"
                      v-model="reg_form.last_name"
                      placeholder="Фамилия"
                      required
                    ></b-form-input>
                  </b-form-group>

                  <b-button type="submit" variant="primary" :disabled="!validatedRegForm">
                    Продолжить
                  </b-button>
            </b-form>

            </b-tab>

        </b-tabs>

      </b-col>
    </b-row>

</b-container>
</template>

<script>
import user_service from "@/api/user_service";

export default {
  name: "Login",
  data () {
    return {
      login_email: '',
      login_password: '',
      login_error: '',
      showLoginError: false,
      errorRegister: '',
      email_exists: false,
      reg_form: {
        email: '',
        password: '',
        confirmPassword: '',
        first_name: '',
        last_name: '',
        phone_number: '',
        as_employee: false,
        as_employer: false,
        as_client: false,
        as_freelancer: false
      },
      try_submit: false
    }
  },
  computed: {
    validatedEmail () {
      return this.correctEmail()
    },
    emailExists () {
      return this.checkEmail()
    },
    passwordError () {
      if (this.reg_form.confirmPassword && this.reg_form.password !== this.reg_form.confirmPassword) {
        return 'Пароли должны совпадать!'
      }
      else {
        return ''
      }
    },
    isRole () {
      return (this.reg_form.as_client || this.reg_form.as_freelancer || this.reg_form.as_employee || this.reg_form.as_employer)
    },
    roleError () {
      if (this.try_submit && !this.isRole) {
        return 'Выберете свою роль!'
      }
      else {
        return ''
      }
    },
    disableEmployer () {
      return this.reg_form.as_employee;
    },
    disableEmployee () {
      return this.reg_form.as_employer;
    },
    validatedRegForm () {  //TODO: create new validation
      return !this.passwordError && this.isRole && this.validatedEmail
    }
  },
  methods: {
    async submitLogin() {
      localStorage.removeItem("token")
      const formData = {
        username: this.login_email,
        password: this.login_password
      }
      await user_service.LogIn(formData)
          .then(response => {
            const token = response.data.auth_token  // получаем токен из бэка
            this.$store.commit('setToken', token)  // сохраняем токен в сторе

            localStorage.setItem("token", token)  // сохраняем токен в хранилище
            this.$store.dispatch('getMe')  // получаем юзера из бэка и кладем в стор
            this.$router.push({name: 'home'})  //FIXME: переход на желаему страницу
            this.onReset()
          })
          .catch(error => {
            if (error.response.data['non_field_errors']) {
              this.showLoginError = true
              this.login_error = error.response.data['non_field_errors'][0]
            } else {
              this.showLoginError = true
              this.login_error = 'Something went wrong. Please try again';
            }
          })

    },
    onReset() {
      this.login_email = '';
      this.login_password = '';
    },
    submitRegistration () {
      this.try_submit = true
      if (this.validatedRegForm) {
        user_service.createUser({
          email: this.reg_form.email,
          username: this.reg_form.email,
          password: this.reg_form.password,
          first_name: this.reg_form.first_name,
          last_name: this.reg_form.last_name,
          phone_number: this.reg_form.phone_number,
          reg_data: this.reg_form
        }).catch(error => {
          if (error.response.data) {
            console.log(error.response.data)
          }
        })
        this.$refs.RegForm.reset()
      }
      
    },
    correctEmail () {
      return (/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(this.reg_form.email));
    },
    checkEmail () {
      user_service.checkEmail({email: this.reg_form.email})
      .then(resp => {
        this.email_exists = resp.data.exists
      })
      return this.email_exists
    },
  }
}
</script>

<style scoped>

</style>