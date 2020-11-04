<template>
  <q-page class="bg-light-white window-height window-width row justify-center items-center">
    <div class="column">
      <div class="row q-col-gutter-sm content-center items-center justify-evenly">
        <h5 class="full-width">Login</h5>
      </div>
      <div class="row">
        <q-card square bordered class="q-pa-lg shadow-1">
          <q-card-section>
            <q-form 
            class="q-gutter-md">

              <q-input square filled clearable 
              v-model="email"
              :rules="[val => val && val.length > 0  ||  'e-mail is wrong!']"
              type="e-mail" 
              label="e-mail" />

              <q-input square filled clearable 
              v-model="password" 
              type="password" 
              :rules="[val => val && val.length > 0  ||  'password is wrong!']"
              label="password" />

            </q-form>
          </q-card-section>

          <q-card-actions 
          class="q-pa-md">
           
            <q-btn
            push
            unelevated color="blue" 
            type="submit"
            size="lg" 
            class="full-width"
            @click="userCheck"
            label = 'login'/>
          </q-card-actions>

          <q-card-section class="text-center q-pa-none" >
            <p class="text-grey-10">If you are not registered, please register first</p>
            <q-btn rounded standout  
            label="회원가입" 
            to="/register" />
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import { LocalStorage } from "quasar";

export default {
  name: 'Login',
  data () {
    return {

      email: "",
      password: ""
      
      }
  },

  methods : {

    userCheck: function() {
      const user = LocalStorage.getItem("user");

      if (this.email == user.email & this.password == user.password) {
        location.href="http://localhost:8080/#/store";
      
          this.$q.dialog({
          title: 'Congratulation!',
          message: '포커머신에 오신 것을 환영합니다!'
        
          }).onOk(() => {
            // console.log('OK')
          }).onCancel(() => {
            // console.log('Cancel')
          }).onDismiss(() => {
            // console.log('I am triggered on both OK and Cancel')
          })
      }

      else if (this.email == '' & this.password == '') {
          this.$q.dialog({
          title: 'Alert',
          message: '정보를 입력해주세요!'

          }).onOk(() => {
            // console.log('OK')
          }).onCancel(() => {
            // console.log('Cancel')
          }).onDismiss(() => {
            // console.log('I am triggered on both OK and Cancel')
          })    
      }

      else  {
          this.$q.dialog({
          title: 'Alert',
          message: '회원이 아닙니다!'

        }).onOk(() => {
          // console.log('OK')
        }).onCancel(() => {
          // console.log('Cancel')
        }).onDismiss(() => {
          // console.log('I am triggered on both OK and Cancel')
        })    
    }
  }
}
}

</script>