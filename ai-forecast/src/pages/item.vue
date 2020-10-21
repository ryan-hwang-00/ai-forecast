<template>
  <main class="q-page q-pa-sm" style="min-height: 704px;">
    <br/>
    <br/>
    <div class="row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly" >

      <q-btn
      clickable
      @click="onItemClickBread"
      to="/predict_variables">
       <img src="~assets/bread.png" height="100px">
      </q-btn>

      <q-btn
      clickable
      @click="onItemClickFruits"
      to="/predict_variables">
       <img src="~assets/fruits.png" height="100px">
      </q-btn>

      <q-btn
      clickable
      @click="onItemClickMineralWater"
      to="/predict_variables">
       <img src="~assets/mineral-water.png" height="100px">
      </q-btn>

    </div>

    <div class="row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly" >

      <q-btn
      clickable
      @click="onItemClickRamen"
      to="/predict_variables">
       <img src="~assets/ramen.png" height="100px">
      </q-btn>

      <q-btn
      clickable
      @click="onItemClickSausages"
      to="/predict_variables">
       <img src="~assets/sausages.png" height="100px">
      </q-btn>

    </div>
  </main>
</template>
<script>

export default {
  data () {
    return {
  }
  },
  methods: {
    onItemClickBread () {
      console.log('bread')
    },
    onItemClickFruits () {
      console.log('fruits')
    },
    onItemClickMineralWater () {
      console.log('mineral-water')
    },
    onItemClickRamen () {
      console.log('ramen')
    },
    onItemClickSausages () {
      console.log('sausages')
    }
  }
}
</script>