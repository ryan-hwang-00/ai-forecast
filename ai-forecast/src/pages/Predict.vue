<template>
  <div class="justify-center q-ma-sm">
    <!-- 예측 변수 정보 chip -->
    <div class="row justify-center q-col-gutter-sm q-py-sm">
      <q-chip
        size="18px"
        color="red-6"
        text-color="white"
        icon="date_range"
      >
        {{getdate}}
      </q-chip>
      <q-chip
        size="18px"
        color="amber-10"
        text-color="white"
        icon="store"
      >
        {{getstore}}
      </q-chip>
      <q-chip
        size="18px"
        color="blue-12"
        text-color="white"
        icon="fastfood"
      >
        {{getproduct}}
      </q-chip>
      <q-chip
        size="18px"
        color="purple-13"
        text-color="white"
        icon="notifications_active"
      >
        {{getevent}}
      </q-chip>
      <q-chip
        size="18px"
        color="deep-purple-8"
        text-color="white"
        icon="beach_access"
      >
        {{getflag}}
      </q-chip>

      <!-- <q-btn color="white" text-color="black" label="예측 변수 정보 불러오기" @click="onvariableClick()"/> -->
    </div>

    <!-- 예측 값 그래프 및 테이블 -->
    <div class="row justify-center q-col-gutter-sm q-py-sm">
      <!-- 예측 값 그래프 캐롯셀 -->
      <div class="col-md-4 col-md-6 col-lg-6 col-lg-10 col-xs-12 q-pa-sm">
        <q-carousel
          v-model="slide"
          transition-prev="scale"
          transition-next="scale"
          swipeable
          animated
          control-color="white"
          navigation
          padding
          arrows
          height="550px"
          width="300px"
          class="bg-primary text-white shadow-1 rounded-borders"
        >
          <q-carousel-slide name="style" class="column no-wrap flex-center">
              <div class="bg-white rounded-borders">
                  <q-card-section class="bg-primary">
                      <div class="row items-center no-wrap">
                          <div class="col">
                              <div class="text-h6 text-white text-center text-Do-Hyeon">주간 예측량</div>
                          </div>
                      </div>
                  </q-card-section>
                  <div>
                      <bar-chart :chart-data="datacollectionBar" :options="optionsBar"></bar-chart>
                  </div>
              </div>
          </q-carousel-slide>

          <q-carousel-slide name="Line" class="column no-wrap flex-center">
              <div class="bg-white rounded-borders">
                  <q-card-section class="bg-primary">
                      <div class="row items-center no-wrap">
                          <div class="col">
                              <div class="text-h6 text-white text-center text-Do-Hyeon">Line Chart</div>
                          </div>
                      </div>
                  </q-card-section>
                  <div style="width:800px">
                      <line-chart :chart-data="datacollectionLine" :options="optionsLine"></line-chart>
                  </div>
              </div>
          </q-carousel-slide>

          <q-carousel-slide name="mixed" class="column no-wrap flex-center">
              <mixed-chart></mixed-chart>
          </q-carousel-slide>

          <q-carousel-slide name="ef" class="column no-wrap flex-center">
              <div class="bg-white rounded-borders">
                  <q-card-section class="bg-primary">
                      <div class="row items-center no-wrap">
                          <div class="col">
                              <div class="text-h6 text-white text-center text-Do-Hyeon">Doughnut Chart</div>
                          </div>
                      </div>
                  </q-card-section>
                  <div>
                      <Doughnut-chart :chart-data="datacollectionDoughnut"></Doughnut-chart>
                  </div>
              </div>
          </q-carousel-slide>

          <q-carousel-slide name="fe" class="column no-wrap flex-center">
              <div class="bg-white rounded-borders">
                  <q-card-section class="bg-primary">
                      <div class="row items-center no-wrap">
                          <div class="col">
                              <div class="text-h6 text-white text-center text-Do-Hyeon">Pie Chart</div>
                          </div>
                      </div>
                  </q-card-section>
                  <div>
                      <Pie-chart :chart-data="datacollectionPie" :options="optionsPie"></Pie-chart>
                  </div>
              </div>
          </q-carousel-slide>

        </q-carousel>

      </div>
      <!-- 예측 값 테이블 -->
      <div class="col-md-4 col-md-6 col-lg-6 col-lg-10 col-xs-12 q-pa-sm">
        <q-table
          title="주간 예측량"
          :data="data"
          :columns="columns"
          height="550px"
          width="500px"
          row-key="Date"
        />
      </div>

    </div>

  </div>
</template> 

<script>
// import PieChart from '../components/charts/PieChart.vue'
import MixedChart from '../components/charts/MixedChart.vue'
// import LineChart from '../components/charts/LineChart.vue'
// import BarChart from '../components/charts/BarChart.vue'
import { LocalStorage } from "quasar";
import LineChart from '../components/charts/LineChart.js'
import BarChart from '../components/charts/BarChart.js'
import PieChart from '../components/charts/PieChart.js'
import DoughnutChart from '../components/charts/DoughnutChart.js'
import Mycanvas from '../components/canvas/Mycanvas.vue'

export default {
  name: "Predict",
  components: {
    BarChart,
    LineChart,
    PieChart,
    MixedChart,
    DoughnutChart,
    Mycanvas
  },
  data () {
    return {
      // Chip Data
      getdate: '날짜',
      getstore: '매장명',
      getproduct: '상품명',
      getevent: '행사',
      getflag: '휴무일',
      slide: 'style',
      
      // Chart Data
      datacollectionBar: null,
      optionsBar: null,
      datacollectionLine: null,
      optionsLine: null,
      datacollectionDoughnut: null,
      datacollectionPie: null,
      optionsPie: null,

      // Table Data
      columns: [
        {
          name: 'Date',
          required: true,
          label: 'Date',
          align: 'left',
          field: 'Date',
          sortable: true
        },
        {
          name: 'Predict_Value',
          label: '예측 수량',
          align: 'right',
          field: 'Predict_Value',
          sortable: true
        }
      ],
      data: [
        {
          Date: '2020-10-23',
          Predict_Value: 118,
        },
        {
          Date: '2020-10-24',
          Predict_Value: 131,
        },
        {
          Date: '2020-10-25',
          Predict_Value: 159,
        },
        {
          Date: '2020-10-26',
          Predict_Value: 182,
        },
        {
          Date: '2020-10-27',
          Predict_Value: 159,
        },
        {
          Date: '2020-10-28',
          Predict_Value: 284,
        },
        {
          Date: '2020-10-29',
          Predict_Value: 568,
        },
      ]
    }
  },

  created () {
    this.fillDataBar()
    this.fillDataLine()
    this.fillDataPie()
    this.fillDataDoughnutChart()
    this.onvariableClick()
  },

  // mounted () {
  //   this.onvariableClick()
  // },

  methods: {
    fillDataBar () {
      this.datacollectionBar = {
        labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
        datasets: [
          {
            label: 'Value',
            backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
            data: [this.getday1Value (), this.getday2Value (), this.getday3Value (), this.getday4Value (), this.getday5Value (), this.getday6Value (), this.getday7Value ()]
          }
        ]
      },
      this.optionsBar = {
        legend: {
          display: false
        },
        scales: {
          // xAxes: [{
          //   ticks: {
          //     autoSkip: true,    //자동으로 숫자 건너뛰기
          //     maxTicksLimit: 7, // x값 표시 개수
          //     maxRotation: 90,  // x값 최대 회전 각도 
          //     minRotation: 90, // x값 최소 회전 각도
          //     fontSize: 14,
          //   }
          // }],
          yAxes: [
              {
              ticks: {
                min: 0,
                // max: 1000
                //stepSize : 250
              }
            }
          ]
        },
        title: {
          display: true,
          text: 'Predict Value'
        }
      }
    },
    
    fillDataLine () {
      this.datacollectionLine = {
        labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
        datasets: [
          {
            label: 'Predict Value',
            fill: false,
            borderColor: '#34495E',
            pointBorderColor: '#249EBF',
            borderWidth: 1,
            lineTension: 0.7,
            backgroundColor: '#34495E',
            pointBackgroundColor: 'white',
            data: [this.getday1Value (), this.getday2Value (), this.getday3Value (), this.getday4Value (), this.getday5Value (), this.getday6Value (), this.getday7Value ()]
          }
        ]
      },
      this.optionsLine = {
        scales: {
          yAxes: [
              {
              ticks: {
                beginAtZero: true,
                min: 0,
                // max: 1000
                //stepSize : 250
              },
              gridLines: {
                display: true
              }
            }
          ],
          xAxes: [ 
              {
              gridLines: {
                display: false
              }
            }
          ]
        },
        legend: {
          display: true
        },
        responsive: true,
        maintainAspectRatio: false,
        // animation: {
        //   duration: 0
        // },
      }
    },

    fillDataDoughnutChart () {
      this.datacollectionDoughnut = {
        labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
        datasets: [
          {
            label: 'wnrk',
            backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
            data: [this.getday1Value (), this.getday2Value (), this.getday3Value (), this.getday4Value (), this.getday5Value (), this.getday6Value (), this.getday7Value ()]
          }
        ]
      }
    },

    fillDataPie () {
      this.datacollectionPie = {
        labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
        datasets: [
          {
            label: 'Value',
            backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
            data: [this.getday1Value (), this.getday2Value (), this.getday3Value (), this.getday4Value (), this.getday5Value (), this.getday6Value (), this.getday7Value ()]
          }
        ]
      },
      this.optionsPie = {
        legend: {
          display: true
        },
        title: {
          display: true,
          text: 'Predict Value'
        }
      }
    },

    onvariableClick () {
      this.getdate = LocalStorage.getItem("date");
      this.getstore = LocalStorage.getItem("store");
      this.getproduct = LocalStorage.getItem("item_1");
      this.getevent = LocalStorage.getItem("event_1");
      this.getbreak = LocalStorage.getItem("break_1");
      if (this.getbreak == "1") {
        this.getflag = "휴무: 일요일"
      } else if (this.getbreak == "0") {
        this.getflag = "휴무: 휴무일 없음"
      } else {
        this.getflag = "휴무일"
      }
    },

    getday1Value () {
      this.day1 = LocalStorage.getItem("day1")
      return this.day1
    },
    getday2Value () {
      this.day2 = LocalStorage.getItem("day2")
      return this.day2
    },
    getday3Value () {
      this.day3 = LocalStorage.getItem("day3")
      return this.day3
    },
    getday4Value () {
      this.day4 = LocalStorage.getItem("day4")
      return this.day4
    },
    getday5Value () {
      this.day5 = LocalStorage.getItem("day5")
      return this.day5
    },
    getday6Value () {
      this.day6 = LocalStorage.getItem("day6")
      return this.day6
    },
    getday7Value () {
      this.day7 = LocalStorage.getItem("day7")
      return this.day7
    }
  }
}
</script>

<style lang="sass">
</style>
