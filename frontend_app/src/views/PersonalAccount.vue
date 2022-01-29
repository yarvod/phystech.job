<template>
  <div class="account">
    <div class="container">
      <div class="pagename">
        <div class="pagename__h">
          <h2 title="Добро пожаловать!">Личный кабинет</h2>
        </div>
      </div>
      <div class="a-posts">
        <div class="a-posts__item a-posts__history">
          <div class="a-posts__cardname">
            <h3 title="info">CardName</h3>
          </div>
          <div class="a-posts__button">
            <form class="a-posts__form" action="#">
              <button class="a-posts__click a-posts__button_1st" type="link" title="#" tabindex="?">Buttton</button>
            </form>
          </div>
          <div class="a-posts__button">
            <form class="a-posts__form" action="#">
              <button class="a-posts__click a-posts__button_1st" type="link" title="#" tabindex="?">Buttton</button>
            </form>
          </div>
          <div class="a-posts__button">
            <form class="a-posts__form" action="#">
              <button class="a-posts__click a-posts__button_1st" type="link" title="#" tabindex="?">Buttton</button>
            </form>
          </div>
        </div>
        <div class="a-posts__item posts__reactions">
          <div class="a-posts__cardname">
            <h3 title="info">CardName</h3>
          </div>
          <div class="a-posts__button">
            <form class="a-posts__form" action="#">
              <button class="a-posts__click a-posts__button_1st" type="link" title="#" tabindex="?">Buttton</button>
            </form>
          </div>
          <div class="a-posts__button">
            <form class="a-posts__form" action="#">
              <button class="a-posts__click a-posts__button_1st" type="link" title="#" tabindex="?">Buttton</button>
            </form>
          </div>
          <div class="a-posts__button">
            <form class="a-posts__form" action="#">
              <button class="a-posts__click a-posts__button_1st" type="link" title="#" tabindex="?">Buttton</button>
            </form>
          </div>
        </div>
        <div class="a-posts__item posts__noted">
          <div class="a-posts__cardname">
            <h3 title="info">CardName</h3>
          </div>
          <div class="a-posts__button">
            <form class="a-posts__form" action="#">
              <button class="a-posts__click a-posts__button_1st" type="link" title="#" tabindex="?">Buttton</button>
            </form>
          </div>
          <div class="a-posts__button">
            <form class="a-posts__form" action="#">
              <button class="a-posts__click a-posts__button_1st" type="link" title="#" tabindex="?">Buttton</button>
            </form>
          </div>
        </div> 
      </div>
    </div>
  </div>
</template>


<script>
</script>


<style>
.pagename {
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;

  border: 1px solid skyblue;
  border-top: none;
}
.pagename__h {
  border: 1px solid black;
}

.a-posts {
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: space-around;

  border: 1px solid skyblue;
  border-top: none;
}
.a-posts__item {
  height: 180px;
  width: 22.5%;
  display: flex;
  flex-direction: column;
  place-items: center start;

  border: 1px solid black;
}
.a-posts__cardname {
  height: 25px;
  width: 10%;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  justify-content: center;

  border: 1px solid skyblue;
  border-top: none;
}
.a-posts__button {
  height: 25px;
  width: 75%;
  margin: auto 0;
  display: flex;
  
  border: 1px solid black;
}
.a-posts__form {
  height: 100%;
  width: 100%;
  overflow: hidden;
  
  background: chartreuse;
}
.a-posts__click {
  height: 100%;
  width: 100%;
}
</style>