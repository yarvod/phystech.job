<template>
	<div id="app">
    <div class="header">
      <a href="/"><h1>phystech.job</h1></a>
      <form class="form">
        <select>
          <option value="1">Долгопрудный</option>
          <option value="2">Жуковский</option>
          <option value="3">Москва</option>
          <option value="4">По-хуй</option>
        </select>
          
      </form>
      <div class="help">
        HELP here
      </div>
    </div>
      <hr style="margin: 0; width: 100%; position: fixed; top: 0; left: 0">
		
		<router-view/>
	</div>
</template>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 100px;
  margin-bottom: 0;
  padding-bottom: 0;
}

.header {
  display: flex;
  flex-direction: row;
  width: 100%;
  margin: 0;
  position: fixed;
  top: 0;
  left: 0;

  background: antiquewhite;
}

.form {
  align-content: center;
  position: relative;
  margin: 0 15px;
}

.help {
  align-content: center;
  position: relative;
  margin: 0 15px;
}
</style>
