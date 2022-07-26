<template>
  <div class="home">
    <h1>Home</h1>
      <span>{{ user_data }}</span>
  </div>

</template>

<script>

import axios from 'axios'

export default {
    name: 'HomeView',
    data() {
      return {
          user_data: ''
      }
    },
    mounted(){
      this.getMe()
    },
    methods: {
        getMe(e){
          // get me data
            axios.get(process.env.VUE_APP_API_LOCAL_HOST + '/api/auth/users/me/').then(response => {
                console.log(response)
                this.user_data = response.data.phone_number
                localStorage.setItem('user_id', response.data.id)

            }).catch(error => {
                console.log(error)
            })

        }
  }
}
</script>
