<template>
  <q-layout view="hHh LpR fff">
    
    <q-header bordered class="bg-primary text-white " height-hint="98">

      <q-toolbar class="fit column inline justify-between" height="70px">

          <!-- 로고 -->
         <q-toolbar-title 
         class = "col absolute-left"    
         >

          <q-btn flat to="/">
            <img id="image_large" src="~assets/Logo-white.png" height="40px" alt="" class="img-responsive"/>
            <img id="image_small" src="~assets/Logo-layout.png" height="25px" alt="" class="img-responsive"/>
          </q-btn>

        </q-toolbar-title>
          <!-- 로그인/회원가입 -->
          <q-tabs class="col self-end">
            <q-route-tab 
              to="/register" 
              label="회원가입" 
              style="padding: 18px 5px; max-width: 70px; height: 85px;"/>
            <!-- <q-separator vertical inset color="white"/> -->
            <q-route-tab 
              to="/login" 
              label="로그인" 
              style="padding: 18px 5px; max-width: 70px; height: 85px;"/>
          </q-tabs>
        </q-toolbar>
    </q-header>
    
    <q-page-container class='bg-grey-1'>
      <router-view />
    </q-page-container>


    <q-footer 
      class="q-page q-pa-sm bg-grey-4 text-primary">
      
        <div 
          class="row q-col-gutter-sm content-center items-center justify-evenly row justify-center"
          style = "padding: 0px 0px 0px 10px;"
        >

          <q-tabs 
            no-caps active-color="primary" 
            indicator-color="transparent" 
            class="content-center text-grey"
            style="padding:1px 1px 1px 1px"
          >

            <eva-icon
              class='q-pa-xs' 
              name="github" 
              animation='pulse' 
              fill="#1D2758"
              width='40px'
              height='40px'
              @click='togithubpage'
              style="padding: 10px 10px 1px 10px;">
            </eva-icon>

            <eva-icon
              class='q-px-xs' 
              name="facebook" 
              animation="pulse" 
              fill="#1D2758"
              width='40px'
              height='40px'
              style = "padding: 10px 20px 1px 17px;"
            >
            </eva-icon>

            <eva-icon
              class='q-pa-xs' 
              name="car"
              animation="pulse" 
              fill="#1D2758"
              width='40px'
              height='40px'
              style="padding: 10px 10px 1px 10px;"
            >
            </eva-icon>

          </q-tabs>
        </div>
 
        <div
          class="row q-ma-none content-center items-center justify-evenly"
        ><h6.5>ⓒ Team NEOGURI</h6.5>
       </div>
      

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


@font-face {
    font-family: 'Jua';
    src: url(../assets/Jua-Regular.ttf);
}

@font-face {
    font-family: 'Wemakeprice-Regular';
    src: url(../assets/Wemakeprice-Regular.ttf);
 
}

.q-tab {
  font-size: 30px;
  font-family: 'Jua';
 
  line-height: 4px;
  font-weight: 100;
}

.q-tab__label {
    font-size: 20px;
    line-height: 14px;
    font-weight: 500;
}

.q-btn {
  font-size: 34px;
}

</style>