<template>
  <q-layout view="hHh LpR fff">
    <q-header bordered class="bg-primary text-white" height-hint="98">
      
      <q-toolbar>
        <q-toolbar-title class = "absolute-top-left">

          <q-btn to="/">
            <img id="image_large" src="~assets/Logo-large.png" height="98px" alt="" class="img-responsive"/>
            <img id="image_small" src="~assets/Logo-medium.png" height="50px" alt="" class="img-responsive"/>
          </q-btn>
          
        </q-toolbar-title>
      </q-toolbar>


      <!-- <q-toolbar>
          <q-btn
            class="q-mr-sm"
            to="/"
            >
            <q-toolbar inset>
              <q-toolbar-title><strong>Foreca  </strong>  Machine</q-toolbar-title>
            </q-toolbar>
          </q-btn>
      </q-toolbar> -->

      <q-tabs align="right">
        <q-route-tab to="/register" label="회원가입" style="max-width: 100px"/>
        <q-separator vertical inset color="white"/>
        <q-route-tab to="/login" label="로그인" style="max-width: 100px"/>
      </q-tabs>

    </q-header>
    <q-page-container class='bg-grey-1'>

      <router-view />
    </q-page-container>

    <q-footer 
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
    </q-footer>

  </q-layout>
</template>

<script>
export default {  
    data () {
      return {
        togithubpage: function() {
        location.href="https://github.com/ryan-hwang-00/ai-forecast"
        }
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