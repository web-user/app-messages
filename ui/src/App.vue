<template>


  <div id="nav">
  <nav class="container navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Logo Here</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div class="navbar-nav mr-auto">
            <router-link to="/" class="nav-item nav-link">Home</router-link>
            <router-link to="/chat" class="nav-item nav-link">Mail</router-link>
            <router-link to="/sing-up" class="nav-link">Sing Up</router-link>
            <router-link to="/login" class="nav-link">Login</router-link>
        </div>
    </div>
</nav>
 </div>
  <router-view/>
</template>

<script>
import axios from 'axios'
export default {
    name: "App",
    beforeCreate() {
        this.$store.commit('initializeStore')
        const access = this.$store.state.access

        if( access ){
          axios.defaults.headers.common["Authorization"] = "JWT " + access
        } else {
          axios.defaults.headers.common["Authorization"] = ""
            this.$router.push('/')
        }
    },
    mounted() {
        setInterval((() => {
            this.getAccess()
        }, 5000))
    },
    methods: {
        getAccess(e) {
            const accessData = {
                refresh: this.$store.state.refresh
            }
            axios.post('/api/token/refresh/', accessData).then(response => {
                const access = response.data.access

                console.log(access)

                localStorage.setItem('access', access)
                this.$store.commit('setAccess', access)
            }).catch(error => {
                console.log(error)
            })
        }
    },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
