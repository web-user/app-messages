<template>
<section style="background-color: #eee;">
  <div class="container py-5">

    <div class="row">
      <div class="col-md-12 col-lg-12 col-xl-12">

        <div class="container">
        <div class="wraper bootstrap snippets bootdeys bootdey">
            <div class="page-title">
                <h3 class="title">Inbox</h3>
            </div>

            <div class="row">
                <!-- Left sidebar -->
                <div class="col-md-3">
                    <div class="panel panel-default p-0  m-t-20">
                        <div class="panel-body p-0">
                            <div class="list-group no-border mail-list">
                                <a v-for = "(tab, index) in tabs" :key="index" class="list-group-item" @click="getMail(tab)" v-bind:class="{ 'active' : tab === active_tab }">
                                    {{ tab }}
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- End Left sidebar -->

                <!-- Right Sidebar -->
                <div class="col-md-9">
                    <div class="panel panel-default m-t-20">
                        <div class="panel-body">
                            <table class="table table-hover mails">
                                <tbody>
                                  <message-item v-for="message in messages" :message="message" :items="messages"/>
                                </tbody>
                            </table>

                        </div> <!-- panel body -->
                    </div> <!-- panel -->
                </div> <!-- end Col-9 -->

            </div><!-- End row -->


        </div>
        </div>


        <SubmitMessage />

      </div>

    </div>

  </div>
</section>
</template>

<script>
import axios from 'axios'

import MessageItem from "@/components/MessageItem";
import SubmitMessage from "@/components/SubmitMessage";
export default {
  name: "Chat",
    components: {MessageItem, SubmitMessage},
    data(){
        return{
            messages: [],
            isActive: 'inbox',
          active_tab: "inbox",
          tabs: ["inbox", "sent"]
        }
    },
    mounted(){
      this.getMessages()
    },
    methods: {
        getMessages(e){
          // get me data
            let isActive = this.active_tab
            axios.get(process.env.VUE_APP_API_LOCAL_HOST + '/api/'+ isActive +'-messages-list/').then(response => {
                console.log(response)
                this.messages = response.data

            }).catch(error => {
                console.log(error)
                if (error.response.status === 403){
                    this.$router.push('/login')
                }
            })

        },
        getMail(name){
            this.active_tab = name
            this.getMessages()
            console.log(name)
        }
  }

}
</script>

<style scoped>

.list-group-item.active, .list-group-item.active:hover, .list-group-item.active:focus {
   background-color: #ddd;
  border-color: #ddd;
  color: #444;
    z-index: 2;
}

.list-group-item,.list-group-item:first-child ,.list-group-item:last-child  {
    border-radius: 0px;
    padding: 12px 20px;
}

.list-group-item-heading {
    font-weight: 300;
}
.list-group-item.active>.badge, .nav-pills>.active>a>.badge {
    color: #3bc0c3;
}
.list-group-item.active .list-group-item-text, .list-group-item.active:focus .list-group-item-text, .list-group-item.active:hover .list-group-item-text {
    color: #3bc0c3;
}
.m-t-40 {
    margin-top: 40px !important;
}
.panel{
    padding: 20px 30px;
    border: none;
    border-top: 1px solid #ddd;
    margin-bottom: 20px;
    box-shadow: none;
}
.panel .panel-body{
    padding: 0px;
    padding-top: 20px;
}
.panel .panel-body p{
    margin: 0px;
}
.panel .panel-body p+p {
    margin-top: 15px;
}
.panel-default > .panel-heading {
    background-color: #FFFFFF;
    border-color: #DDDDDD;
    color: #797979;
}
.panel-heading {
    border-color:#eff2f7 ;
    font-size: 16px;
    padding: 0;
    padding-bottom: 15px;
}
.panel-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 0;
    margin-top: 0;
}
.panel-footer {
    margin: 0px -30px -30px;
    background: #eee;
    border-top: 0px;
}
.panel-group .panel .panel-heading {
padding-bottom: 0;
border-bottom: 0;
}
.panel-group .panel {
margin-bottom: 0;
border-radius: 0;
}
.m-t-20 {
    margin-top: 20px;
}
</style>