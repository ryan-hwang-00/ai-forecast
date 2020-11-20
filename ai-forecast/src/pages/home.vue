<template>
  <main
    class="q-page q-pa-sm"
    style="min-height: 704px;"
  >

  <div class="row q-col-gutter-sm q-py-xl content-center items-center justify-evenly">
    <ul>
    <text-effect-1 ></text-effect-1>
    </ul>
  </div>

    <div class="row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly">

        <q-btn
          rounded
          standout
          color="pink-9"
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