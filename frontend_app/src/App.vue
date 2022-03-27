<template>
	<div id="app">
    <Header/>
    <router-view/>

	</div>
</template>

<script>
import Header from "@/components/Header";
import axios from "axios";

export default {
  components: {Header},
  beforeCreate() {
    this.$store.commit('storeToken')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
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