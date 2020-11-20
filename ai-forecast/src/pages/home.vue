<template>
  <main
    class="q-page q-pa-sm"
    style="min-height: 500px;"
  >

  <div class="row q-col-gutter-sm q-py-xl content-center items-center justify-evenly" style = "padding: 180px 3px 80px 3px;">
    <ul>
    <text-effect-1 ></text-effect-1>
    </ul>
  </div>

    <div class="row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly">

        <q-btn
          rounded
          standout
          color="Navigator"
          label="Start"
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
</style>