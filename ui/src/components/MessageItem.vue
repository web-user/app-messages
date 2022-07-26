<template>


    <tr class="active">
      <td class="mail-rateing">
          <i class="fa fa-star text-warning"></i>
      </td>
      <td>
          <a href="#email-read.html">{{ message.sender }}</a>
      </td>
      <td>
          <a href="#email-read.html">{{ message.message }}</a>
      </td>
      <td>

      </td>
      <td class="text-right">
          {{ printFullDate(message.timestamp) }}
      </td>
        <td>
            <a class="del-item"  @click="delItem(message)"><b-icon-trash-fill></b-icon-trash-fill></a>
        </td>
  </tr>
</template>

<script>
import moment from 'moment'
import axios from 'axios'
export default {
  name: "MessageItem",
  props: {
    message: {
      type: Object,
      required: true
    },
    items: {
        required: true
    }
  },
  methods: {
    printFullDate: function(date){
      return moment(date).format("ddd MMM DD, [at] HH:mm a");
    },
    delItem(message){
        this.items.splice(message, 1);
        let id_item = message.id
        axios.delete(process.env.VUE_APP_API_LOCAL_HOST + '/api/message-detail/' + id_item + '/').then(response => {

        }).catch(error => {
            console.log(error)
        })
    }
  },
}
</script>

<style scoped>
.del-item{
    cursor: pointer;
    color: red;
}
</style>