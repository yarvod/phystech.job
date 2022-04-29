<template>
  <b-container>
    <b-row class="mt-2">
      <b-col>

        <b-tabs content-class="mt-3" fill>

            <b-tab title="Вход">
              <div class="text-center">
                <b-form @submit.prevent="submitLogin">
                  <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
                    <b-form-input v-model="login_username" placeholder="username" type="text" required></b-form-input>
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
            </b-tab>

            <b-tab title="Регистрация">

              <b-form @submit.prevent="submitRegistration" novalidate>

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
                      Я работадатель и ищу работника в свою супер компанию
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
                <h4>Заполните форму:</h4>
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
                      v-validate="{ required: true, min: 3 }"
                      :state="validateState('input-pass1')"
                      aria-describedby="input-pass1-feedback"
                      name="password1"
                    ></b-form-input>
                    <b-form-invalid-feedback id="input-pass1-feedback">{{ veeErrors.first('input-pass1') }}</b-form-invalid-feedback>
  <!--                  <b-form-text id="password-help-block">-->
  <!--                    Your password must be 8-20 characters long, contain letters and numbers, and must not-->
  <!--                    contain spaces, special characters, or emoji.-->
  <!--                  </b-form-text>-->

                    <b-form-input
                      id="input-pass2"
                      class="mt-1"
                      v-model="reg_form.confirmPassword"
                      type="password"
                      placeholder="Enter a password again"
                      v-validate="{ required: true, min: 3 }"
                      :state="validateState('input-pass2')"
                      data-vv-name="password2"
                    ></b-form-input>
  <!--                  <b-form-invalid-feedback id="input-pass2-feedback">{{ veeErrors.first('input-pass2') }}</b-form-invalid-feedback>-->

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
                      v-model="reg_form.second_name"
                      placeholder="Фамилия"
                      required
                    ></b-form-input>
                  </b-form-group>


                  <b-button type="submit" variant="primary" @click="submitRegistration" :disabled="Boolean(passwordError)">
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
      login_username: '',
      login_password: '',
      login_error: '',
      showLoginError: false,
      reg_form: {
        email: '',
        password: '',
        confirmPassword: '',
        as_employee: false,
        as_employer: false
      },
    }
  },
  computed: {
    passwordError () {
      if (this.reg_form.password !== this.reg_form.confirmPassword) {
        return 'Пароли должны совпадать!'
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
    }
  },
  methods: {
    async submitLogin() {
      localStorage.removeItem("token")
      const formData = {
        username: this.login_username,
        password: this.login_password
      }
      await user_service.LogIn(formData)
          .then(response => {
            const token = response.data.auth_token  // получаем токен из бэка
            this.$store.commit('setToken', token)  // сохраняем токен в сторе

            localStorage.setItem("token", token)  // сохраняем токен в хранилище
            this.$store.dispatch('getMe')  // получаем юзера из бэка и кладем в стор
            this.$router.push({name: 'home'})  // переходим на домашнюю страницу
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
      this.username = '';
      this.password = '';
      this.$nextTick(() => {
        this.$validator.reset();
      });
    },
    validateState(ref) {
      if (
        this.veeFields[ref] &&
        (this.veeFields[ref].dirty || this.veeFields[ref].validated)
      ) {
        return !this.veeErrors.has(ref);
      }
      return null;
    },
    submitRegistration() {
      this.$validator.validateAll().then(result => {
        if (!result) {
          return;
        }
        alert("Form submitted!");
      });
      console.log(JSON.stringify(this.reg_form))
    }
  }
}
</script>

<style scoped>

</style>