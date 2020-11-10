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
        style = "width: 50vw; height: 500px;"
      >
      
        <gmap-marker
            :key="index"
            v-for="(m, index) in markers"
            :position="m.position"
            :clickable="true"
            :draggable="false"
            @click ="tostore"
        >
        </gmap-marker>

      </gmap-map>
    </div>
  </q-page>
</template>

<script>
import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps';


Vue.use (VueGoogleMaps, {
  load: {
    key: 'AIzaSyBfy54pwwjGG5iOkxtMPNnU-bHiq49zIEw',
    libraries: 'places'
  }
})


export default {
  name: 'PageIndex',
  data () {
    return {

      CustomMarker: null,

      center: {
        lat: 36,
        lng: 127
      },

      zoom: 7,
    
      markers:[{
        position: {lat: 35.1028, lng: 129.0403}
      }, {
        position: {lat: 127.269311, lng: 37.413294}
      }]

    }
  },

  methods : {

    tostore: function() {
       {location.href="http://localhost:8080/#/store";
      
          this.$q.dialog({
          title: 'Congratulation!',
          message: '포커머신에 오신 것을 환영합니다!'
        
          }).onOk(() => {
            // console.log('OK')
          }).onCancel(() => {
            // console.log('Cancel')
          }).onDismiss(() => {
            // console.log('I am triggered on both OK and Cancel')
          })
      }
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