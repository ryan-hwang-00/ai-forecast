<template>

  <div class="q-pa-md">

    <div
      class="q-gutter-md"

      style="max-width: 300px"
    >

      <q-input
        v-model="textSetLocal"
        label="로컬 스토리지에 데이터 저장"
      />

      <q-btn
        color="white"
        text-color="black"
        label="로컬 스토리지에 데이터 저장"

        @click="setLocalStorage()"

      />

      <q-input

        filled
        v-model="textGetLocal"
        label="로컬 스토리지에서 데이터 가져오기"
      />

      <q-btn
        color="white"
        text-color="black"
        label="로컬 스토리지에서 데이터 가져오기"
        @click="getLocalStorage()"

      />

      <!--

      <q-input

        outlined

        v-model="textSetJson"

        label="Outlined"

      />

      -->

      <q-btn

        color="white"
        text-color="black"
        label="JSON 데이터를 로컬 스토리지 등록"
        @click="setMultiLocalStorage()"
      />



      <q-input
        standout
        v-model="textGetJson"
        label="JSON 데이터를 로컬 스토리지에서 가져오기"
      />
      <q-btn
        color="white"
        text-color="black"
        label="JSON 데이터를 로컬 스토리지에서 가져오기"
        @click="getMultiLocalStorage()"
      />



      <q-input
        standout="bg-teal text-white"
        v-model="textGetJsonSingle"
        label="데이터 중 하나 가져오기"
      />
      <q-btn
        color="white"
        text-color="black"
        label="데이터 중 하나 가져오기"
        @click="getMultiSingleLocalStorage()"
      />



      <q-input
        standout="bg-teal text-white"
        v-model="axiosGetData"
        label="axios 데이터 가져오기"
      />
      <q-btn
        color="white"
        text-color="black"
        label="axios 데이터 가져오기"
        @click="getAxios()"
      />


      <q-input
        standout="bg-teal text-white"
        v-model="axiosPostResponseData"
        label="axios post"
      />

      <q-btn
        color="white"
        text-color="black"
        label="axios post"
        @click="postAxios()"
      />

    </div>
  </div>
</template>

<script>
import { LocalStorage } from "quasar";
import axios from "axios";

export default {
  data () {
    return {
      textSetLocal: '',
      textGetLocal: '',
      textSetJson: {},
      textGetJson: {},
      textGetJsonSingle: '',
      textBorderless: '',
      axiosGetData: {},
      axiosPostResponseData: {}
    }
  },

  methods: {
    // save single data 
    setLocalStorage: function () {

      console.log('textSetLocal', this.textSetLocal)
      LocalStorage.set("textSetLocal", this.textSetLocal);
      // LocalStorage.set('user', 'user')

    },

    // get single data

    getLocalStorage: function () {

      this.textGetLocal = LocalStorage.getItem("textSetLocal");

    },

    // save multi data (JSON)

    setMultiLocalStorage: function () {

      this.textSetJson = {

        a: 40,
        b: 30,
        c: 700,
        d: 200,
        e: 4200,
        f: 220,
        g: 1000

      }

      LocalStorage.set("textSetJson", this.textSetJson);

    },

    // get multi data(JSON)

    getMultiLocalStorage: function () {

      //json to string 형태로 변환
      this.textGetJson = JSON.stringify(LocalStorage.getItem("textSetJson"));
      console.log(this.textGetJson)

    },

    // get multi data(JSON)


    getMultiSingleLocalStorage: function () {

      const data = LocalStorage.getItem("textSetJson")
      this.textGetJsonSingle = data.a;

      console.log(JSON.stringify(LocalStorage.getItem("textSetJson")['a']));

    },


    // axios get data
    getAxios: function () {

      axios.get('https://reqres.in/api/users/2')
        .then((response) => {
          this.axiosGetData = JSON.stringify(response.data)

        })

    },

    // axios post data

    postAxios: function () {

      const data = {

        "horizon": "7",

      }

      axios.post('http://127.0.0.1:3000/api/v3.0/forecast/sales', 

      data
      
      ).then(response => {

        console.log(response)
        
        this.axiosPostResponseData = JSON.stringify(response.data)
        LocalStorage.set("axiosJSON", this.axiosPostResponseData)

      }).catch((ex) => {

        console.warn("ERROR!!!!! : ", ex)

      })

    },

  }

}


</script>

