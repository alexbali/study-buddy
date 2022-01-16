<template>
<div class="container">
    <div class="container-elements">
        <h1 class="h1-header">Welcome To Study Buddy!</h1>
        <!-- <h2 class="header-instruction">Enter Your Email</h2> -->
        <button @click="signIn()" type="button" class="btn btn-outline-primary signin-btn">Sign in with Google</button>

        <!-- <button @click="signOut()" type="button" class="btn btn-outline-primary signout-btn">Sign out</button> -->
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
            this.$emit('sign-in', this.email)
            console.log('working')
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
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    background: rgb(255, 255, 255);
    height: 100%;
}

.signin-btn {
    margin: 60px;
}
</style>