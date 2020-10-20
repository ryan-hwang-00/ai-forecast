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
            <div class="absolute-bottom-right q-pr-md" style="transform: translateY(50%);">
              <q-btn fab icon="close" color="black" />
            </div>
          </q-card-section>

          <q-card-section>
            <q-form class="q-px-sm q-pt-xl q-pb-lg">
              <q-input square clearable v-model="email" type="email" label="E-mail">
                <template v-slot:prepend>
                  <q-icon name="email" />
                </template>
              </q-input>

              <q-input square clearable v-model="username" type="username" label="ID">
                <template v-slot:prepend>
                  <q-icon name="person" />
                </template>
              </q-input>

              <q-input square clearable v-model="password" type="password1" label="Password">
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>    
              </q-input>

              <q-input square clearable v-model="password" type="password2" label="1 more time">
                <template v-slot:prepend>
                  <q-icon name="lock" />    
                </template>
              </q-input>
            </q-form>
          </q-card-section>

          <q-card-actions class="q-px-lg">
            <q-btn unelevated size="lg" color="blue" class="full-width text-5-white" label="회원가입완료" />
          </q-card-actions>

          <q-card-section class="text-center q-pa-sm">
            <p class="text-grey-6">Return to login</p>
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
      email: '',
      username: '',
      password: '',
    }
  }
}
</script>


<style lang='sass'>
    .q-px-lg
        .block
            font-size : 17px
</style>