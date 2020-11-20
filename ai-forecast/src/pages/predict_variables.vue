<template>
  <main class="q-page q-pa-sm" style="min-height: 704px;">

    <!-- div 1 -->
    <div class="fit column content-center items-center justify-evenly"> 
      <!-- 전체 가운데 정렬 -->
    
 

       <!-- div 2 -->
        <div class="fit row q-col-gutter-sm  q-py-sm content-center items-center justify-center" style="max-width:320px">  
        <!-- 상위 div에서 column의 content를 center 정렬하라고 되어 있음 -->
        <!-- 위 div class에서 fit 지정해주지 않으면 
        justify-evenly가 적용되지 않고 공백 없이 3개 버튼이 붙어버림
        이 때 fit을 이용해서 해당 row에만 justify-evenly 적용할 수 있게 된다.   -->


          <div class="q-py-xl" style="min-height:50px">
            <q-btn-dropdown color="red-10" size="12px" label="상품명">
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
          </div>


        <!-- <q-btn-dropdown color="primary" size="17px" label="행사구분">
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
      </q-btn-dropdown> -->

      
      <div class="q-py-xl" style="min-height:50px">
        <q-btn-dropdown color="primary"
        size="12px" 
        label="휴무"
        
      
        >
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
      </div>


      <div class="q-py-xl" style="min-height:50px">
        <q-btn-dropdown
          
          color="primary"
          label="할인요일"
          size="12px"
          
        >
          <!-- style="max-height:50px" -->
          <div class="row no-wrap q-pa-md" >
            <div class="column">
              <div class="text-h6 q-mb-lg" >할인 요일 선택</div>
              <q-toggle v-model="event_mon" label="월요일 할인" />
              <q-toggle v-model="event_tue" label="화요일 할인" />
              <q-toggle v-model="event_wen" label="수요일 할인" />
              <q-toggle v-model="event_thu" label="목요일 할인" />
              <q-toggle v-model="event_fri" label="금요일 할인" />
              <q-toggle v-model="event_sat" label="토요일 할인" />
              <q-toggle v-model="event_sun" label="일요일 할인" />

            </div>

          </div>
        </q-btn-dropdown>
      </div>


      
      </div> 
      <!-- /div 2 -->      


        <!-- div 3 -->
        <div class="fit row justify-center content-center" style="max-width:400px">
        

        <!-- div 4 -->
        <div class="q-pa-sm">
          <div class="q-gutter-md row items-start">
            <div>
              <div class="q-pb-sm q-gutter-sm">
                <q-badge color="teal">
                  기준일: {{ model1 }}
                </q-badge>
                <!-- <q-badge color="purple" text-color="white"> Mask: YYYY-MM-DD </q-badge> -->
            </div>
          </div>
        </div>

        <q-date v-model="model1" 
        :options="optionsFn"
         mask="YYYY-MM-DD" />
      </div>               
        <!-- /div 4 -->
        
        </div>         
        <!-- /div_3 -->


       
   
<!-- 
      <div class="fit row justify-start" style="max-width:630px">
      
      <q-btn color="white" text-color="black" label="할인 요일 선택" />
      </div> -->

      <!-- div_6 -->
    <!-- <div class="q-pa-md">
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
    </div> -->
    <!--/div_6  -->





    

      


      <!-- 할인정보 체크박스 형태 -->
      <!-- div_6  -->
    <!-- <div class="q-pa-md">
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
    </div> -->
    <!--/div_6  -->
    
        

  
    <!-- div_10 -->
    <div class="fit row q-col-gutter-sm  q-py-lg content-center items-center justify-between" style="max-width:305px">
      
      <!-- div_5 -->
      <div class="row q-py-sm">
      
        
        <!-- <q-btn push color="primary" text-color="white" label="예측하기" @click="flask_alert"/> -->
        <!-- <q-btn :loading="loading2" size="14px" color="primary" @click="simulateProgress(2)">
          
          
          예측하기
        <template v-slot:loading>
          computing...
        </template>
        </q-btn> -->
        <q-btn label="예측하기" color="primary" size="14px" @click="showCustom" />

      </div>
      <!-- /div_5 -->
        <!-- div21 -->
        <div class="row q-py-sm">
          <q-btn push color="primary" text-color="white" size="14px" label="예측 결과보기" to="/Predict"/>
        </div>
        <!-- /div21 -->
    </div>
    <!-- /div_10 -->
    
      <!-- div22 -->
      <!-- <div class="fit row q-pt-xl justify-start">
        <div class='fit row q-pt-xl'>
          <q-btn push color="primary" text-color="white" label="<< 매장선택" size="10px" to="/map"/>
        
      </div>
      </div> -->
      <!-- /div22 -->

    </div>
    <!-- /div 1 -->

  </main>
</template>


<script>
import { date, LocalStorage } from "quasar";
import { QSpinnerGears } from 'quasar'
import BarChart from '../components/charts/BarChart'
// import Predict from '../pages/Predict'
import axios from "axios";
import { QSpinnerFacebook } from 'quasar'

export default {
  data () {
    return {

      model1: '2019-12-01',
      // model2: '03-21-2019',
      selection: [ ],
      // test1_data : Predict.data().getflag,
      event_mon: false,
      event_tue: false,
      event_wen: false,
      event_thu: false,
      event_fri: false,
      event_sat: false,
      event_sun: false,
      loading: false,
      loading2: false,
      progress: false
      
    }

      this.selected_date={model1}

  },

  methods: {

    bac_2l () {
      console.log('Clicked item')
      localStorage.item_1 = '백산수2.0L';
      store_
    },

    bac_500ml () {
      console.log('Clicked item')
      localStorage.item_1 = '백산수500ml';
    },

    sin_ramyun () {
      console.log('Clicked item')
      localStorage.item_1 = '신라면멀티';
    },

    ansung_ramyun () {
      console.log('Clicked item')
      localStorage.item_1 = '안성탕면멀티';
    },

    jin_ramyun () {
      console.log('Clicked item')
      localStorage.item_1 = '진라면멀티(순한맛)';

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

    optionsFn (model1) {
      return model1 >= '2019/11/01' && model1 <= '2019/12/31'
    },

    showCustom () {


        localStorage.event_mon=this.event_mon;
        localStorage.event_tue=this.event_tue;
        localStorage.event_wen=this.event_wen;
        localStorage.event_thu=this.event_thu;
        localStorage.event_fri=this.event_fri;
        localStorage.event_sat=this.event_sat;
        localStorage.event_sun=this.event_sun;

        if (this.event_mon === true) {
        this.wday1 = "월요일"
      };
        if (this.event_tue === true) {
        this.wday2 = "화요일"
      };
        if (this.event_wen === true) {
        this.wday3 = "수요일"
      };
        if (this.event_thu === true) {
        this.wday4 = "목요일"
      };
        if (this.event_fri === true) {
        this.wday5 = "금요일"
      };
        if (this.event_sat === true) {
        this.wday6 = "토요일"
      };
        if (this.event_sun === true) {
        this.wday7 = "일요일"
      };

      this.edays=[]
      if (this.wday1 ==='월요일') { this.edays.push(this.wday1)     
      };
        if (this.wday2 ==='화요일') { this.edays.push(this.wday2)
      };
        if (this.wday3 ==='수요일') { this.edays.push(this.wday3)
      };
        if (this.wday4 ==='목요일') { this.edays.push(this.wday4)
      };
        if (this.wday5 ==='금요일') { this.edays.push(this.wday5)
      };
        if (this.wday6 ==='토요일') { this.edays.push(this.wday6)
      };
        if (this.wday7 ==='일요일') { this.edays.push(this.wday7)
      };
        localStorage.edate=this.edays;
        
      const data = {

        // "for_return" : this.day1_2,
        "selected_date" : this.model1,
        "event_info" : {'1': localStorage.event_mon, '2' : localStorage.event_tue, '3' : localStorage.event_wen,
                        '4' : localStorage.event_thu, '5': localStorage.event_fri, '6' : localStorage.event_sat,
                        '7' : localStorage.event_sun},
        // "event_info" : [localStorage.event_mon, localStorage.event_tue, localStorage.event_wen, localStorage.event_thu, 
        //                 localStorage.event_fri, localStorage.event_sat, localStorage.event_sun,],
        // "break_info" : this.break_info,
        "item_info" : localStorage.getItem('item_1'),
        "store_info" : localStorage.getItem('store_code'),
        "break_info" : localStorage.getItem('break_1')
        
      }

      axios.post('http://127.0.0.1:5000/date_info',

        data

      ).then(response => {

        console.log(response)

        localStorage.origin_data = JSON.stringify(response.data);
        localStorage.day1 = response.data['day1'];
        localStorage.day2 = response.data['day2'];
        localStorage.day3 = response.data['day3'];
        localStorage.day4 = response.data['day4'];
        localStorage.day5 = response.data['day5'];
        localStorage.day6 = response.data['day6'];
        localStorage.day7 = response.data['day7'];
        localStorage.Tday1 = JSON.stringify(response.data['Tday1']);
        localStorage.Tday2 = JSON.stringify(response.data['Tday2']);
        localStorage.Tday3 = JSON.stringify(response.data['Tday3']);
        localStorage.Tday4 = JSON.stringify(response.data['Tday4']);
        localStorage.Tday5 = JSON.stringify(response.data['Tday5']);
        localStorage.Tday6 = JSON.stringify(response.data['Tday6']);
        localStorage.Tday7 = JSON.stringify(response.data['Tday7']);
        localStorage.date = this.model1;
        // localStorage.return2 = JSON.stringify(response.data['promotion']);
        
        // alert(test_data);
        setTimeout(function() { 
          this.return1=localStorage.return1 }, 15);
        
          
        // this.day1_1=localStorage.day1;

      }).catch((ex) => {

        console.warn("ERROR!!!!! : ", ex)

      });


      const dialog = this.$q.dialog({
        title: '판매량을 예측 하는중...',
        dark: true,
        message: '0%',
        progress: {
          spinner: QSpinnerGears,
          color: 'amber'
        },
        persistent: true, // we want the user to not be able to close it
        ok: false // we want the user to not be able to close it
      })

      // we simulate some progress here...
      let percentage = 0
      const interval = setInterval(() => {
        percentage = Math.min(100, percentage + Math.floor(Math.random() * 7))
        // *22가 원본

        // we update the dialog
        dialog.update({
          message: `${percentage}%`
        })
        


      //   if (!localStorage.day1) {
          // setTimeout(function() {
            
          // console.log("not arrived")}, 1000);
        
      //       // if we are done...
      // }
        if (!localStorage.day1 || percentage !== 100) {
          setTimeout(function() {
            
          console.log("not arrived")}, 400);
        } 
        else if (percentage === 100) {
          clearInterval(interval)

          dialog.update({
            title: '예측완료!',
            message: `예측결과보기를 눌러 확인하세요`,
            progress: false,
            ok: true
          });
        }
      }, 100)
    },



    // let percentage = 0
    //   const interval = setInterval(() => {
    //     percentage = Math.min(100, percentage + Math.floor(Math.random() * 35))
    //     // *22가 원본

    //     // we update the dialog
    //     dialog.update({
    //       message: `${percentage}%`
    //     })

    //     // if we are done...
    //     if (percentage === 100) {
    //       clearInterval(interval)

    //       dialog.update({
    //         title: '예측완료!',
    //         message: `예측결과보기를 눌러 확인하세요`,
    //         progress: false,
    //         ok: true
    //       })
    //     }
    //   }, 500)
    // },







    flask_alert : function () {

      this.$q.loading.show({
        spinner: QSpinnerFacebook,
        spinnerColor: 'yellow',
        spinnerSize: 140,
        backgroundColor: 'blue',
        message: 'Forecasting...',
        messageColor: 'black'
      })

      this.timer = setTimeout(() => {
        this.$q.loading.hide()
        this.timer = void 0
      }, 3000)

        localStorage.event_mon=this.event_mon;
        localStorage.event_tue=this.event_tue;
        localStorage.event_wen=this.event_wen;
        localStorage.event_thu=this.event_thu;
        localStorage.event_fri=this.event_fri;
        localStorage.event_sat=this.event_sat;
        localStorage.event_sun=this.event_sun;

        if (this.event_mon === true) {
        this.wday1 = "월요일"
      };
        if (this.event_tue === true) {
        this.wday2 = "화요일"
      };
        if (this.event_wen === true) {
        this.wday3 = "수요일"
      };
        if (this.event_thu === true) {
        this.wday4 = "목요일"
      };
        if (this.event_fri === true) {
        this.wday5 = "금요일"
      };
        if (this.event_sat === true) {
        this.wday6 = "토요일"
      };
        if (this.event_sun === true) {
        this.wday7 = "일요일"
      };

      this.edays=[]
      if (this.wday1 ==='월요일') { this.edays.push(this.wday1)     
      };
        if (this.wday2 ==='화요일') { this.edays.push(this.wday2)
      };
        if (this.wday3 ==='수요일') { this.edays.push(this.wday3)
      };
        if (this.wday4 ==='목요일') { this.edays.push(this.wday4)
      };
        if (this.wday5 ==='금요일') { this.edays.push(this.wday5)
      };
        if (this.wday6 ==='토요일') { this.edays.push(this.wday6)
      };
        if (this.wday7 ==='일요일') { this.edays.push(this.wday7)
      };
        localStorage.edate=this.edays;
        

  
      const data = {
        // "for_return" : this.day1_2,
        "selected_date" : this.model1,
        "event_info" : {'1': localStorage.event_mon, '2' : localStorage.event_tue, '3' : localStorage.event_wen,
                        '4' : localStorage.event_thu, '5': localStorage.event_fri, '6' : localStorage.event_sat,
                        '7' : localStorage.event_sun},
        // "event_info" : [localStorage.event_mon, localStorage.event_tue, localStorage.event_wen, localStorage.event_thu, 
        //                 localStorage.event_fri, localStorage.event_sat, localStorage.event_sun,],
        // "break_info" : this.break_info,
        "item_info" : localStorage.getItem('item_1'),
        "store_info" : localStorage.getItem('store_code'),
        "break_info" : localStorage.getItem('break_1')
      }

      axios.post('http://127.0.0.1:5000/date_info',
        data
      ).then(response => {

        console.log(response)

        localStorage.origin_data = JSON.stringify(response.data);
        localStorage.day1 = response.data['day1'];
        localStorage.day2 = response.data['day2'];
        localStorage.day3 = response.data['day3'];
        localStorage.day4 = response.data['day4'];
        localStorage.day5 = response.data['day5'];
        localStorage.day6 = response.data['day6'];
        localStorage.day7 = response.data['day7'];
        localStorage.Tday1 = JSON.stringify(response.data['Tday1']);
        localStorage.Tday2 = JSON.stringify(response.data['Tday2']);
        localStorage.Tday3 = JSON.stringify(response.data['Tday3']);
        localStorage.Tday4 = JSON.stringify(response.data['Tday4']);
        localStorage.Tday5 = JSON.stringify(response.data['Tday5']);
        localStorage.Tday6 = JSON.stringify(response.data['Tday6']);
        localStorage.Tday7 = JSON.stringify(response.data['Tday7']);
        localStorage.date = this.model1;
  

      setTimeout(function() { 
        this.return1=localStorage.return1 }, 50);

      setTimeout(function() { 
        alert('예측완료') }, 150);
          
      }).catch((ex) => {
        console.warn("ERROR!!!!! : ", ex)
      });

    },

    beforeDestroy () {
      if (this.timer !== void 0) {
        clearTimeout(this.timer)
        this.$q.loading.hide()
      }
    },

    training : function () {
      const data = {

        // "for_return" : this.day1_2,
        "selected_date" : this.model1,
        "event_info" : {'1': localStorage.event_mon, '2' : localStorage.event_tue, '3' : localStorage.event_wen,
                        '4' : localStorage.event_thu, '5': localStorage.event_fri, '6' : localStorage.event_sat,
                        '7' : localStorage.event_sun},
        // "event_info" : [localStorage.event_mon, localStorage.event_tue, localStorage.event_wen, localStorage.event_thu, 
        //                 localStorage.event_fri, localStorage.event_sat, localStorage.event_sun,],
        // "break_info" : this.break_info,
        "item_info" : localStorage.getItem('item_1'),
        "store_info" : localStorage.getItem('store_code'),
        "break_info" : localStorage.getItem('break_1')
        
      }

      axios.post('http://127.0.0.1:5000/training',

        data

      ).then(response => {

        console.log(response)

        localStorage.traing = JSON.stringify(response.data);
        
        // localStorage.return2 = JSON.stringify(response.data['promotion']);
        
        // alert(test_data);
        setTimeout(function() { 
          this.return1 = localStorage.return1 }, 50);

        setTimeout(function() { 
          alert(this.return1) }, 100);
          
        // this.day1_1=localStorage.day1;

      }).catch((ex) => {
        console.warn("ERROR!!!!! : ", ex)
      });
      
  
    },
    
  },
}

</script>
