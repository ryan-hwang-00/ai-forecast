<template>
  <q-page class="bg-light-white window-height window-width row justify-center items-center">
    <div class="column">
      <div class="row">
        <h5 class="text-h5 text-white q-my-md">FORCA Machine</h5>
      </div>
      <div class="row">
        <q-card square bordered class="q-pa-lg shadow-1">
          <q-card-section>
            <q-form class="q-gutter-md">
              <q-input square filled clearable v-model="ID" type="ID" label="ID" />
              <q-input square filled clearable v-model="password" type="password" label="password" />
            </q-form>
          </q-card-section>
          <q-card-actions class="q-pa-md">
            <q-btn unelevated color="blue" size="lg" class="full-width" label="Login" />
          </q-card-actions>
          <q-card-section class="text-center q-pa-none" >
            <p class="text-grey-10">If you are not registered, please register first</p>
            <q-btn rounded standout v-model=text label="회원가입" to="/register" />
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
      ID : '',
      password : ''
    }
  }
}  
</script>

<style>
.q-card {
  width: 400px;
}
</style>