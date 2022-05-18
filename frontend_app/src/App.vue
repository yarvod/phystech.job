<template>
	<div id="app">
    
    <div v-if="$store.getters.loading_user">
      <Loader/>
    </div>
    
    <div v-else>
      <Header
        :user="$store.getters.user"
        :show_login="$route.params.show_login"
      />
    
      <div class="wrapper">
        <div class="content">
          <router-view/>
        </div>
    
        <div class="footer">
          <Footer/>
        </div>
      </div>
    </div>

  </div>

</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Loader from '@/components/Loader';
import axios from "axios";

export default {
  components: {
    Header,
    Footer,
    Loader,
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

* {
	margin: 0;
	padding: 0;
}
html,
body {
	height: 100%;
}
.wrapper {
	position: relative;
	min-height: 100%;
}
.content {
	padding-bottom: 90px;
}
.footer {
	position: absolute;
	left: 0;
	bottom: 0;
	width: 100%;
	height: 80px;
}

</style>