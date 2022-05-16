<template>
  <div>
    <b-card class="mt-2">
      <template #header>
        <b-container>
          <b-row>
            <b-col>
              {{item.type}}
            </b-col>
            <b-col class="text-right">
              <b-dropdown variant="secondary" size="sm" right>
                <div v-if="user.employer">
                  <b-dropdown-item @click="responseItem(true)" variant="success">Принять</b-dropdown-item>
                  <b-dropdown-item @click="responseItem(false)" variant="warning">Отклонить</b-dropdown-item>
                </div>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item @click="deleteItem" variant="danger">Удалить</b-dropdown-item>
              </b-dropdown>
            </b-col>
          </b-row>
        </b-container>
      </template>
      
      <b-card-text v-if="item.type === 'Отклик на вакансию'">
        <div v-if="user.employee">
          <b-link
            class="h5"
            @click="clickItem"
          >
            {{item.to_vacancy.title}}
          </b-link>
          <br>
          <b-link class="small">{{item.to_vacancy.company_name}}</b-link>
        </div>
        
        <div v-if="user.employer">
          <small>Резюме:</small>
          <b-link
            class="h5"
            @click="clickItem"
          >
            {{item.from_resume.title}}
          </b-link>
          <br>
          <small>Вакансия:</small>
          <b-link
            class="small"
          >
            {{item.to_vacancy.title}}
          </b-link>
        </div>
        
        <br>
        Статус: <b>{{status}}</b>
      </b-card-text>
      
      <template #footer>
        <small class="text-muted">
          Создано {{item.created|formatDate}}
        </small>
      </template>
    </b-card>
  </div>
</template>

<script>
import r2v_service from "@/api/r2v_service";
export default {
  name: "ResponseItem",
  props: ['item', 'user', 'responses'],
  data () {
    return {
      new_item: {},
      new_responses: [],
    }
  },
  mounted () {
    this.new_item = this.item;
    this.new_responses = this.responses;
  },
  computed: {
    status () {
      if (this.new_item.accepted) {
        return 'Принято'
      }
      if (this.new_item.accepted === false) {
        return 'Отклонено'
      }
      if (this.new_item.viewed) {
        return 'Просмотрено'
      }
      return 'Не просмотрено'
    }
  },
  methods: {
    clickItem() {
      if (this.item.type === 'Отклик на вакансию') {
        if (this.user.employee) {
          this.$router.push({name: 'vacancy_details', params: {vacancyId: this.item.to_vacancy.id}});
        }
        if (this.user.employer) {
          this.$router.push({name: 'resume_details', params: {resumeId: this.item.from_resume.id}})
          this.new_item.viewed = true;
          r2v_service.updateResume2Vacancy({id: this.item.id, viewed: this.new_item.viewed})
        }
      }
    },
    async deleteItem () {
      this.new_item = {}
      
      await r2v_service.deleteResume2Vacancy(this.item.id)
        .then(
          await this.$store.dispatch('getMe')
        )
        .then(
          this.$emit('user_update', this.$store.getters.user),
          this.$emit('item_update', this.new_item)
        )
      
    },
    async responseItem (response) {
      this.new_item.accepted = response
      
      if (this.item.type === 'Отклик на вакансию') {
        await r2v_service.updateResume2Vacancy({
          id: this.item.id,
          accepted: this.new_item.accepted
        })
        .then(
          await this.$store.dispatch('getMe')
        )
        .then(
          this.$emit('user_update', this.$store.getters.user),
          this.$emit('item_update', this.new_item)
        )
      }
    }
  }
}
</script>

<style scoped>

</style>