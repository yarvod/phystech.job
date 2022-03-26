<template>

  <div class="container mt-5">
    <div class="row mt-2">
      <div class="col mr-1 text-center border rounded shadow-sm mt-2">
        <h4>Я хочу найти сотрудника</h4>
        <br>
        <button class="btn btn-outline-success"> Разместить вакансию </button>
        <br>
        <router-link to="/resumes">К списку резюме</router-link>
      </div>
      <div class="col text-center border rounded shadow-sm mt-2">
        <h4>Я хочу найти работу</h4>
        <br>
        <button class="btn btn-outline-success"> Разместить резюме </button>
        <br>
        <router-link to="/vacancies">К списку вакансий</router-link>
      </div>
    </div>

    <div class="row mt-2">
      <div class="col mr-1 text-center border rounded shadow-sm mt-2">
        <h4>Я хочу найти исполнителя</h4>
        <br>
        <button class="btn btn-outline-success"> Разместить задачу на исполнение </button>
        <br>
        <router-link to="/">К списку услуг фрилансеров</router-link>
      </div>
      <div class="col text-center border rounded shadow-sm mt-2">
        <h4>Я хочу предоставить свою услугу</h4>
        <br>
        <button class="btn btn-outline-success"> Разместить услугу </button>
        <br>
        <router-link to="/">К списку задач для иполнения</router-link>
      </div>
    </div>

  </div>


</template>


<script>

export default {
  components: {}
}
</script>

<style>
</style>