<template>

  <b-container>
    <b-row>
      <b-col>
        <h2 v-if="isServiceEdit">Редактирование услуги</h2>
        <h2 v-else>Добавление услуги</h2>
      </b-col>
    </b-row>
    <b-link @click="$router.back()">Назад</b-link>

    <hr>

    <b-row>
      <b-col>

        <b-form @submit="onSubmit">
          <b-form-group id="title-group" label="Название:" label-for="title">
            <b-form-input
              id="title"
              :value="service.title"
              v-model="service.title"
              placeholder="Введите название"
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="about-group" label="Об услуге:" label-for="about">
            <b-form-textarea
              id="about"
              :value="service.about"
              v-model="service.about"
              placeholder="Расскажите о своей услуге"
              required
            >
            </b-form-textarea>
          </b-form-group>
          
          <b-form-group id="location-group" label="Адрес:" label-for="location">
            <b-form-input
              id="location"
              type="text"
              :value="service.location"
              v-model="service.location"
              placeholder="Страна, город ..."
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group label="Стоимость:" label-for="salary">
            <b-form-input
                id="salary"
                type="number"
                step="1000"
                min="0"
                v-model="service.salary"
            ></b-form-input>
          </b-form-group>

          <TagMultiSelect
              :options="tags"
              :value="service.tags"
              v-model="service.tags"
          />

          <hr>

          <b-row>
            <b-col cols="auto">
               <b-button type="submit" variant="outline-primary" @click="onSubmit">Сохранить</b-button>
            </b-col>
            <b-col cols="auto">
              <b-form-checkbox
                  v-model="service.is_published"
                  value="true"
                  unchecked-value="false"
              >
                Опубликовать
              </b-form-checkbox>
            </b-col>
            <b-col v-if="isServiceEdit" cols="auto text-right">
              <b-button variant="outline-danger" @click="onDelete()">Удалить</b-button>
            </b-col>
          </b-row>

        </b-form>

      </b-col>
    </b-row>

  </b-container>

</template>

<script>
import tags_service from "@/api/tags_service";
import services_service from "@/api/services_service";
import TagMultiSelect from "@/components/TagMultiSelect";
import router from "@/router";
export default {
  name: "Service",
  props: [
    'isServiceEdit',
  ],
  components: {
    TagMultiSelect
  },
  data() {
    return {
      service: {
        title: '',
        about: '',
        location: '',
        salary: null,
        is_published: false,
        tags: []
      },
      tags: [],
      user: {}
    }
  },
  async mounted () {
    let raw_tags = [];
    await tags_service.getTags()
      .then(response => {raw_tags = response.data})
    for (var key in raw_tags) {
      this.tags.push(raw_tags[key].title)
    }
    this.user = this.$store.getters.user
    if (this.$route.params.serviceId) {
      if (this.isServiceEdit) {
        let {data} = await services_service.getServiceDetail(this.$route.params.serviceId);
        this.service = data
      }
      else {
        let {data} = await services_service.getService(this.$route.params.serviceId);
        this.service = data
      }
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      if (this.isServiceEdit) {
        this.service.category = 'it'
        this.service.freelancer = this.user.freelancer.id
        this.$store.dispatch('updateService', {service: this.service})
      } else {
        this.service.category = 'it'
        this.service.freelancer = this.user.freelancer.id
        this.$store.dispatch('createService', {service: this.service})
        this.onReset()
      }
      router.push({name: 'account'})
    },
    onReset() {
      event.preventDefault()
      // Reset our form values
      this.service = {}
    },
    onDelete() {

    }
  }
}
</script>

<style scoped>

</style>