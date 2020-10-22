<template>
  <main class="q-page q-pa-sm" style="min-height: 704px;">
    <br/>
    <br/>
    <div class="row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly" >
      <q-btn color="yellow-10"
      clickable
       @click="onItemClickStore1"
       to="/item">
        <q-icon left size="5em" name="store" /> 
        <div>store 1</div>
      </q-btn>
      <q-btn q-btn color="pink"
      clickable
       @click="onItemClickStore2"
       to="/item">
        <q-icon left size="5em" name="store" /> 
        <div>store 2</div>
      </q-btn>  
      <!-- <q-btn color="yellow-10" icon-right="store" label="store 1" />
      <q-btn color="pink" icon-right="store" label="store 2" /> -->
    </div> 
  </main>
</template>

<script>

import axios from "axios";
 
export default {
  name: "store",
  data() {
    return {
    store1: "",
    store2: "",
    };
  },
  methods: {
    onItemClickStore1() {
      console.log("store1");
      this.bread = "store1";
    },
    onItemClickStore2() {
      console.log("store2");
      this.fruits = "store2";
    },
    onBackEndSendClick() {
      const data = {
        'store1': this.store1,
        'store2': this.store2,
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