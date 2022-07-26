<template>
    <div class="container py-4">

      <!-- Bootstrap 5 starter form -->
      <form @submit.prevent="submitMessageTo">
          <div class="mb-3">
              <select class="form-control" name="user" v-model="user">
                <option v-for="item in users" :value="item.id" :key="item.id" name="user">
                 {{ item.name }}
                </option>
              </select>
          </div>
        <!-- Message input -->
        <div class="mb-3">
          <label class="form-label" for="message">Message</label>
          <textarea class="form-control" id="message" type="text" name="message" v-model="message" placeholder="Message" style="height: 10rem;"></textarea>
        </div>

        <!-- Form submit button -->
        <div class="d-grid">
          <button class="btn btn-primary btn-lg" type="submit">Submit</button>
        </div>

      </form>

    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "SubmitMessage",
    data(){
        return {
            users: [],
            user: '',
            message: ''
        }
    },
    mounted(){
      this.getUserMessages()
    },
    methods: {
        getUserMessages(e){
          // get users

            axios.get(process.env.VUE_APP_API_LOCAL_HOST + '/api/sent-user/').then(response => {
                this.users = response.data

            }).catch(error => {
                console.log(error)

            })

        },
        submitMessageTo(e){
          // clean up data
            let user_id = localStorage.getItem('user_id')
            const formData = {
                sender: +user_id,
                receiver: this.user,
                message: this.message
            }

            // sent messages
            axios.post(process.env.VUE_APP_API_LOCAL_HOST + '/api/messages/', formData).then(response => {
                this.$router.push('/chat')
            }).catch(error => {
                console.log(error)
            })
        }

  }
}
</script>

<style scoped>

</style>