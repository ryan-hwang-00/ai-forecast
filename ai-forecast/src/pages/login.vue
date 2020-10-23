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

          <q-card-actions class="q-pa-md">
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
export default {
  name: 'Login',
  data () {
    return {
      email: "",
      password: ""
      }
  },
  methods :{
    userCheck() {
      if (this.email == "NG" & this.password == '1111') {
        location.href="http://localhost:8080/#/store";
    }
  }
}
}
</script>
