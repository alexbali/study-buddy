<template>
    <nav class="navbar navbar-expand-lg navbar navbar-dark bg-dark">
        <div class="nav-container">
                <a class="navbar-brand" href="#">
    <img src="../assets/logo.png" width="30" height="30" class="d-inline-block align-top" alt="">
    Study Buddy
    </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only"></span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">About</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Team</a>
      </li>
      <div class="right-side">
        <li class="nav-item">
        <a class="nav-link" href="#">GitHub</a>
      </li>
      </div>
    </ul>
  </div>
        </div>

</nav>
</template>

<script>
export default {
    name: 'NavBar'
}
</script>

<style>
.nav-container{
    display: flex;
    justify-content: flex-end;
    align-content: center;
}
</style>