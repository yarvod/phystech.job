<template>
	<div id="app">
    <Header/>
		<router-view/>
	</div>
</template>

<script>
import Header from "@/components/Header";
export default {
  components: {Header}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
*{padding:0;margin:0;border:0;top:0;left:0;}
*,*:before,*:after{-moz-box-sizing:border-box;-webkit-box-sizing:border-box;box-sizing:border-box;}
:focus,:active{outline:none;}
a:focus,a:active{outline:none;}
nav,footer,header,aside{display:block;}
html,body{height:100%;width:100%;font-size:100%;line-height:1;font-size:14px;-ms-text-size-adjust:100%;-moz-text-size-adjust:100%;-webkit-text-size-adjust:100%;}
input,button,textarea{font-family:inherit;}
input::-ms-clear{display:none;}
button{cursor:pointer;}
button::-moz-focus-inner{padding:0;border:0;}
a{text-decoration:none;}
ul li{list-style:none;}
img{vertical-align:top;}
h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight:inherit;}
</style>