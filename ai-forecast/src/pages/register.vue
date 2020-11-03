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

              <q-input square clearable 
              v-model="email" 
              type="email" 
              label="E-mail">

                <template v-slot:prepend>
                  <q-icon name="email" />
                </template>
              </q-input>

              <q-input square clearable 
              v-model="password" 
              type="password" 
              label="Password">

                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>    
              </q-input>

              <q-input square clearable 
              v-model="password1" 
              type="password" 
              label="one more time">
                <template v-slot:prepend>
                  <q-icon name="lock" />    
                </template>
              </q-input>

            </q-form>
          </q-card-section>

          <q-card-actions class="q-pa-md q-gutter-sm">

            <q-btn 
            label="가입하기" 
            color="primary"
            @click="alert"
            type="submit" />

            <q-btn label="뒤로" 
            color="primary" 
            to="/login" /> 

            <q-dialog 
            >
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
import { LocalStorage } from "quasar";
 
export default {
  name: 'register',
    data () {
      return {
        email: '',
        password: '',
        password1:'',
        user: {}
      }
    },
  methods: {
    alert () {
        if (this.password == "") {
          
          this.$q.dialog({
          title: 'Alert',
          message: '비밀번호를 입력해주세요!'

          }).onOk(() => {
            // console.log('OK')
          }).onCancel(() => {
            // console.log('Cancel')
          }).onDismiss(() => {
            // console.log('I am triggered on both OK and Cancel')
          })
       }
    
        // else if {
        //   this.$q.dialog({
        //     title: 'Alert',
        //     message: '비밀번호를 입력해주세요!'
        // }

        else if (this.password == this.password1) {
          
          this.$q.dialog({
          title: '가입 성공!',
          message: '가입되었습니다!'
          
          }).onOk(() => {
            // console.log('OK')
          }).onCancel(() => {
            // console.log('Cancel')
          }).onDismiss(() => {
            // console.log('I am triggered on both OK and Cancel')
          })

          const user = {
            email: this.email,
            password: this.password
          };

          LocalStorage.set("user", user);
          location.href="http://localhost:8080/#/login";
        }

        else {
          this.$q.dialog({
          title: 'Alert',
          message: '비밀번호를 확인해주세요!'

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
