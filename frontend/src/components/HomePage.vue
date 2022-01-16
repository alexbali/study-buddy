<template>
  <div class="home-container">
      <h1>Welcome {{email}}</h1>
  </div>
</template>

<script>
export default {
    name: 'HomePage',
    props: {
        email: {
            default: 'test@ualberta.ca',
            type: String
        }
    }
}
</script>

<style>
.home-container {
    width: 80%;
    height: 600px;
    /* margin-top: auto; */
    /* margin-bottom: auto; */
    margin-top: 20px;
    margin-left: auto;
    margin-right: auto;
    /* margin: auto; */
    background: 3px solid black;
    align-content: center;
    text-align: center;
    border: 2px solid black;
}

</style>