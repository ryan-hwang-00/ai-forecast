<template>
  <main class="q-page q-pa-sm" style="min-height: 704px;">

    <div class="fit column content-center items-center justify-evenly"> <!-- div 1 -->
    
    

      <div class="fit row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly" style="max-width:1300px">  <!-- div 2 -->
        <!-- 상위 div에서 column의 content를 center 정렬하라고 되어 있음 -->
        <!-- 위 div class에서 fit 지정해주지 않으면 
        justify-evenly가 적용되지 않고 공백 없이 3개 버튼이 붙어버림
        이 때 fit을 이용해서 해당 row에만 justify-evenly 적용할 수 있게 된다.   -->


        <q-btn-dropdown color="red-10" size="17px" label="상품명">
        <q-list>
          <q-item clickable v-close-popup @click="bac_2l">
            <q-item-section>
              <q-item-label>백산수 2L</q-item-label>                      <!-- 1 -->
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="bac_500ml">
            <q-item-section>
              <q-item-label>백산수 500ml</q-item-label>                   <!-- 2 -->
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="sin_ramyun">
            <q-item-section>
              <q-item-label>신라면 멀티</q-item-label>                    <!-- 3 -->
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="ansung_ramyun">
            <q-item-section>
              <q-item-label>안성탕면 멀티</q-item-label>                  <!-- 4 -->
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="jin_ramyun">
            <q-item-section>
              <q-item-label>진라면 멀티(순한맛)</q-item-label>            <!-- 5 -->
            </q-item-section>
          </q-item>   
        </q-list>
      </q-btn-dropdown>


        <q-btn-dropdown color="primary" size="17px" label="행사구분">
        <q-list>
          <q-item clickable v-close-popup @click="no_event">
            <q-item-section>
              <q-item-label>할인없음</q-item-label>
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="event_on">
            <q-item-section>
              <q-item-label>할인진행</q-item-label>
            </q-item-section>
          </q-item>        
        </q-list>
      </q-btn-dropdown>


        <q-btn-dropdown color="primary" size="17px" label="휴무">
        <q-list>
          <q-item clickable v-close-popup @click="normal_state">
            <q-item-section>
              <q-item-label>정상영업</q-item-label>
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="break_day">
            <q-item-section>
              <q-item-label>일요일 휴무</q-item-label>
            </q-item-section>
          </q-item>        
        </q-list>
      </q-btn-dropdown>

        
      </div> <!-- /div 2 -->
    
        <div class="fit row justify-center content-center">
        <!-- div 3 -->

        <!-- div 4 -->
        <div class="q-pa-md">
          <div class="q-gutter-md row items-start">
            <div>
              <div class="q-pb-sm q-gutter-sm">
                <q-badge color="teal">
                  시작일: {{ model1 }}
                </q-badge>
                <!-- <q-badge color="purple" text-color="white"> Mask: YYYY-MM-DD </q-badge> -->
            </div>
          </div>
        </div>

        <q-date v-model="model1" mask="YYYY-MM-DD" />
      </div>               
        <!-- /div 4 -->
        
        </div>         
        <!-- /div_3 -->


      <!-- div_6 -->
    <div class="q-pa-md">
      <div class="q-gutter-sm">
        <q-checkbox v-model="selection" val=1 label="월요일" color="teal" />
        <q-checkbox v-model="selection" val=2 label="화요일" color="orange" />
        <q-checkbox v-model="selection" val=3 label="수요일" color="red" />
        <q-checkbox v-model="selection" val=4 label="목요일" color="cyan" />
        <q-checkbox v-model="selection" val=5 label="금요일" color="cyan" />
        <q-checkbox v-model="selection" val=6 label="토요일" color="cyan" />
        <q-checkbox v-model="selection" val=7 label="일요일" color="cyan" />

      </div>

      <div class="q-px-sm">
        할인 요일: <strong>{{ selection }}</strong>
      </div>
    </div>
    <!--/div_6  -->
          
    </div>
    <!-- /div 1 -->

    


    <div class="row justify-end q-ma-lg">
          <!-- div_5 -->
        <q-btn push color="white" text-color="primary" label="number_store" @click="number_store"/>
        <q-btn push color="white" text-color="primary" label="date_check" @click="data_check"/>
        <q-btn push color="white" text-color="primary" label="flask" @click="flask_alert"/>
        <q-btn push color="white" text-color="primary" label="summary" @click="summary_alert"/>
        <q-btn push color="white" text-color="primary" label="Predict>>" to="/Predict"/>
        
    </div>
        <!-- /div_5 -->

  </main>
</template>


<script>
import { date, LocalStorage } from "quasar";

import axios from "axios";

export default {
  data () {
    return {
      model1: '2020-02-15',
      model2: '03-21-2019',
      selection: [ ]
      
      
    }
      this.selected_date={model1}
  },


  methods: {

    bac_2l () {
      console.log('Clicked item')
      localStorage.item_1 = '백산수_2l';
    },

    bac_500ml () {
      console.log('Clicked item')
      localStorage.item_1 = '백산수_500ml';
    },
    sin_ramyun () {
      console.log('Clicked item')
      localStorage.item_1 = '신라면_멀티';
    },

    ansung_ramyun () {
      console.log('Clicked item')
      localStorage.item_1 = '안성탕면_멀티';
    },
    jin_ramyun () {
      console.log('Clicked item')
      localStorage.item_1 = '진라면_멀티(순한맛)';

    },

    no_event () {
      console.log('Clicked event_info')
      localStorage.event_1 = '정상가';
    },

    event_on () {
      console.log('Clicked event_info')
      localStorage.event_1 = '할인진행';
    },

    normal_state () {
      console.log('Clicked break_info')
      localStorage.break_1 = 0;
    },

    break_day () {

      console.log('Clicked break_info')

      localStorage.break_1 = 1;

    },

    summary_alert () {

      console.log('Clicked summary_alert')
      var item_info = localStorage.getItem('item_1');
      var event_info = localStorage.getItem('event_1');
      var break_info = localStorage.getItem('break_1');
      // localStorage.event_222=test_variable
      alert("예측 상품 : " + item_info + "  할인 정보 : " + event_info + "  휴무 정보 : " + break_info);
    },

    // for test
    
    flask_alert : function () {

      const data = {
        
        
        "for_return" : this.day1_2,
        "selected_date" : this.model1,
        "event_info" : this.selection,
        "break_info" : localStorage.getItem('break_1')
      }

      axios.post('http://127.0.0.1:5000/date_info',

        data

      ).then(response => {

        console.log(response)

        localStorage.origin_data = JSON.stringify(response.data);
        localStorage.return1 = JSON.stringify(response.data['day']);
        localStorage.return2 = JSON.stringify(response.data['promotion']);
        
        // alert(test_data);
        setTimeout(function() { 
          this.return1=localStorage.return1 }, 50);
        setTimeout(function() { 
          alert(this.return1) }, 100);
          
        // this.day1_1=localStorage.day1;

      }).catch((ex) => {

        console.warn("ERROR!!!!! : ", ex)

      });
      
      

    },
    data_check () {
      console.log('Clicked data_check')
      // this.sel_date=data();
      // this.check_data = localStorage.getItem('origin_data');
      
      // localStorage.event_222=test_variable
      alert(this.model1);
      alert(this.selection);
    },
    number_store () {
      localStorage.day1 = 200;
      localStorage.day2 = 555;
      localStorage.day3 = 900;
      localStorage.day4 = 600;
      localStorage.day5 = 700;
      localStorage.day6 = 400;
      localStorage.day7 = 200;
      this.day1_2 = localStorage.day2;
    },

    searchparam () {
      const data = {
        "item": this.item_info,
        "event": this.event_info,
        "break": this.break_info 
      }
      axios.post('http:://localhost:3000/api/v1.0/forecast/sale',
        data
      ).then(response => {
        console.log(response)
        this.axiosPostResponseData = JSON.stringify(response.data)
      }).catch((ex) => {
        console.warn("ERROR!!!!! : ", ex)
      })
    }
    
  },

  
}


// for test
// flask_alert () {
//       postAxios: function () {

//       const data = {

//         "name": "morpheus22",

//         "job": "leader"

//       }

//       axios.post('http://127.0.0.1:5000/userLogin',

//         data

//       ).then(response => {

//         console.log(response)

//         this.axiosPostResponseData = JSON.stringify(response.data)

//       }).catch((ex) => {

//         console.warn("ERROR!!!!! : ", ex)

//       })

//     }

//   },



</script>



