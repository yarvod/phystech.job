<template>

  <div class="container">
    <div class="row">
      <div class="col">
        <h2 v-if="isResumeEdit">Редактирование резюме</h2>
        <h2 v-else>Добавление резюме</h2>
      </div>
    </div>
    <b-link @click="$router.back()">Назад</b-link>

    <hr>

    <div class="row">
      <div class="col">

        <b-form ref="formResume" @submit.prevent="onSubmit">
          <b-form-group id="title-group" label="Название:" label-for="title">
            <b-form-input
              id="title"
              :value="resume.title"
              v-model="resume.title"
              placeholder="Введите название"
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="education-group" label="Образование:" label-for="education">
            <b-form-textarea
              id="education"
              :value="resume.education"
              v-model="resume.education"
              placeholder="Расскажите о своем образовании"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="work-experiance-group" label="Опыт работы:" label-for="work_experience">
            <b-form-textarea
              id="work-experience"
              :value="resume.work_experiance"
              v-model="resume.work_experiance"
              placeholder="Расскажите об опыте работы"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="skills-group" label="Навыки:" label-for="skills">
            <b-form-textarea
              id="skills"
              :value="resume.skills"
              v-model="resume.skills"
              placeholder="Расскажите о своих навыках"
              required
            >
            </b-form-textarea>
          </b-form-group>

          <b-form-group id="about-me-group" label="Дополнительная информация о Вас:" label-for="about_me">
            <b-form-textarea
              id="about_me"
              :value="resume.about_me"
              v-model="resume.about_me"
              placeholder="Расскажите о себе (хобби, увлечения ...)"
              required
            >
            </b-form-textarea>
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
                        v-model="resume.salary_min"
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
                      v-model="resume.salary_max"
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
              <b-row>
                <b-col>
                  <b-form-group label="Валюта:" label-for="currency" label-cols-sm="4" label-align-sm="right">
                    <b-form-select 
                    id="currency"
                    v-model="resume.currency"
                    :options="currencies"
                    >
                    </b-form-select>
                  </b-form-group>
                </b-col>
                <b-col>
                  <b-form-group label="Период:" label-for="billing_period" label-cols-sm="4" label-align-sm="right">
                    <b-form-select 
                    id="billing_period"
                    v-model="resume.billing_period"
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
            :value="resume.tags"
            @set_tags="resume.tags = $event"
          />
          <br>

          <b-form-group id="category-group" label="Категория:" label-for="category">
            <b-form-select 
            id="category"
            v-model="resume.category"
            :options="categories"
            required
            >
            </b-form-select>
          </b-form-group>
          
          <br>

          <b-form-group>
            <b-form-checkbox
                v-model="resume.ready_relocate"
                value="true"
                unchecked-value="false"
            >
              Готов к переезду
            </b-form-checkbox>
            <b-form-checkbox
                v-model="resume.ready_distant_work"
                value="true"
                unchecked-value="false"
            >
              Удаленная работа
            </b-form-checkbox>
          </b-form-group>

          <hr>

          <div class="row">
            <div class="col-auto">
               <b-button type="submit" variant="outline-primary">Сохранить</b-button>
            </div>
            <div class="col-auto">
              <b-form-checkbox
                  v-model="resume.is_published"
                  value="true"
                  unchecked-value="false"
              >
                Опубликовать
              </b-form-checkbox>
            </div>
            <div v-if="isResumeEdit" class="col-auto offset-7 text-right">
              <b-button variant="outline-danger" @click="onDelete()">Удалить</b-button>
            </div>
          </div>


        </b-form>

      </div>
    </div>

  </div>

</template>

<script>
import tags_service from "@/api/tags_service";
import categories_service from "@/api/categories_service";
import currencies_service from "@/api/currencies_service";
import billing_periods_service from "../api/billing_periods_service";
import resumes_service from "@/api/resumes_service";
import TagMultiSelect from "@/components/TagMultiSelect";
import { mapGetters } from "vuex";
export default {
  name: "Resume",
  props: [
    'isResumeEdit',
  ],
  components: {
    TagMultiSelect
  },
  data() {
    return {
      resume: {
        title: '',
        about_me: '',
        is_published: false,
        ready_relocate: false,
        ready_distant_work: false,
        work_experiance: '',
        tags: [],
        category: null
      },
      tags: [],
      categories: [{value: null, text: 'Выберете категорию'}],
      currencies: [],
      billing_periods: []
    }
  },
  computed: {
    ...mapGetters(['user']),
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
    if (this.$route.params.resumeId) {
      if (this.isResumeEdit) {
        let {data} = await resumes_service.getResumeDetail(this.$route.params.resumeId);
        this.resume = data
      }
      else {
        let {data} = await resumes_service.getResume(this.$route.params.resumeId);
        this.resume = data;
      }
    }
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault()
      if (this.isResumeEdit) {
        this.resume.employee = this.user.employee.id
        this.$store.dispatch('updateResume', {resume: this.resume})
      } else {
        this.resume.employee = this.user.employee.id
        this.$store.dispatch('createResume', {resume: this.resume})
      }
      await this.$store.dispatch('getMe')
        .then(
          this.$router.back(),
          this.onReset()
        )
      
    },
    onReset() {
      this.$refs.formResume.reset()
    },
    onDelete() {

    }
  }
}
</script>

<style scoped>

</style>