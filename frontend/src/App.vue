<template>
  <div class="home">
    <NavBar />
    <VideoPage />
  </div>
</template>

<script>

import "bootstrap/dist/css/bootstrap.min.css"
import NavBar from './components/NavBar.vue'
import VideoPage from './components/VideoPage.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    VideoPage
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
}
</style>
