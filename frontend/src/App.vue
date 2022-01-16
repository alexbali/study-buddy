<template>
  <NavBar />
  <SignIn />
</template>

<script>

import "bootstrap/dist/css/bootstrap.min.css"
import NavBar from './components/NavBar.vue'
import SignIn from './components/SignIn.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    SignIn
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  /* margin: 0; */
}
</style>
