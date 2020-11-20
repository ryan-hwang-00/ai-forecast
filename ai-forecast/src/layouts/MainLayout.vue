<template>
  <q-layout view="hHh LpR fff">
    
    <q-header bordered class="bg-primary text-white" height-hint="98">
      <div class="fit column inline justify-between">
        <q-toolbar>
          <!-- 로고 -->
          <q-toolbar-title class = "col absolute-top-left">
            <q-btn to="/">
              <img id="image_large" src="~assets/Logo-large.png" height="98px" alt="" class="img-responsive"/>
              <img id="image_small" src="~assets/Logo-medium.png" height="50px" alt="" class="img-responsive"/>
            </q-btn>
          </q-toolbar-title>
        </q-toolbar>
        <!-- 로그인/회원가입 -->
        <q-tabs class="col self-end">
          <q-route-tab to="/register" label="회원가입" style="max-width: 100px"/>
          <q-separator vertical inset color="white"/>
          <q-route-tab to="/login" label="로그인" style="max-width: 100px"/>
        </q-tabs>
      </div>
    </q-header>
    
    <q-page-container class='bg-grey-1'>
      <router-view />
    </q-page-container>

    <q-footer
      bordered class="bg-grey-4 text-primary"
    >

      <q-toolbar
        class="q-pa-md justify-center"
      >

        <q-tabs 
          no-caps active-color="primary" 
          indicator-color="transparent" 
          class="text-grey" 
          v-model="tab"
        >

          <eva-icon
            class='q-pa-md center' 
            name="github" 
            animation="pulse" 
            fill="#1D2758"
            width='30px'
            height='30px'
            @click='togithubpage'
            style="font-size:3px">
          </eva-icon>

          <eva-icon
            class='q-pa-md center' 
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

      </q-toolbar>
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