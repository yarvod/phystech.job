<template>
  <b-card-group deck>
    <div v-for="item of items" :key="item.created+item.id">
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
    </div>
  </b-card-group>
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