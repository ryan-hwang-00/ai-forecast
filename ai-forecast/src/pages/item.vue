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
import axios from "axios";
 
  export default {
    name: "item",
    data() {
      return {
      bread: "",
      fruits: "",
      mineralWater: "",
      ramen: "",
      sausages: ""
      };
    },
    methods: {
      onItemClickBread() {
        console.log("bread");
        this.bread = "bread";
      },
      onItemClickFruits() {
        console.log("fruits");
        this.fruits = "fruits";
      },
      onItemClickMineralWater() {
        console.log("mineral-water");
        this.mineralWater = "mineral-water";
      },
      onItemClickRamen() {
        console.log("ramen");
        this.ramen = "ramen";
      },
      onItemClickSausages() {
        console.log("sausages");
        this.sausages = "sausages";
      },
      onBackEndSendClick() {
        const data = {
          'fruits': this.bread,
          'bread': this.fruits,
          'mineralwater': this.mineralWater,
          'ramen': this.ramen,
          'sausages': this.sausages
        };
        console.log("data log=========", data);
        const returnData = axios
        .post(
        "http://localhost:8080/api/", // backend endpoint
        data,
        options
        )
        
        condole.log('returnData', this.returnData);
      }
    }
};

</script>