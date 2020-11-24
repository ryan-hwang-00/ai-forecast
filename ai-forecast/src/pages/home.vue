<template>
  <main
    class="q-page q-pa-sm"
    style="padding: 60px 3px 30px 3px; min-height: 500px;"
  >

    <div 
      class="row q-col-gutter-sm q-py-xl content-center items-center justify-evenly" 
      style = "padding: 120px 3px 80px 3px;">

      <ul>
      <text-effect-1 ></text-effect-1>
      </ul>
    </div>

    <div 
      class="row q-col-gutter-sm q-py-xl content-center items-center justify-evenly">

      <q-btn
        rounded
        standout
        class='text-a'
        color="primary"
        label="Start"
        style = "padding: 1px 0px 0px 0px;"
        to="/map"
        size="20px"
      />

    <!-- </q-card-section> -->
    </div>
  </main>
</template>

<script>
import TextEffect1 from '../components/textEffect/TextEffect1.vue'
import { colors } from 'quasar'

colors.setBrand('pink-9', '#456D91')

export default {
  name: "home",
  components: {
    TextEffect1
  }
}
</script>

<style>

.text-a {
  display: block !important;
  font-family: 'Jua';
}


</style>