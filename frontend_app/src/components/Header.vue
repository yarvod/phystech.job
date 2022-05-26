<template>

  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand class="btn" @click="$router.push({name: 'home'})">phystech.job</b-navbar-brand>


      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item @click="$router.push({name: 'home'})">Главная</b-nav-item>
          <b-nav-item href="#">Предложения</b-nav-item>
          <b-nav-item href="#">События</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">

          <template v-if="$store.getters.isAuthenticated && user">
            <b-nav-item-dropdown right>
              <template #button-content>
                <em type="bright">{{ user.username }}</em>
              </template>
              <b-dropdown-item @click="$router.push({name: 'account', params: {tabIndex: 0}})">Профиль</b-dropdown-item>
              <b-dropdown-item @click="$router.push({name: 'account', params: {tabIndex: 1}})">Избранное</b-dropdown-item>
              <b-dropdown-item @click="$router.push({name: 'account', params: {tabIndex: 2}})">Отклики</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item @click="LogOut" variant="danger">Выйти</b-dropdown-item>
            </b-nav-item-dropdown>
          </template>

          <template v-else>
            <b-button class="mx-1" @click="$router.push({name: 'login', params: {tabIndex: 0}})">Вход</b-button>
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
