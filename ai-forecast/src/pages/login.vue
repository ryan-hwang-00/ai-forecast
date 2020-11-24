<template>
  <q-page
    class="window-height window-width row justify-center items-center"
    style="background: linear-gradient(white, white);"
  >
    <div class="column q-pa-lg">
      <div class="row">

        <q-card 
          square class="shadow-24" 
          style="width:300px;height:485px;"
        >

          <q-card-section class="bg-primary">
            <h4 class="text-Gugi text-white q-my-md">Login</h4>
            <div class="absolute-bottom-right q-pr-md" 
                 style="transform: translateY(50%);">
            </div>
          </q-card-section>

          <q-card-section>
            <q-form 
            class="q-gutter-md">

              <q-input 
                square filled clearable 
                v-model="email"
                :rules="[val => val && val.length > 0  ||  'e-mail is wrong!']"
                type="e-mail" 
                label="e-mail" />

              <q-input 
                square filled clearable 
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
            unelevated color="primary" 
            type="submit"
            size="lg" 
            class="full-width"
            @click="userCheck"
            label = 'login'/>

          </q-card-actions>

          <q-card-section class="text-center q-pa-none" >
            <p class="text-grey-10" >If you are not registered, please register first</p>
              <q-btn 
                rounded standout 
                class = "text-bold" 
                label="register" 
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
        location.href="http://localhost:8080/#/map";
      
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

<style>

@font-face {
    font-family: 'Wemakeprice-Regular';
    src: url(../assets/Wemakeprice-Regular.ttf);
 
}

.text-Gugi {

  font-size: 30px;
  font-family: 'Wemakeprice-Regular';
 
  line-height: 4px;
  font-weight: 100;

}


</style>