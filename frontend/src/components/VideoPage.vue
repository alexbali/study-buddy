<template>
 <div class="container-fluid chat_container" id="app">
   <!-- <h1 class="heading">Welcome {{email}}</h1> -->
   <h1 class="heading">Welcome to Study Buddy, {{email.replace("@ualberta.ca",'')}}!</h1>
   <div class="paragraph">
     Before joining our study rooms, please be sure to observe the following rules to keep our community safe and to ensure you and others are able to study as effectively as possible:
    <ol>
      <li>Be nice</li>
      <li>Be good</li>
      <li>Be awesome</li>
    </ol>
   </div>

     <div class="row" v-if="authenticated">
       <Rooms />
       <Video :username="username"/>
       <!-- <Video :username="email"/> -->
       <Logs />
     </div>
     <div class="row" v-else>
       <div class="username">
           <form class="form-inline" @submit.prevent="submitUsername(username)">
           <!-- <form class="form-inline" @submit.prevent="submitUsername()"> -->
             <div class="form-group mb-2">
                 <input type="text" class="form-control" v-model="username" >
             </div>
             <button type="submit" class="btn btn-primary mb-2 Botton">Start Studying!</button>
         </form>
       </div>
     </div>
 </div>
</template>


<script>
import Rooms from './Rooms'
import Video from './Video'
import Logs from './Logs'
import AddRoom from './AddRoom'

export default {
  name: 'VideoPage',
  props: {
      email: {
          default: 'test@ualberta.ca',
          type: String
      }
  },
  data() {
    return {
      username: "",
      authenticated: false
    }
  },
  components: {
    Rooms,
    Video,
    Logs,
    AddRoom
  },
  methods: {
    submitUsername(username) {
        if(!username) {
          return alert('please provide a username');
        }

        username = 'hardcode';

        this.authenticated = true;
    }
    // submitUsername() {
    //     if(!email) {
    //       return alert('an error has occured, please reload');
    //     }

    //     this.authenticated = true;
    // }
  }
 }
</script>


<style>
 #app {
   font-family: 'Avenir', Helvetica, Arial, sans-serif;
   -webkit-font-smoothing: antialiased;
   -moz-osx-font-smoothing: grayscale;
   text-align: center;
   color: #2c3e50;
   margin-top: 60px;
   background: #2c3e50;
 }
 .box {
   border: 1px solid gray;
 }

 .username {
   margin: 12px auto 7px auto;
   color: wheat;
 }

   .Botton {
   color: #fff;
   background-color: #4d555f;
   border-color: #303840;
   padding: 8px;
   font-weight: bolder;
 }
 
 .heading {
   color: #fff;
 }

 .paragraph {
   color: #fff;
   text-align: left;
   width: 60%;
   position: relative;
   transform: translateX(-50%);
   left: 50%;
 }
</style>