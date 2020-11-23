<template>
  <q-layout view="hHh LpR fff">
    <q-header bordered="bordered" class="bg-primary text-white" height-hint="98">
      <div class="fit column inline justify-between">
        <q-toolbar class="fit column inline justify-between" height="70px">
          <!-- 로고 -->
         <q-toolbar-title class = "col absolute-left">
            <q-btn flat to="/">
              <img id="image_large" src="~assets/Logo-white.png" height="40px" alt="" class="img-responsive"/>
              <img id="image_small" src="~assets/Logo-layout.png" height="25px" alt="" class="img-responsive"/>
            </q-btn>
          </q-toolbar-title>
          <!-- 로그인/회원가입 -->
          <q-tabs class="col self-end">
            <q-route-tab to="/register" label="회원가입" style="max-width: 70px; height: 85px;"/>
            <!-- <q-separator vertical inset color="white"/> -->
            <q-route-tab to="/login" label="로그인" style="max-width: 70px"/>
          </q-tabs>
        </q-toolbar>

        <q-drawer
          v-model="drawer"
          show-if-above="show-if-above"
          content-class="bg-grey-4"
          :width="350"
          :breakpoint="444"
          >
          <div class="fit column content-center" style = "padding: 10px 10px 2px 10px;">
            <q-btn
              standout
              color="primary"
              size="15px" 
              style="width : 300px"
              label="예측정보 정의"
              to="/predict_variables"
            />
            <br>
            <q-btn
              standout
              color="primary"
              size="15px" 
              style="width : 300px"
              label="예측결과 조회"
              to="/Predict"
            />
            <br>
            <span class="text-h6 text-dark">조회조건</span>
            <q-table
              :data="NavigatorData"
              :columns="NavigatorColumns"
              row-key="attribute"
              hide-header
              hide-bottom
              :pagination.sync="NavigatorPagination"
              class= "q-pa-md"
              style = "padding: 7px 1px 7px 1px;"
            />
          </div>

          <q-tabs
            no-caps="no-caps"
            active-color="primary"
            indicator-color="transparent"
            class="text-grey absolute-bottom"
          >
            <div class="fit row justify-center">
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
                height='30px'>
              </eva-icon>

              <eva-icon
                class='q-pa-md'
                name="car"
                animation="pulse"
                fill="#1D2758"
                width='30px'
                height='30px'>
              </eva-icon>
            </div>
          </q-tabs>
        </q-drawer>
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
import { LocalStorage } from "quasar";
import Predict from '../pages/Predict.vue'
import predict_variables from '../pages/predict_variables.vue'
import EventBus from '../components/eventBus.js';

export default { 
    data () {
      return {
        drawer: false,
        togithubpage: function() {
        location.href="https://github.com/ryan-hwang-00/ai-forecast"
        },
        NavigatorColumns: [
        {
          name: 'attribute',
          required: true,
          align: 'left',
          field: 'attribute',
          sortable: true,
          // classes: 'bg-grey-2 ellipsis',
          // headerClasses: 'bg-grey-2 ellipsis'
        },
        {
          name: 'Value',
          align: 'right',
          field: 'Value',
          sortable: true
        }
        ],
        NavigatorData: [
          {
            attribute: "기준일",
            Value: LocalStorage.getItem("date"),
          },
          {
            attribute: "매장명",
            Value: '',
          },
          {
            attribute: "상품명",
            Value: '',
          },
          {
            attribute: "휴일 구분",
            Value: '',
          },
          {
            attribute: "행사 구분",
            Value: '',
          },
          {
            attribute: "대량 주문",
            Value: '',
          }
        ],
        NavigatorPagination: {
          // sortBy: 'desc',
          // descending: false,
          page: 1,
          rowsPerPage: 6,
          // rowsNumber: 10
        },
      }
    },

    created() {
      // console.log('NavigatorData', this.NavigatorData)
      EventBus.$on("pushData_1", payload => {
        console.log('payload', payload);
        this.NavigatorData[1].Value = payload;
      },
    );
      EventBus.$on("pushData_2", payload => {
        console.log('payload', payload);
        this.NavigatorData[1].Value = payload;
      },
    );
      EventBus.$on("product_bus", bus_product => {
        console.log('product_bus>>>>>', bus_product);
        this.NavigatorData[2].Value = bus_product;
    });

        EventBus.$on("event_bus", bus_event => {
        console.log('event_bus>>>>>', bus_event);
        this.NavigatorData[4].Value = bus_event;
    });

        EventBus.$on("break_bus", bus_break => {
        console.log('break_bus>>>>>', bus_break);
        this.NavigatorData[3].Value = bus_break;
    });

        EventBus.$on("special_order_bus", bus_special_order => {
        console.log('special_order_bus>>>>>', bus_special_order);
        this.NavigatorData[5].Value = bus_special_order;
    });

    
  },
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