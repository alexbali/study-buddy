<template>
  <div>
    <NavBar />
    <SignIn v-if="!displayHomePage" @sign-in="displayHome"/>
    <VideoPage v-if="displayHomePage" :email="email"/>
    <!-- <HomePage v-if="displayHomePage" :email="email" /> You'll want to merge the functionality of home and video-->
  </div>

</template>

<script>

import "bootstrap/dist/css/bootstrap.min.css"
import NavBar from './components/NavBar.vue'
import SignIn from './components/SignIn.vue'
import HomePage from './components/HomePage.vue'
import VideoPage from './components/VideoPage.vue'


export default {
  name: 'App',
  data() {
    return {
      displayHomePage: false,
      email: "",
    }
  },
  components: {
    NavBar,
    SignIn,
    HomePage,
    VideoPage
  },
  methods: {
    displayHome(email) {
      console.log('inside home')
      this.email = email
      this.displayHomePage = !this.displayHomePage
    },
  },
  emits:['sign-in'],
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
}
</style>