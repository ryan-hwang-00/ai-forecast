<template>
  <q-layout view="hHh LpR fff">
    <q-header bordered class="bg-primary text-white" height-hint="98">
      <div class="fit column inline justify-between">
        <q-toolbar>
          <q-toolbar-title
            class ="col absolute-top-left">
          
            <q-drawer
              v-model="drawer"
              show-if-above
              :width="200"
              :breakpoint="400"
            >

            <q-scroll-area 
              bordered class="bg-grey-4 text-primary"
              style="height: calc(100% - 150px); margin-top: 150px; border-right: 1px solid #ddd">

              <q-list
              class='q-gutter-md'
              padding>

                <q-card
              
                  flat bordered
                  class="col-auto bg-grey-4"
                  >

                  <q-card-section>
                    <div class="text-h6">예측결과 조회조건</div>
                  </q-card-section>

                  <q-separator inset />

                  <q-card-section>

          
                    
                    <div class="text-subtitle2">기 준 일  : </div>
                    <div class="text-subtitle2">매    장  : {{ store_name }} </div>
                    <div class="text-subtitle2">상    품  : 신라면</div>
                    <div class="text-subtitle2">할인행사  : 월요일</div>
                    <div class="text-subtitle2">휴 무 일  : 일요일</div>

             
                  </q-card-section>
                </q-card>

              </q-list>
            </q-scroll-area>

            <q-img 
              bordered class="bg-grey-4 text-primary absolute-top"
              style="height: 150px">
              <div class="absolute-bottom bg-transparent">
                <q-avatar size="50px" class="q-mb-sm">
                  <img src="../assets/Logo.png">
                </q-avatar>
                
                <div class="text-black">TEAM NEOGURI</div>
                <div class="text-black">Navigator</div>
              </div>
            </q-img>
              
              <q-tabs 
                no-caps active-color="primary" 
                indicator-color="transparent" 
                class="text-grey absolute-bottom" 
            
              >
        
            <eva-icon
              class='q-pa-md' 
              name="github" 
              animation="pulse" 
              fill="#1D2758"
              width='30px'
              height='30px'
              @click='togithubpage'
              style="font-size:3px">
            </eva-icon>

            <eva-icon
              class='q-pa-md' 
              name="facebook" 
              animation="pulse" 
              fill="#1D2758"
              width='30px'
              height='30px'
            >
            </eva-icon>

            <eva-icon
              class='q-pa-md' 
              name="car" 
              animation="pulse" 
              fill="#1D2758"
              width='30px'
              height='30px'
              >
            </eva-icon>

          </q-tabs>
        </q-drawer>
           
          <q-btn to="/">
            <img id="image_large" src="~assets/Logo-large.png" height="98px" alt="" class="img-responsive"/>
            <img id="image_small" src="~assets/Logo-medium.png" height="50px" alt="" class="img-responsive"/>
          </q-btn>
            
          </q-toolbar-title>
        </q-toolbar>

        <q-tabs class="col-auto self-end">
          <q-route-tab to="/register" label="회원가입" style="max-width: 1000px"/>

          <q-separator vertical inset color="white"/>

          <q-route-tab to="/login" label="로그인" style="max-width: 1000px"/>
        </q-tabs>
      </div>

    </q-header>
    <q-page-container class='bg-grey-1'>

      <router-view />
    </q-page-container>

    <!-- <q-footer 
    bordered class="bg-grey-4 text-primary"
    >

      <q-tabs 
      no-caps active-color="primary" 
      indicator-color="transparent" 
      class="text-grey" 
      v-model="tab"
     
      >
        
        <eva-icon
        class='q-pa-md' 
        name="github" 
        animation="pulse" 
        fill="#1D2758"
        width='30px'
        height='30px'
        @click='togithubpage'
        style="font-size:3px">
        </eva-icon>

        <eva-icon
        class='q-pa-md' 
        name="facebook" 
        animation="pulse" 
        fill="#1D2758"
        width='30px'
        height='30px'
        >
        </eva-icon>

        <eva-icon
        class='q-pa-md' 
        name="car" 
        animation="pulse" 
        fill="#1D2758"
        width='30px'
        height='30px'
        >
        </eva-icon>

      </q-tabs>
    </q-footer> -->

  </q-layout>
</template>

<script>

import predict_variables from '../pages/predict_variables.vue';
import map from '../pages/map.vue';
import { LocalStorage } from "quasar";

export default { 

  data () {

    return {

      store_name: store_name1,
      drawer: false,
      leftDrawerOpen: false,
      essentialLinks: linksData
       
    },
      store_name1 = localStorage.getItem('store_name') 
      
  },  

  methods: {
    togithubpage: function() {
      location.href="https://github.com/ryan-hwang-00/ai-forecast"
    }
  }

}

</script>

<style scoped>
/* min-width = app->web */
@media (min-width: 600px){ 
    #image_large{
        display: block
    }
    #image_small{
        display: none
    }
}
/* max-width = web->app */
@media (max-width: 600px){ 
    #image_large{
        display: none
    }
    #image_small{
        display: block
    }
}
</style>

<!--
<template>

  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          Foreca Machine
        </q-toolbar-title>

        <div>FM v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          Essential Links
        </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksData = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev'
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev'
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev'
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev'
  }
];

export default {
  name: 'MainLayout',
  components: { EssentialLink },
  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData
    }
  }
}

</script>
-->