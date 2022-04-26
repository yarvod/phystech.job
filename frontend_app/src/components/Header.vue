<template>

  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand class="btn" @click="$router.push('/')">phystech.job</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <template v-if="$store.getters.isAuthenticated && user">
            <b-nav-item-dropdown right>
              <template #button-content>
                <em type="bright">{{ user.username }}</em>
              </template>
              <b-dropdown-item @click="$router.push({name: 'account'})">Профиль</b-dropdown-item>
              <b-dropdown-item @click="LogOut">Выйти</b-dropdown-item>
            </b-nav-item-dropdown>
          </template>

          <template v-else>
            <b-button class="mx-1" @click="$router.push({name: 'login'})">Вход</b-button>
            <b-button variant="primary"
                      @click="$router.push({name: 'login'})"
            >
              Регистрация
            </b-button>
          </template>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>

</template>

<script>

export default {
  name: "Header",
  props: ['user'],  // передаем юзера из App
  data () {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    async LogOut() {
      await this.$store.dispatch('LogOut');
      localStorage.removeItem("token");  // Do not remove token from local storage before logout!!!!
      await this.$router.push({name: 'home'});
    }
  }
}
</script>
