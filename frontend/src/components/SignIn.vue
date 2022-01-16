<template>
<div class="container">
    <div class="container-elements">
        <h1 class="h1-header">Welcome To Study Buddy</h1>
        <h2 class="header-instruction">Enter Your Email</h2>
        <div class="form-outline email-input">
            <input v-model="email" placeholder="youremail@ualberta.ca" type="text" id="typeText" class="form-control" />
            <!-- <label class="form-label" for="typeText">Text input</label> -->
        </div>
        <button @click="authenticateWithGoogle" type="button" class="btn btn-outline-primary signin-btn">Authenticate with Google</button>
    </div>


</div>
  
</template>

<script>
import GAuth from 'vue-google-oauth2'

export default {
    name: 'SignIn',
    data() {
        return {
            email: "",
        }
    },
    methods: {
        async authenticateWithGoogle() {
            const gauthOption = {
            clientId: 'CLIENT_ID.apps.googleusercontent.com',
            scope: 'profile email',
            prompt: 'select_account'
        }
        Vue.use(GAuth, gauthOption)
        }
    },
}
</script>

<style>
.h1-header{
    margin: 20px;
}

.container{
    border: 4px solid black;
    width: 50%;
    height: 400px;
    margin-top: 60px;
}

.email-input {
    width: 50%;
    align-items: center;
    margin: auto;
    margin-top: 40px;
}

.header-instruction {
    margin-top: 20px;
}

.container-elements {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    background: rgb(255, 255, 255);
    height: 100%;
}

.signin-btn {
    margin: 20px;
}
</style>