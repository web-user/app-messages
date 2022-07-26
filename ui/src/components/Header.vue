<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link to="/">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/about">about</router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>
  </header>
  <div class="container">

<!-- Wrapper container -->

</div>
</template>

<script>
export default {
  name: "Header",
  props: {
    title: {
      type: String,
      default: 'Hello World',
    }
  },


}
</script>

<style scoped>
  header {
    display: flex;
    margin-bottom: 20px;
  }
</style>