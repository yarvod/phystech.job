<template>
  <div class="header">
    <div class="header__menu">
      <div class="header__section headgeneral">
        <a href="/" class="header__item headlogo" title="Домашняя страница" tabindex="0">
          <h1>PJ</h1>
        </a>
        <form class="header__item headloc" title="Выберете регион">
          <select>
            <option value="1" tabindex="1">Долгопрудный</option>
            <option value="2" tabindex="2">Жуковский</option>
            <option value="3" tabindex="3">Москва</option>
            <option value="4" tabindex="4">Похую</option>
          </select>
        </form>
        <a href="/help" class="header__item headhelp" title="Помощь" tabindex="5">
          <p>HELP here</p>
        </a>
      </div>
      <div class="header__section headaccount">
        <div class="header__item headpa">
          <form action="/account">
            <button type="link" title="Личный кабинет" tabindex="6">Личный кабинет</button>
          </form>
        </div>
        <!-- <div class="header__enter">
          <form action="/enter">
            <button type="link" title="Войти в личный кабинет" tabindex="#">Войти</button>
          </form>
        </div>
        <div class="header__reg">
          <form action="/registration">
            <button type="link" title="Создать учётную" tabindex="#">Регистрация</button>
          </form>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>
.header {
  display: flex;
  height: 64px;
  min-width: 100%;
  position: sticky;
  border-bottom: 1px solid skyblue;
  background: white;
}

.header__menu {
  display: flex;
  min-width: 100%;
  justify-content: space-between;
  align-items: center;
}

.header__section {
  display: flex;
  flex-direction: row;
}

.header__item {
  padding: 2px;
  margin: 5px;
  color: skyblue;
  border: 1px solid black;
}

.headgeneral {
  margin-left: 10px;
}

.headaccount {
  margin-right: 10px;
}
</style>