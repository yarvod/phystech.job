<template>
	<div id="app">
    <Header
      :user="$store.getters.user"
      :show_login="$route.params.show_login"
    />
    <router-view/>

	</div>
</template>

<script>
import Header from "@/components/Header";
import axios from "axios";

export default {
  components: {
    Header
  },
  async beforeMount() {
    await this.$store.commit('storeToken')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
    if (this.$store.getters.isAuthenticated) {
      await this.$store.dispatch('getMe')
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
a{text-decoration:none;}
img{vertical-align:top;}
</style>