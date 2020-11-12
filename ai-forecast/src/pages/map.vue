<template>
  <q-page class="bg-light-white window-width row justify-center items-center">
    <div class = 'column'>
    <div id = "app" square bordered class="text-grand-hotel text-weight-bolder">
        <h4>위치 선택!</h4>
    </div>

      <gmap-map
        class="justify-center items-center"
        :center = "center"
        :zoom = "zoom"
        :options = "options"
        style = "width: 60vw; height: 500px;"
      >
      
        <!-- <gmap-marker
            :key="index"
            v-for="(m, index) in markers" 
            :position="m.position"
            :clickable="true"
            :draggable="false"
            v-on:click= 'tostore1'
            :icon="{ url:require('../assets/blue-pushpin.png') }"
            > -->

          <gmap-marker
          :position="{lat: 35.1028, lng: 129.0403}"
          :clickable="true"
          :draggable="false"
          v-on:click= 'tostore1'
          :icon="{ url:require('../assets/blue-pushpin.png') }"
          ></gmap-marker>

          <gmap-marker
          :position="{lat: 33.35, lng: 126.28}"
          :clickable="true"
          :draggable="false"
          v-on:click= 'tostore2'
          :icon="{ url:require('../assets/blue-pushpin.png') }"
          ></gmap-marker>

          <gmap-marker
          :position="{lat: 37.487935, lng: 126.857758}"
          :clickable="true"
          :draggable="false"
          v-on:click= 'tostore3'
          :icon="{ url:require('../assets/blue-pushpin.png') }"
          >
        
          
        </gmap-marker>
      </gmap-map>
    </div>
  </q-page>
</template>

<script>

import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps';
import GmapCustomMarker from 'vue2-gmap-custom-marker';


Vue.use (VueGoogleMaps, {
  load: {
    key: 'AIzaSyBfy54pwwjGG5iOkxtMPNnU-bHiq49zIEw',
    libraries: 'places'
  }
})

const mapMarker = require('../assets/blue-pushpin.png');
export default {
  name: 'PageIndex',
  data () {
    return {

      CustomMarker: null,

      center: {
        lat: 36,
        lng: 127.5
      },

      zoom: 6.75,
      
      markers: [
        {
          position: {
            lat: 35.1028, 
            lng: 129.0403,
           
          }
        }
      ]
    }
  },

  methods : {

    tostore1: function() {

    console.log(this.markers[0].position.lat)
        location.href="http://localhost:8080/#/store"

        this.$q.dialog({
        title: '지역선택완료!',
        message: '부산의 매장입니다.'
      })
    },

    tostore2: function() {
  
        this.$q.dialog({
        title: '제주도',
        message: "서비스 준비중입니다."
    })
  },

    tostore3: function() {
  
        this.$q.dialog({
        title: '서울',
        message: "서비스 준비중입니다."
    })
  }
}
}

</script>
<style scoped>

body {
    margin: 0;
    padding: 0;
}

</style>