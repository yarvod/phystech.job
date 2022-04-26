<template>
  <b-container>
    <b-row class="mt-2">
      <b-col>

        <b-tabs content-class="mt-3" fill>

            <b-tab title="Вход">
              <div class="text-center">
                <b-form @submit.prevent="submitLogin">
                  <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
                    <b-form-input v-model="username" placeholder="username" type="text"></b-form-input>
                  </b-input-group>
                    <br>
                  <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
                    <b-form-input v-model="password" placeholder="password" type="password"></b-form-input>
                  </b-input-group>
                  <div v-if="errors.length">
                    <br>
                    <b-alert variant="danger" show v-for="error in errors" v-bind:key="error"> {{ error }} </b-alert>
                  </div>
                  <br>
                  <b-button size="md" class="my-2 my-sm-0" type="submit">Войти</b-button>
                </b-form>
              </div>
            </b-tab>

            <b-tab title="Регистрация" active>

              <b-form @submit.prevent="submitRegistration">
                <b-form-group
                  id="input-group-1"
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

                <b-form-group id="input-group-2" label="Имя, Фамилия:" label-for="input-2">
                  <b-form-input
                    id="input-2"
                    v-model="reg_form.first_name"
                    placeholder="Имя"
                    required
                  ></b-form-input>
                  <b-form-input
                    class="mt-1"
                    id="input-3"
                    v-model="reg_form.second_name"
                    placeholder="Фамилия"
                    required
                  ></b-form-input>
                </b-form-group>


                <b-form-group id="input-group-4" v-slot="{ ariaDescribedby }">
                  <b-form-checkbox-group
                    v-model="reg_form.checked"
                    id="checkboxes-4"
                    :aria-describedby="ariaDescribedby"
                  >
                    <b-form-checkbox value="me">Check me out</b-form-checkbox>
                    <b-form-checkbox value="that">Check that out</b-form-checkbox>
                  </b-form-checkbox-group>
                </b-form-group>

                <b-button type="submit" variant="primary" @click="submitRegistration">Продолжить</b-button>
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
  props: ['reg', 'login'],
  data () {
    return {
      username: '',
      password: '',
      errors: [],
      reg_form: {}
    }
  },
  methods: {
    async submitLogin() {
      localStorage.removeItem("token")
      const formData = {
        username: this.username,
        password: this.password
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
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else {
              this.errors.push('Something went wrong. Please try again')

              console.log(JSON.stringify(error))
            }
          })

    },
    onReset() {
      this.username = ''
      this.password = ''
    },
    submitRegistration() {
      console.log(JSON.stringify(this.reg_form))
    }
  }
}
</script>

<style scoped>

</style>