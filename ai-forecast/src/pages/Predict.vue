<template>
  <div class="justify-center q-ma-sm">
    <!-- 예측 변수 정보 chip -->
    <div class="row justify-center q-col-gutter-sm q-py-sm">
      <q-chip
        size="16px"
        color="red-6"
        text-color="white"
        icon="date_range"
        label="기준일:"
      >
        {{getdate}}
      </q-chip>
      <q-chip
        size="16px"
        color="amber-10"
        text-color="white"
        icon="store"
      >
        {{getstore}}
      </q-chip>
      <q-chip
        size="16px"
        color="blue-12"
        text-color="white"
        icon="fastfood"
        label="상품:"
      >
        {{getproduct}}
      </q-chip>
      <q-chip
        size="16px"
        color="purple-13"
        text-color="white"
        icon="notifications_active"
        label="할인행사:"
      >
        {{getevent}}
      </q-chip>
      <q-chip
        size="16px"
        color="deep-purple-8"
        text-color="white"
        icon="beach_access"
      >
        {{getflag}}
      </q-chip>
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
          :pagination.sync="pagination"
        />
      </div>

    </div>

  </div>
</template> 

<script>
import MixedChart from '../components/charts/MixedChart.vue'
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
      geteventmon: '',
      geteventtue: '',
      geteventweb: '',
      geteventthu: '',
      geteventfri: '',
      geteventsat: '',
      geteventsun: '',
      geteventday: '',
      
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
          Date: this.getday1Date (),
          Predict_Value: this.getday1Value (),
        },
        {
          Date: this.getday2Date (),
          Predict_Value: this.getday2Value (),
        },
        {
          Date: this.getday3Date (),
          Predict_Value: this.getday3Value (),
        },
        {
          Date: this.getday4Date (),
          Predict_Value: this.getday4Value (),
        },
        {
          Date: this.getday5Date (),
          Predict_Value: this.getday5Value (),
        },
        {
          Date: this.getday6Date (),
          Predict_Value: this.getday6Value (),
        },
        {
          Date: this.getday7Date (),
          Predict_Value: this.getday7Value (),
        },
      ],
      pagination: {
        // sortBy: 'desc',
        // descending: false,
        page: 1,
        rowsPerPage: 7,
        // rowsNumber: 10
      },
    }
  },
  created () {
    this.fillDataBar()
    this.fillDataLine()
    this.fillDataPie()
    this.fillDataDoughnutChart()
    this.onvariableClick()
    this.onEventClick ()
  },
  // mounted () {
  //   this.onvariableClick()
  // },

  methods: {
    fillDataBar () {
      this.datacollectionBar = {
        labels : [
            this.getday1Date(),
            this.getday2DateMMDD(),
            this.getday3DateMMDD(),
            this.getday4DateMMDD(),
            this.getday5DateMMDD(),
            this.getday6DateMMDD(),
            this.getday7DateMMDD()
        ],
        datasets: [
          {
            label: 'Value',
            backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
            data: [
                this.getday1Value(),
                this.getday2Value(),
                this.getday3Value(),
                this.getday4Value(),
                this.getday5Value(),
                this.getday6Value(),
                this.getday7Value()
            ]
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
        labels: [
            this.getday1Date(),
            this.getday2DateMMDD(),
            this.getday3DateMMDD(),
            this.getday4DateMMDD(),
            this.getday5DateMMDD(),
            this.getday6DateMMDD(),
            this.getday7DateMMDD()
        ],
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
            data: [
                this.getday1Value(),
                this.getday2Value(),
                this.getday3Value(),
                this.getday4Value(),
                this.getday5Value(),
                this.getday6Value(),
                this.getday7Value()
            ]
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
        labels: [
            this.getday1DateMMDD(),
            this.getday2DateMMDD(),
            this.getday3DateMMDD(),
            this.getday4DateMMDD(),
            this.getday5DateMMDD(),
            this.getday6DateMMDD(),
            this.getday7DateMMDD()
        ],
        datasets: [
          {
            label: 'wnrk',
            backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
            data: [
                this.getday1Value(),
                this.getday2Value(),
                this.getday3Value(),
                this.getday4Value(),
                this.getday5Value(),
                this.getday6Value(),
                this.getday7Value()
            ]
          }
        ]
      }
    },

    fillDataPie () {
      this.datacollectionPie = {
        labels: [
            this.getday1DateMMDD(),
            this.getday2DateMMDD(),
            this.getday3DateMMDD(),
            this.getday4DateMMDD(),
            this.getday5DateMMDD(),
            this.getday6DateMMDD(),
            this.getday7DateMMDD()
        ],
        datasets: [
          {
            label: 'Value',
            backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
            data: [
                this.getday1Value(),
                this.getday2Value(),
                this.getday3Value(),
                this.getday4Value(),
                this.getday5Value(),
                this.getday6Value(),
                this.getday7Value()
            ]
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
      this.getproduct = LocalStorage.getItem("item_1");
      this.getshop = LocalStorage.getItem("store_code");
      if (this.getshop === "1") {
        this.getstore = "매장: 해운대점"
      } else if (this.getshop == "6") {
        this.getstore = "매장: 광안리점"
      } else {
        this.getstore = "매장"
      };
      this.getevent = LocalStorage.getItem("event_1");
      this.getbreak = LocalStorage.getItem("break_1");
      if (this.getbreak === "1") {
        this.getflag = "휴무: 일요일"
      } else if (this.getbreak == "0") {
        this.getflag = "휴무: 휴무일 없음"
      } else {
        this.getflag = "휴무일"
      };
    },

    onEventClick () {
      this.getmon = LocalStorage.getItem('event_mon')
      this.gettue = LocalStorage.getItem('event_tue')
      this.getthu = LocalStorage.getItem('event_thu')
      this.getwen = LocalStorage.getItem('event_wen')
      this.getsat = LocalStorage.getItem('event_sat')
      this.getsun = LocalStorage.getItem('event_sun')
      this.getfri = LocalStorage.getItem('event_fri')
      if (this.getmon == "true") {
        this.geteventmon = "월요일"
      } else {
        this.geteventmon = ""
      };
      if (this.gettue == "true") {
        this.geteventtue = "화요일"
      } else {
        this.geteventtue = ""
      };
      geteventweb ()
      if (this.getwen == "true") {
        this.geteventweb = "수요일"
      } else {
        this.geteventweb = ""
      };
      geteventthu ()
      if (this.getthu == "true") {
        this.geteventthu = "목요일"
      } else {
        this.geteventthu = ""
      };
      geteventfri ()
      if (this.getfri == "true") {
        this.geteventfri = "금요일"
      } else {
        this.geteventfri = ""
      };
      geteventsat ()
      if (this.getsat == "true") {
        this.geteventsat = "토요일"
      } else {
        this.geteventsat = ""
      };
      geteventsun ()
      if (this.getsun == "true") {
        this.geteventsun = "일요일"
      } else {
        this.geteventsun = ""
      };
      var dayArr = [this.getmon, this.gettue, this.getwen, this.getthu, this.getfri, this.getsat, this.getsun]
      var days = [this.geteventmon (), this.geteventtue (), this.geteventweb (), this.geteventthu (), this.geteventfri (), this.geteventsat (), this.geteventsun ()]
      console.log("dayArr", dayArr[i])
      for (let i = 0; i < dayArr.length; i++) {
        if (dayArr[i] == "true") {
          return this.getevent = days[i]
        }
      };
    },

    // Predict-Value Data
    getday1Value () {
      this.day1 = LocalStorage.getItem("Tday1")
      return this.day1
    },
    getday2Value () {
      this.day2 = LocalStorage.getItem("Tday2")
      return this.day2
    },
    getday3Value () {
      this.day3 = LocalStorage.getItem("Tday3")
      return this.day3
    },
    getday4Value () {
      this.day4 = LocalStorage.getItem("Tday4")
      return this.day4
    },
    getday5Value () {
      this.day5 = LocalStorage.getItem("Tday5")
      return this.day5
    },
    getday6Value () {
      this.day6 = LocalStorage.getItem("Tday6")
      return this.day6
    },
    getday7Value () {
      this.day7 = LocalStorage.getItem("Tday7")
      return this.day7
    },

    // Date Data
    getday1Date () {
      this.day1Date = LocalStorage.getItem("day1")
      return this.day1Date
    },
    getday2Date () {
      this.day2Date = LocalStorage.getItem("day2")
      return this.day2Date
    },
    getday3Date () {
      this.day3Date = LocalStorage.getItem("day3")
      return this.day3Date
    },
    getday4Date () {
      this.day4Date = LocalStorage.getItem("day4")
      return this.day4Date
    },
    getday5Date () {
      this.day5Date = LocalStorage.getItem("day5")
      return this.day5Date
    },
    getday6Date () {
      this.day6Date = LocalStorage.getItem("day6")
      return this.day6Date
    },
    getday7Date () {
      this.day7Date = LocalStorage.getItem("day7")
      return this.day7Date
    },

    // Date Data MMDD
    getday1DateMMDD () {
      this.day1DateMMDD = this.day1Date.substring(5,10)
      return this.day1DateMMDD
    },
    getday2DateMMDD () {
      this.day2DateMMDD = this.day2Date.substring(5,10)
      return this.day2DateMMDD
    },
    getday3DateMMDD () {
      this.day3DateMMDD = this.day3Date.substring(5,10)
      return this.day3DateMMDD
    },
    getday4DateMMDD () {
      this.day4DateMMDD = this.day4Date.substring(5,10)
      return this.day4DateMMDD
    },
    getday5DateMMDD () {
      this.day5DateMMDD = this.day5Date.substring(5,10)
      return this.day5DateMMDD
    },
    getday6DateMMDD () {
      this.day6DateMMDD = this.day6Date.substring(5,10)
      return this.day6DateMMDD
    },
    getday7DateMMDD () {
      this.day7DateMMDD = this.day7Date.substring(5,10)
      return this.day7DateMMDD
    },
  }
}
</script>

<style lang="sass">
</style>
