<template>

  <b-container>
    <b-row>
      <b-col>
        <h2 v-if="isVacancyEdit">Редактирование вакансии</h2>
        <h2 v-else>Добавление вакансии</h2>
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
              :value="vacancy.title"
              v-model="vacancy.title"
              placeholder="Введите название"
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="about-group" label="О вакансии:" label-for="about">
            <b-form-textarea
              id="about"
              :value="vacancy.about"
              v-model="vacancy.about"
              placeholder="Расскажите о вакании"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="duties-group" label="Обязанности" label-for="duties">
            <b-form-textarea
              id="duties"
              :value="vacancy.duties"
              v-model="vacancy.duties"
              placeholder="Расскажите об обязанностях сотрудника"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="requirements-group" label="Требования" label-for="requirements">
            <b-form-textarea
              id="requirements"
              :value="vacancy.requirements"
              v-model="vacancy.requirements"
              placeholder="Расскажите о требованиях к сотруднику"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="conditions-group" label="Условия работы:" label-for="conditions">
            <b-form-textarea
              id="conditions"
              :value="vacancy.conditions"
              v-model="vacancy.conditions"
              placeholder="Расскажите об условиях работы"
              required
            >
            </b-form-textarea>
          </b-form-group>
          
          <b-form-group id="location-group" label="Адрес:" label-for="location">
            <b-form-input
              id="location"
              type="text"
              :value="vacancy.location"
              v-model="vacancy.location"
              placeholder="Страна, город ..."
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group label="Зарплата:" label-for="salary">
            <b-container>
              <b-row>
                <b-col>
                  <b-form-group label="От:" label-for="salary_min" label-cols-sm="4" label-align-sm="right">
                    <b-form-input
                        id="salary_min"
                        type="number"
                        step="1000"
                        min="0"
                        v-model="vacancy.salary_min"
                    ></b-form-input>
                  </b-form-group>
                </b-col>
                <b-col>
                  <b-form-group label="До:" label-for="salary_max" label-cols-sm="4" label-align-sm="right">
                    <b-form-input
                      id="salary_max"
                      type="number"
                      step="1000"
                      min="0"
                      v-model="vacancy.salary_max"
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
              <b-row>
                <b-col>
                  <b-form-group label="Валюта:" label-for="currency" label-cols-sm="4" label-align-sm="right">
                    <b-form-select 
                    id="currency"
                    v-model="vacancy.currency"
                    :options="currencies"
                    >
                    </b-form-select>
                  </b-form-group>
                </b-col>
                <b-col>
                  <b-form-group label="Период:" label-for="billing_period" label-cols-sm="4" label-align-sm="right">
                    <b-form-select 
                    id="billing_period"
                    v-model="vacancy.billing_period"
                    :options="billing_periods"
                    >
                    </b-form-select>
                  </b-form-group>
                </b-col>
              </b-row>
            </b-container>
                
          </b-form-group>
          

          <TagMultiSelect
            :options="tags"
            :value="vacancy.tags"
            @set_tags="vacancy.tags = $event"
          />

          <br>

          <b-form-group id="category-group" label="Категория:" label-for="category">
            <b-form-select 
            id="category"
            v-model="vacancy.category"
            :options="categories"
            required
            >
            </b-form-select>
          </b-form-group>
          
          <br>

          <b-form-group>
            <b-form-checkbox
                v-model="vacancy.distant_work"
                value="true"
                unchecked-value="false"
            >
              Удаленная работа
            </b-form-checkbox>
          </b-form-group>

          <hr>

          <b-row>
            <b-col cols="auto">
               <b-button type="submit" variant="outline-primary" @click="onSubmit">Сохранить</b-button>
            </b-col>
            <b-col cols="auto">
              <b-form-checkbox
                  v-model="vacancy.is_published"
                  value="true"
                  unchecked-value="false"
              >
                Опубликовать
              </b-form-checkbox>
            </b-col>
            <b-col v-if="isVacancyEdit" cols="auto text-right">
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
import categories_service from "@/api/categories_service";
import currencies_service from "@/api/currencies_service";
import billing_periods_service from "../api/billing_periods_service";
import vacancies_service from "@/api/vacancies_service";
import TagMultiSelect from "@/components/TagMultiSelect";
import { mapGetters } from "vuex";
export default {
  name: "Vacancy",
  props: [
    'isVacancyEdit',
  ],
  components: {
    TagMultiSelect
  },
  data() {
    return {
      vacancy: {
        title: '',
        about: '',
        duties: '',
        requirements: '',
        skills: '',
        conditions: '',
        location: '',
        salary_min: null,
        salary_max: null,
        distant_work: false,
        is_published: false,
        tags: []
      },
      tags: [],
      categories: [{value: null, text: 'Выберете категорию'}],
      currencies: [],
      billing_periods: []
    }
  },
  computed: {
    ...mapGetters(['user'])
  },
  async mounted () {
    await tags_service.getTags()
      .then(response => {this.tags = response.data})
    await categories_service.getCategories()
      .then(resp => {
        this.categories = this.categories.concat(resp.data.map(x => ({value: x.slug, text: x.title})))
      })
    await currencies_service.getCurrencies()
      .then(resp => {
        this.currencies = this.currencies.concat(resp.data.map(x => ({value: x.title, text: x.title})))
      })
    await billing_periods_service.getBillingPeriods()
      .then(resp => {
        this.billing_periods = this.billing_periods.concat(resp.data.map(x => ({value: x.title, text: x.title})))
      })
    if (this.$route.params.vacancyId) {
      if (this.isVacancyEdit) {
        let {data} = await vacancies_service.getVacancyDetail(this.$route.params.vacancyId);
        this.vacancy = data
      }
      else {
        let {data} = await vacancies_service.getVacancy(this.$route.params.vacancyId);
        this.vacancy = data
      }
    }
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault()
      if (this.isVacancyEdit) {
        this.vacancy.employer = this.user.employer.id
        this.$store.dispatch('updateVacancy', {vacancy: this.vacancy})
      } else {
        this.vacancy.employer = this.user.employer.id
        this.$store.dispatch('createVacancy', {vacancy: this.vacancy})
        this.onReset()
      }
      await this.$store.dispatch('getMe')
        .then(
          this.$router.back()
        )
    },
    onReset() {
      // Reset our form values
      this.vacancy = {}
    },
    onDelete() {

    }
  }
}
</script>

<style scoped>

</style>