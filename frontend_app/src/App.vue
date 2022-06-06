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
          <router-view class="content"/>
          <Footer class="footer"/>
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
      this.$store.commit('setLoadingUser')
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
.content {
  min-height: calc(100vh - 80px);
}

.linebreaks {
  white-space: pre-line;
}

</style>