<template>
  <b-row>
    <b-col v-for="item of items" :key="item.created+item.id" cols="md-4" class="mb-4">
      <VacancyItem
        v-if="item.employer"
        :vacancy="item"
        :edit="false"
      />
      <OfferItem
        v-if="item.admin"
        :offer="item"
        :edit="false"
      />
      <ResumeItem
        v-if="item.employee"
        :resume="item"
        :edit="false"
      />
    </b-col>
  </b-row>
</template>

<script>
import VacancyItem from "@/components/VacancyItem";
import OfferItem from "@/components/OfferItem";
import ResumeItem from "@/components/ResumeItem";
export default {
  name: "PostWrapper",
  components: {
    VacancyItem,
    OfferItem,
    ResumeItem,
  },
  props: ['items']
}
</script>

<style scoped>

</style>