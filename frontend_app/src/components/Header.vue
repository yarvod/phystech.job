<template>

  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand class="btn" @click="$router.push('/')">phystech.job</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <template v-if="$store.getters.isAuthenticated">
            <b-nav-item-dropdown right>
              <template #button-content>
                <em type="bright">{{ user.username }}</em>
              </template>
              <b-dropdown-item @click="$router.push({name: 'account'})">Профиль</b-dropdown-item>
              <b-dropdown-item @click="LogOut">Выйти</b-dropdown-item>
            </b-nav-item-dropdown>
          </template>

          <template v-else>
            <b-button id="popover-button-variant" tabindex="0" size="md">Аккаунт</b-button>
            <b-popover target="popover-button-variant" variant="primary" triggers="focus" placement="bottom" size="xl">
              <template #title>Вход</template>
              <div class="text-center">
                <b-form @submit.prevent="submitForm">
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
                <hr>
                <div class="">
                  <b>Еще нет аккаунта?</b>
                  <br>
                  <button size="md" class="my-2 my-sm-0 btn btn-outline-primary">Регистрация</button>
                </div>
              </div>
            </b-popover>
          </template>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>

</template>

<script>
import user_service from "@/api/user_service";
import axios from "axios";

export default {
  name: "Header",
  data () {
    return {
      username: '',
      password: '',
      errors: [],
      user: {}
    }
  },
  methods: {
    async submitForm () {
      localStorage.removeItem("token")
      const formData = {
        username: this.username,
        password: this.password
      }
      await user_service.LogIn(formData)
        .then(response => {
          const token = response.data.auth_token
          this.$store.commit('setToken', token)

          localStorage.setItem("token", token)
          this.$router.push({name: 'home'})
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
      await this.getUser()
    },
    async LogOut () {
      this.onReset()
      await this.$store.dispatch('LogOut');
      localStorage.removeItem("token");  // Do not remove token from local storage before logout!!!!
      await this.$router.push({name: 'home'});

    },
    onReset () {
      this.username = ''
      this.password = ''
    }
  }
}
</script>
