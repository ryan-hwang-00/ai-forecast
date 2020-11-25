<template>

  
          

  <main class="q-page q-pa-sm fit column content-center items-center" style="max-height: 720px;">



    <div class="q-pa-xm">
      <div class="q-pa-md"></div>
      
    <div class="q-gutter-md" style="width: 1100px">


    <q-field outlined label="" stack-label>
        <template v-slot:control>
          <div class="self-center full-width no-outline" tabindex="0"></div>


    

    
    <div class="row q-pa-sm"></div>
    
    <!-- 여백 조절 -->

    <div class="q-pl-md column content-center items-center" style="width : 1000px">
    
    <!-- <div class="column q-pa-lg"></div> -->
    <div class="column q-pa-sm"></div>

    </div>

    <!-- div 0 -->
    <div class="row justify-evenly" style="width : 1000px">

    
    <!-- div 1 -->
    <div class="fit column content-center items-center justify-evenly" style="max-width:350px">
      <!-- 전체 가운데 정렬 -->
    
    
    <div class="row q-pa-md"></div>
 

       <!-- div 2 -->
        <!-- <div class="fit row q-col-gutter-sm q-py-sm content-center items-center justify-center" style="max-width:350px">   -->
        
        <div class="row q-pa-lg"></div>
         <!-- div_31 -->
          <div class="q-py-md" style="min-height:50px">
            <q-btn-dropdown color="primary" 
              size="18px"
              style='width:170px' 
              label="상품명">
              <q-list>
                <q-item clickable v-close-popup @click="bac_2l">
                  <q-item-section>
                    <q-item-label>생수 2L</q-item-label>                      <!-- 1 -->
                  </q-item-section>
                </q-item>

                <q-item clickable v-close-popup @click="bac_500ml">
                  <q-item-section>
                    <q-item-label>생수 500ml</q-item-label>                   <!-- 2 -->
                  </q-item-section>
                </q-item>

                <q-item clickable v-close-popup @click="sin_ramyun">
                  <q-item-section>
                    <q-item-label>라면A</q-item-label>                    <!-- 3 -->
                  </q-item-section>
                </q-item>

                <q-item clickable v-close-popup @click="ansung_ramyun">
                  <q-item-section>
                    <q-item-label>라면B</q-item-label>                  <!-- 4 -->
                  </q-item-section>
                </q-item>

                <q-item clickable v-close-popup @click="jin_ramyun">
                  <q-item-section>
                    <q-item-label>라면C</q-item-label>            <!-- 5 -->
                  </q-item-section>
                </q-item>   
              </q-list>
            </q-btn-dropdown>
          </div>
          <!-- /div_31 -->
        
      <!-- /div 2 -->


      
      <div class="q-py-md" style="min-height:50px">
        <q-btn-dropdown color="primary"
        
        label="휴무"        
        size="18px"
        style='width:170px'
        
      
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

      <!-- div_25 -->
      <div class="q-py-md" style="min-height:50px">
        <q-btn-dropdown
          
          color="primary"
          label="할인요일"
          size="18px"
          style='width:170px'
          
        >
          <!-- style="max-height:50px" -->
          <div class="row no-wrap q-pa-md" >
            <div class="column">
              <div class="text-h6 q-mb-lg" >할인 요일 선택</div>
              <q-toggle v-model="event_mon" label="월요일 할인" @input="event_toggle"/>
              <q-toggle v-model="event_tue" label="화요일 할인" @input="event_toggle"/>
              <q-toggle v-model="event_wen" label="수요일 할인" @input="event_toggle"/>
              <q-toggle v-model="event_thu" label="목요일 할인" @input="event_toggle"/>
              <q-toggle v-model="event_fri" label="금요일 할인" @input="event_toggle"/>
              <q-toggle v-model="event_sat" label="토요일 할인" @input="event_toggle"/>
              <q-toggle v-model="event_sun" label="일요일 할인" @input="event_toggle"/>

            </div>

          </div>

          <div class="row q-pa-sm justify-end">
      
            <!-- <q-btn label="적용" color="red-10" size="12px" style="width : 95px" @click="toggle_bus1"/> -->

          </div>
        </q-btn-dropdown>
      </div>
      <!-- /div_25 -->



      <!-- div_26 -->
      <div class="q-py-md" style="min-height:50px">
        <q-btn-dropdown
          
          color="primary"
          label="대량주문"
          size="18px"
          style='width:170px'
          
        >
          <!-- style="max-height:50px" -->
          <div class="row no-wrap q-pa-md" >
            <div class="column">
              <div class="text-h6 q-mb-lg" >출하 요일 선택</div>
              <q-toggle v-model="so_event_mon" label="월요일" @input="so_toggle1"/>
              <!-- <q-toggle v-model="so_event_mon" label="월요일" /> -->
              <q-toggle v-model="so_event_tue" label="화요일" @input="so_toggle1"/>
              <q-toggle v-model="so_event_wen" label="수요일" @input="so_toggle1"/>
              <q-toggle v-model="so_event_thu" label="목요일" @input="so_toggle1"/>
              <q-toggle v-model="so_event_fri" label="금요일" @input="so_toggle1"/>
              <q-toggle v-model="so_event_sat" label="토요일" @input="so_toggle1"/>
              <q-toggle v-model="so_event_sun" label="일요일" @input="so_toggle1"/>

            </div>

          </div>

          <div class="row q-pa-sm justify-end">
      
            <!-- <q-btn label="적용" color="red-10" size="12px" style="width : 90px" @click="toggle_bus2"/> -->

          </div>

        </q-btn-dropdown>
      </div>
      <!-- /div_26 -->
    </div>
    <!-- /div 1 -->

<!-- div_1 === div_3 -->

<!-- 달력  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> -->
        <!-- div 3 -->
        <div class="fit row justify-center content-center" style="max-width:350px">
          <div class='row q-py-sm'></div>
        

        <!-- div 4 -->
        <div class="q-pa-sm">
          <div class='row q-py-sm'></div>
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

        <q-date 
          v-model="model1" 
          :options="optionsFn"
          mask="YYYY-MM-DD" @click="clickDate"/>
        </div>               
        <!-- /div 4 -->
        
        </div>
        <!-- /div_3 -->

    </div>
    <!-- /div 0 -->

  <div 
    class="q-pl-md column content-center items-center" 
    style="width : 1000px">
    
    <div class="column q-pa-lg"></div>
    <div class="column q-pa-xs"></div>

  </div>
  

   </template>
    </q-field>
    </div>
  </div>

  <div class="q-pl-md column content-center items-center" style="width : 1000px">
    
    <div class="column q-pa-md"></div>
    
    <!-- <div class="row q-pa-xs">2</div> -->
    <!-- 여백 조절 -->

    <!-- div_30 -->
    <!-- <div class="row content-center items-center justify-evenly"> -->

      <!-- <div class="row justify-evenly" style="width : 750px"> -->
    
    <!-- div_10 -->
    <div class="row q-col-gutter-sm q-py-lg content-center items-center justify-between" style="width:350px">
      
      <!-- div_5 -->
      <div class="row q-pa-sm">
      
        <q-btn label="예측하기" color="red-10" size="15px" style="width : 140px" @click="showCustom" />
        <!-- <q-btn label="학습시키기" color="red-10" size="15px" style="width : 140px" @click="showCustomTraining" /> -->

      </div>
      <!-- /div_5 -->
        <!-- div21 -->



        <div class="row q-pa-sm">
          <q-btn color="primary" text-color="white" size='15px' style="width : 140px" label="예측 결과보기" to="/Predict"/>
        </div>
        <!-- /div21 -->
    </div>
    <!-- /div_10 -->
    <!-- </div> -->
    <!-- /div_30 -->
    </div>
    <div class="column q-pa-md"></div>
      <!-- <task proptest = 'test111'></task> -->
    <!-- <task> v-for=" (task) in tasks"      </task> -->
  <div class="q-pa-md"></div>


    
  </main>
  
  
</template>


<script>
import { date, LocalStorage } from "quasar";
import { QSpinnerGears } from 'quasar'
import BarChart from '../components/charts/BarChart'
// import Predict from '../pages/Predict'
import axios from "axios";
import EventBus from '../components/eventBus.js';
import Predict from '../pages/Predict.vue';

// document.onclick = processClick;






export default {
  
  // name: 'Child',
  // components: {
  //   ChildAndChild
  // },



  data () {
    return {

      tasks : [
        {
          name : 'Go to shop',
          dudate : '2019/05/12',
          duetime: '18:00'
        },
        {
          name : 'test2',
          dudate : '2020/01/23',
          dutime : '19:00'
        }
      ],

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

      so_event_mon: false,
      so_event_tue: false,
      so_event_wen: false,
      so_event_thu: false,
      so_event_fri: false,
      so_event_sat: false,
      so_event_sun: false,

      loading: false,
      loading2: false,

      progress: false
      
    }

      this.selected_date={model1}

  },

  components : {
    'task' : Predict
  },

  methods: {

    clickDate () {
      EventBus.$emit("Date_bus", this.model1)

    },
    // so_toggle1 () {
    //   EventBus.$emit("special_order_bus", this.so_event_mon)

    // },


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



    bac_2l () {
      console.log('Clicked item')
      localStorage.item_1 = '백산수2.0L';
      const item_1 = '생수 2.0L';
      EventBus.$emit("product_bus", item_1);
    },

    bac_500ml () {
      console.log('Clicked item')
      localStorage.item_1 = '백산수500ml';
      const item_1 = '생수 500ml';
      
      EventBus.$emit("product_bus", item_1);
    },

    sin_ramyun () {
      console.log('Clicked item')
      localStorage.item_1 = '신라면멀티';
      const item_1 = '라면A';
      
      EventBus.$emit("product_bus", item_1);
    },

    ansung_ramyun () {
      console.log('Clicked item')
      localStorage.item_1 = '안성탕면멀티';
      const item_1 = '라면B';
      
      EventBus.$emit("product_bus", item_1);
    },

    jin_ramyun () {
      console.log('Clicked item')
      localStorage.item_1 = '진라면멀티(순한맛)';
      const item_1 = '라면C';
      
      EventBus.$emit("product_bus", item_1);

    },

    // no_event () {
    //   console.log('Clicked event_info')
    //   localStorage.event_1 = '정상가';
    // },


    // event_on () {
    //   console.log('Clicked event_info')
    //   localStorage.event_1 = '할인진행';
    // },

    normal_state () {
      console.log('Clicked break_info')
      localStorage.break_1 = 0;
      const break_bus = '정상영업';      
      EventBus.$emit("break_bus", break_bus);
    },

    break_day () {
      console.log('Clicked break_info')
      localStorage.break_1 = 1;

      const break_bus = '일요휴무';      
      EventBus.$emit("break_bus", break_bus);

    },

    optionsFn (model1) {
      return model1 >= '2019/11/01' && model1 <= '2019/12/31'
    },

    
    event_toggle () {
      console.log('clicked toggle special_order')
      

      localStorage.event_mon=this.event_mon;
      localStorage.event_tue=this.event_tue;
      localStorage.event_wen=this.event_wen;
      localStorage.event_thu=this.event_thu;
      localStorage.event_fri=this.event_fri;
      localStorage.event_sat=this.event_sat;
      localStorage.event_sun=this.event_sun;


      this.edays=[]

        if (this.event_mon === true) {
        this.wday1 = "월";
        this.edays.push(this.wday1)
        this.edays.push(',')
      };
        if (this.event_tue === true) {
        this.wday2 = "화"
        this.edays.push(this.wday2)
        this.edays.push(',')
      };
        if (this.event_wen === true) {
        this.wday3 = "수"
        this.edays.push(this.wday3)
        this.edays.push(',')
      };
        if (this.event_thu === true) {
        this.wday4 = "목"
        this.edays.push(this.wday4)
        this.edays.push(',')
      };
        if (this.event_fri === true) {
        this.wday5 = "금"
        this.edays.push(this.wday5)
        this.edays.push(',')
      };
        if (this.event_sat === true) {
        this.wday6 = "토"
        this.edays.push(this.wday6)
        this.edays.push(',')
      };
        if (this.event_sun === true) {
        this.wday7 = "일"
        this.edays.push(this.wday7)
        this.edays.push(',')
      };
      
      this.edays.pop();
      EventBus.$emit("event_bus", this.edays);
     

    },


    so_toggle1 () {
      console.log('clicked toggle special_order')
      // console.log('boolean>>>>', this.so_event_mon)
      

      localStorage.so_event_mon=this.so_event_mon;
      localStorage.so_event_tue=this.so_event_tue;
      localStorage.so_event_wen=this.so_event_wen;
      localStorage.so_event_thu=this.so_event_thu;
      localStorage.so_event_fri=this.so_event_fri;
      localStorage.so_event_sat=this.so_event_sat;
      localStorage.so_event_sun=this.so_event_sun;


      this.so_days=[]

        if (this.so_event_mon === true) {
        this.so_day1 = "월";
        this.so_days.push(this.so_day1)
        this.so_days.push(',')
      };
        if (this.so_event_tue === true) {
        this.so_day2 = "화"
        this.so_days.push(this.so_day2)
        this.so_days.push(',')
      };
        if (this.so_event_wen === true) {
        this.so_day3 = "수"
        this.so_days.push(this.so_day3)
        this.so_days.push(',')
      };
        if (this.so_event_thu === true) {
        this.so_day4 = "목"
        this.so_days.push(this.so_day4)
        this.so_days.push(',')
      };
        if (this.so_event_fri === true) {
        this.so_day5 = "금"
        this.so_days.push(this.so_day5)
        this.so_days.push(',')
      };
        if (this.so_event_sat === true) {
        this.so_day6 = "토"
        this.so_days.push(this.so_day6)
        this.so_days.push(',')
      };
        if (this.so_event_sun === true) {
        this.so_day7 = "일"
        this.so_days.push(this.so_day7)
        this.so_days.push(',')
      };
      this.so_days.pop();
      EventBus.$emit("special_order_bus", this.so_days);
      // console.log('so_days>>>>>>', this.so_days)
    },


    showCustom () {

      console.log('clicked predict>>>>>', this.model1);
      localStorage.removeItem('day1');


      this.test_day=localStorage.getItem('event_mon')
      console.log('step0>>>>>>>', this.test_day)

      this.edays1=[]

      console.log('stpe1>>>>>>')
      if (this.test_day === true) {
      this.wday1 = "월요일"
      console.log('step1-1>>>>>>')
  
      };

      console.log('stpe2>>>>>>');
        if (localStorage.event_tue === true) {
        this.wday2 = "화요일"
        this.edays.push(this.wday2)
      };

      console.log('stpe3>>>>>>');
        if (localStorage.event_wen === true) {
        this.wday3 = "수요일"
        // this.edays.push(this.wday3)
      };

      console.log('stpe4>>>>>>');
        if (localStorage.event_thu === true) {
        this.wday4 = "목요일"
        // this.edays.push(this.wday4)
      };

      console.log('stpe5>>>>>>');
        if (localStorage.event_fri === true) {
        this.wday5 = "금요일"
        // this.edays.push(this.wday5)
      };

      console.log('stpe6>>>>>>');
        if (localStorage.event_sat === true) {
        this.wday6 = "토요일"
        // this.edays.push(this.wday6)
      };

      console.log('stpe7>>>>>>');
        if (localStorage.event_sun === true) {
        this.wday7 = "일요일"
        // this.edays.push(this.wday7)
      };
      // console.log('edays>>>>>>>', this.wday1)

      
        if(this.wday1 ==='월요일') { this.edays1.push(this.wday1)     
      };
        if (this.wday2 ==='화요일') { this.edays1.push(this.wday2)
      };
        if (this.wday3 ==='수요일') { this.edays1.push(this.wday3)
      };
        if (this.wday4 ==='목요일') { this.edays1.push(this.wday4)
      };
        if (this.wday5 ==='금요일') { this.edays1.push(this.wday5)
      };
        if (this.wday6 ==='토요일') { this.edays1.push(this.wday6)
      };
        if (this.wday7 ==='일요일') { this.edays1.push(this.wday7)
      };
        localStorage.edate=this.edays1;
        console.log('edays>>>>>>', this.edays1)
        

        // 대량주문 정보 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

      this.so_days=[]
        if (localStorage.so_event_mon === true) {
        this.so_day1 = "월요일";
        this.so_days.push(this.so_day1)
      };
        if (localStorage.so_event_tue === true) {
        this.so_day2 = "화요일";
        this.so_days.push(this.so_day2)
      };
        if (localStorage.so_event_wen === true) {
        this.so_day3 = "수요일"
        this.so_days.push(this.so_day3)
      };
        if (localStorage.so_event_thu === true) {
        this.so_day4 = "목요일"
        this.so_days.push(this.so_day4)
      };
        if (localStorage.so_event_fri === true) {
        this.so_day5 = "금요일"
        this.so_days.push(this.so_day5)
      };
        if (localStorage.so_event_sat === true) {
        this.so_day6 = "토요일"
        this.so_days.push(this.so_day6)
      };
        if (localStorage.so_event_sun === true) {
        this.so_day7 = "일요일"
        this.so_days.push(this.so_day7)
      };
      localStorage.so_date=this.so_days;

      
      // if (this.wday1 ==='월요일') { this.edays.push(this.wday1)     
      // };
      //   if (this.so_day2 ==='화요일') { this.so_days.push(this.so_day2)
      // };
      //   if (this.so_day3 ==='수요일') { this.so_days.push(this.so_day3)
      // };
      //   if (this.so_day4 ==='목요일') { this.so_days.push(this.so_day4)
      // };
      //   if (this.so_day5 ==='금요일') { this.so_days.push(this.so_day5)
      // };
      //   if (this.so_day6 ==='토요일') { this.so_days.push(this.so_day6)
      // };
      //   if (this.so_day7 ==='일요일') { this.so_days.push(this.so_day7)
      // };
        





        
// 나중에 주석 해제 할 것
  

      const data = {

        // "for_return" : this.day1_2,
        "selected_date" : this.model1,
        "event_info" : {'1': localStorage.event_mon, '2' : localStorage.event_tue, '3' : localStorage.event_wen,
                        '4' : localStorage.event_thu, '5': localStorage.event_fri, '6' : localStorage.event_sat,
                        '7' : localStorage.event_sun},

        "special_info" : {'1': localStorage.so_event_mon, '2' : localStorage.so_event_tue, '3' : localStorage.so_event_wen,
                        '4' : localStorage.so_event_thu, '5': localStorage.so_event_fri, '6' : localStorage.so_event_sat,
                        '7' : localStorage.so_event_sun},
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

  // 주석 해제 여기까지


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
        percentage = Math.min(100, percentage + Math.floor(Math.random() * 5))
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

// if 구문 주석 해제 하고 else if로 넣을 것
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


    // 여기서부터 트레이닝 버튼
    showCustomTraining () {

      localStorage.event_mon=this.event_mon;
      localStorage.event_tue=this.event_tue;
      localStorage.event_wen=this.event_wen;
      localStorage.event_thu=this.event_thu;
      localStorage.event_fri=this.event_fri;
      localStorage.event_sat=this.event_sat;
      localStorage.event_sun=this.event_sun;

      localStorage.so_event_mon=this.so_event_mon;
      localStorage.so_event_tue=this.so_event_tue;
      localStorage.so_event_wen=this.so_event_wen;
      localStorage.so_event_thu=this.so_event_thu;
      localStorage.so_event_fri=this.so_event_fri;
      localStorage.so_event_sat=this.so_event_sat;
      localStorage.so_event_sun=this.so_event_sun;

      this.edays=[]

        if (this.event_mon === true) {
        this.wday1 = "월요일";
        this.edays.push(this.wday1)
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

      
      // if (this.wday1 ==='월요일') { this.edays.push(this.wday1)     
      // };
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


        // 대량주문 정보 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

      this.so_days=[]
        if (this.so_event_mon === true) {
        this.so_day1 = "월요일";
        this.so_days.push(this.so_day1)
      };
        if (this.so_event_tue === true) {
        this.so_day2 = "화요일"
      };
        if (this.so_event_wen === true) {
        this.so_day3 = "수요일"
      };
        if (this.so_event_thu === true) {
        this.so_day4 = "목요일"
      };
        if (this.so_event_fri === true) {
        this.so_day5 = "금요일"
      };
        if (this.so_event_sat === true) {
        this.so_day6 = "토요일"
      };
        if (this.so_event_sun === true) {
        this.so_day7 = "일요일"
      };

      // if (this.wday1 ==='월요일') { this.edays.push(this.wday1)     
      // };

        if (this.so_day2 ==='화요일') { this.so_days.push(this.so_day2)
      };
        if (this.so_day3 ==='수요일') { this.so_days.push(this.so_day3)
      };
        if (this.so_day4 ==='목요일') { this.so_days.push(this.so_day4)
      };
        if (this.so_day5 ==='금요일') { this.so_days.push(this.so_day5)
      };
        if (this.so_day6 ==='토요일') { this.so_days.push(this.so_day6)
      };
        if (this.so_day7 ==='일요일') { this.so_days.push(this.so_day7)
      };
        localStorage.so_date=this.so_days;

// 나중에 주석 해제 할 것
  
      const data = {

        // "for_return" : this.day1_2,
        "selected_date" : this.model1,
        "event_info" : {'1': localStorage.event_mon, '2' : localStorage.event_tue, '3' : localStorage.event_wen,
                        '4' : localStorage.event_thu, '5': localStorage.event_fri, '6' : localStorage.event_sat,
                        '7' : localStorage.event_sun},

        "special_info" : {'1': localStorage.so_event_mon, '2' : localStorage.so_event_tue, '3' : localStorage.so_event_wen,
                        '4' : localStorage.so_event_thu, '5': localStorage.so_event_fri, '6' : localStorage.so_event_sat,
                        '7' : localStorage.so_event_sun},
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

        localStorage.origin_data = JSON.stringify(response.data);
        // localStorage.return2 = JSON.stringify(response.data['promotion']);
        
        // alert(test_data);
        setTimeout(function() { 
          this.return1=localStorage.return1 }, 15);
        
          
        // this.day1_1=localStorage.day1;

      }).catch((ex) => {

        console.warn("ERROR!!!!! : ", ex)

      });

  // 주석 해제 여기까지


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

// if 구문 주석 해제 하고 else if로 넣을 것
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
    // 트레이닝 버튼 끝




    flask_alert : function () {

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
          this.return1=localStorage.return1 }, 50);
        
          
        // this.day1_1=localStorage.day1;

      }).catch((ex) => {

        console.warn("ERROR!!!!! : ", ex)

      });

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
          this.return1=localStorage.return1 }, 50);
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

<style>

@font-face {
    font-family: 'Jua';
    src: url(../assets/Jua-Regular.ttf);
}

.text-h6 {
  font-family: 'Jua';
}

.block {
  font-family: 'Jua';
  font-size:'28px'
}

.q-date__header {
   font-family: 'Jua';
}


</style>