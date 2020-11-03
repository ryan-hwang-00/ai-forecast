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

          <q-item clickable v-close-popup @click="onItemClick">
            <q-item-section>
              <q-item-label>신라면 멀티</q-item-label>                    <!-- 3 -->
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="onItemClick">
            <q-item-section>
              <q-item-label>안성탕면 멀티</q-item-label>                  <!-- 4 -->
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="onItemClick">
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

        <div class="q-pa-md">                        <!-- div 4 -->
            
            
            <div class="q-pb-sm">{{ date }}</div>
            <q-date v-model="date"
            title="Calendar"
            subtitle="Year" range />
            </div>                             <!-- /div 4 -->
        
        </div>         
        <!-- /div_3 -->
          
    </div>
    <!-- /div 1 -->
    <div class="row justify-end q-ma-lg">
          <!-- div_5 -->

        <q-btn push color="white" text-color="primary" label="summary" @click="summary_alert"/>
        <q-btn push color="white" text-color="primary" label="Predict>>" to="/Predict"/>
        
    </div>
        <!-- /div_5 -->

  </main>
</template>


<script>
export default {
  methods: {

    bac_2l () {
      console.log('Clicked test1')
      localStorage.item_info = '백산수_2l';
    },

    bac_500ml () {
      console.log('Clicked test2')
      localStorage.item_info = '백산수_500ml';
    },

    onItemClick3 () {
      console.log('Clicked test3')
      localStorage.item_info = 'store_test3';
    },

    no_event () {
      console.log('Clicked event_info')
      localStorage.event_info = '정상가';
    },

    event_on () {
      console.log('Clicked event_info')
      localStorage.event_info = '할인진행';
    },

    normal_state () {
      console.log('Clicked break_info')
      localStorage.break_info = '정상영업';
    },

    break_day () {

      console.log('Clicked break_info')
      localStorage.break_info = '일요휴무';

    },

    summary_alert () {

      console.log('Clicked summary_alert')
      var item_summary=localStorage.getItem('item_info');
      var event_summary=localStorage.getItem('event_info');
      var break_summary=localStorage.getItem('break_info');
      // localStorage.event_222=test_variable
      alert("예측 상품 : " + item_summary + "  할인 정보 : " + event_summary + "  휴무 정보 : " + break_summary);
    }
    
  },

  data () {
    return {
      date : { 시작: '2020/07/08', 끝 : '2020/07/17' }
    }
    
  }
}
</script>