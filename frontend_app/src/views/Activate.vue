<template>
  <b-container>
    <b-card class="mt-5 text-center" title="Аккаунт активирован!">
      <b-button class="" @click="$router.push({name: 'login'})">Войти</b-button>
    </b-card>
  </b-container>

</template>

<script>
import user_service from "@/api/user_service";
export default {
  name: "Activate",
  async mounted() {
    let data = {uid: this.$route.params.uid, token: this.$route.params.token}
    console.log('data ', data)
    await user_service.activate(data)
  }
}
</script>

<style scoped>

</style>