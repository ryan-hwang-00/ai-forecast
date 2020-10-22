<template>
  <q-page
    class="window-height window-width row justify-center items-center"
    style="background: linear-gradient(white, white);"
  >
    <div class="column q-pa-lg">
      <div class="row">
        <q-card square class="shadow-24" style="width:300px;height:485px;">
          <q-card-section class="bg-primary">
            <h4 class="text-h5 text-white q-my-md">Registration</h4>
            <div class="absolute-bottom-right q-pr-md" 
                 style="transform: translateY(50%);">
            </div>
          </q-card-section>

          <q-card-section>
            <q-form class="q-px-sm q-pt-xl q-pb-lg">
              <q-input square clearable v-model="email" 
              type="email" label="E-mail">

                <template v-slot:prepend>
                  <q-icon name="email" />
                </template>
              </q-input>

              <q-input square clearable v-model="username" 
              type="username" label="ID">
                <template v-slot:prepend>
                  <q-icon name="person" />
                </template>
              </q-input>

              <q-input square clearable v-model="password" 
              type="password1" label="Password">
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>    
              </q-input>

              <q-input square clearable v-model="password" 
              type="password2" label="1 more time">
                <template v-slot:prepend>
                  <q-icon name="lock" />    
                </template>
              </q-input>

            </q-form>
          </q-card-section>

          <q-card-actions class="q-pa-md q-gutter-sm">
            <q-btn label="가입하기" color="primary" type="submit" />
            <q-btn label="뒤로" flat class="q-ml-sm" color="primary" to="/login" /> 

              <q-dialog
              v-model="small">
              <q-card style="width: 300px">
                <q-card-section>
                  <div class="text-h6">완료</div>
                </q-card-section>

                <q-card-section class="q-pt-none">
                  가입이 완료되었습니다.
                </q-card-section>

                <q-card-actions align="right" class="bg-white text-teal">
                  <q-btn flat label="OK" v-close-popup />
                </q-card-actions>
              </q-card>
            </q-dialog>

          </q-card-actions>

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

      email: '',
      username: '',
      password: '',

      small: false,
      medium: false,
      fullWidth: false,
      fullHeight: false
    }
  }
}
</script> 


<style lang='sass'>
    .q-px-lg
        .block
            font-size : 17px
</style>