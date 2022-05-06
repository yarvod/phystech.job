<template>

  <b-card-group deck>
    <ServiceItem
      v-for="service of services"
      :key="service.id"
      :service="service"
      :edit="false"
    />
  </b-card-group>

</template>

<script>
import ServiceItem from "@/components/ServiceItem";

export default {
  name: "ServiceList",
  props: ['services'],
  components: {ServiceItem},
}
</script>

<style scoped>

</style>