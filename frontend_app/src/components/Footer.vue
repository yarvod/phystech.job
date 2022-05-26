<template>
  <v-footer
    color="#17a2b8"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-col
        class="primary lighten-2 py-4 text-center"
        style="color: #fff;"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>phystech.job</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
export default {
  name: "Footer",
  data () {
    return {
      links: [
        'Home',
        'About Us',
        'Team',
        'Services',
        'Blog',
        'Contact Us',
      ],
    }
  }
}
</script>

<style scoped>
</style>