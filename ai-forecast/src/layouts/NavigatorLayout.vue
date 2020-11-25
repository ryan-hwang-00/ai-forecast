
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

        <q-drawer
          v-model="drawer"
          show-if-above="show-if-above"
          content-class="bg-grey-4"
          :width="350"
          :breakpoint="444"
          >

          <div class="fit column content-center" style = "padding: 30px 10px 2px 10px;">

            <q-btn
              standout
              color="primary"
              size="18px" 
              style="width : 300px"
              label="예측정보 정의"
              to="/predict_variables"
            />
            <br>

            <q-btn
              standout
              color="primary"
              size="18px" 
              style="font:'Wemakeprice-Regular'; width : 300px;"
              label="예측결과 조회"
              to="/Predict"
            />
            
            <br>
            <span 
              class="text-h6 text-dark"
              style="padding: 40px 0px 0px 0px;"
            >조회조건</span>

            <q-table
              :data="NavigatorData"
              :columns="NavigatorColumns"
              row-key="attribute"
              hide-header
              hide-bottom
              :pagination.sync="NavigatorPagination"
              class="text-left"
              style="padding: 1px 1px 1px 1px;"
            />
            
          </div>

            <div
              class="row q-ma-none text-grey absolute-bottom row justify-center"
            ><h6.5>ⓒ Team NEOGURI</h6.5>
            </div>

        <!-- <div
          class='row q-col-gutter-sm content-center items-center justify-evenly row justify-center'></div>
          <q-tabs
            no-caps="no-caps"
            active-color="primary"
            indicator-color="transparent"
            class="text-grey absolute-bottom"
          >

            <div class="fit row justify-center">

              <eva-icon
              class='q-pa-xs' 
              name="github" 
              animation='pulse' 
              fill="#1D2758"
              width='30px'
              height='30px'
              @click='togithubpage'
              style = "padding: 1px 15px 1px 15px;">
            </eva-icon>

            <eva-icon
              class='q-px-xs' 
              name="facebook" 
              animation="pulse" 
              fill="#1D2758"
              width='30px'
              height='30px'
              style = "padding: 1px 15px 1px 15px;"
            >
            </eva-icon>

            <eva-icon
              class='q-pa-xs' 
              name="car"
              animation="pulse" 
              fill="#1D2758"
              width='30px'
              height='30px'
              style = "padding: 1px 15px 1px 15px;"
            >
            </eva-icon>

            <div
              class="row q-ma-none content-center items-center row justify-center"
            ><h6.5>ⓒ Team NEOGURI</h6.5>
            </div>

            </div>
          </q-tabs> -->
        </q-drawer>
      </div>
    </q-header>
    
    <q-page-container class='bg-grey-1'>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
import { LocalStorage } from "quasar";
import Predict from '../pages/Predict.vue'
import predict_variables from '../pages/predict_variables.vue'
import EventBus from '../components/eventBus.js';
import Vue from "vue";

Vue.component('child', {
  // props 정의
  props: ['message'],
  // 데이터와 마찬가지로 props는 템플릿 내부에서 사용할 수 있습니다
  // data 속성에서 사용할 땐 vm => ({vm.message})로 사용할 수 있습니다.
  template: '<span>{{ message }}</span>'
})

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
            Value: '2019-12-01',
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


      EventBus.$on("Date_bus", bus_date => {
        console.log('Date_bus', bus_date);
        this.NavigatorData[0].Value = bus_date;
      },
    );

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

.text-h6 {
  font-family: 'Wemakeprice-Regular';
}

.text-left {
  font-family: 'Jua';
  font-size: 15px;
  padding: 2px 2px;
}

.q-btn {
  font-size: 34px;
}


.q-table tbody td {
    font-size: 16px;
}

</style>