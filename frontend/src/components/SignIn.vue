<template>
<div class="container">
    <div class="container-elements">
        <h1 class="h1-header">Welcome To Study Buddy</h1>
        <h2 class="header-instruction">Enter Your Email</h2>
        <div class="form-outline email-input">
            <input v-model="email" placeholder="youremail@ualberta.ca" type="text" id="typeText" class="form-control" />
            <!-- <label class="form-label" for="typeText">Text input</label> -->
        </div>
        <button @click="signIn()" type="button" class="btn btn-outline-primary signin-btn">Sign in with Google</button>

        <button @click="signOut()" type="button" class="btn btn-outline-primary signout-btn">Sign out</button>
    </div>


</div>
  
</template>

<script>

export default {
    name: 'SignIn',
    data() {
        return {
            email: ""
        }
    },
    methods: {
        async signOut(){
            this.$gAuth.signOut()
        },
        async signIn() {
            const googleUser = await this.$gAuth.signIn().catch(error => {
              console.error('Failed to get google user')
              throw error
            })
            
            this.email = googleUser.getBasicProfile().ev;
            if(!this.email){
              throw new Error('Failed to get email from google user')
            }
            // "Not a valid origin for the client: http://localhost:8080 has not been registered for client ID 123368583629-jqqc210j1sbhteum2b0q29c67ghfe9vl.apps.googleusercontent.com. Please go to https://console.developers.google.com/ and register this origin for your project's client ID."
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