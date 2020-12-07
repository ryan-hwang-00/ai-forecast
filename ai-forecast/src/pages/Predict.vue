<template>
  <div class="justify-center q-ma-sm">
    <!-- 예측 변수 정보 chip -->
<!-- 
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
        {{getEventDays}}
      </q-chip>
      <q-chip
        size="16px"
        color="deep-purple-8"
        text-color="white"
        icon="beach_access"
      >
        {{getflag}}
      </q-chip>
    </div> -->

    <!-- 예측 값 그래프 및 테이블 -->
    <div class="content-center" style="max-height: 30px;">
      <span class="text-Jua text-center"><h4> 주간 수요예측량</h4></span>
    </div>
    <div class="fit row  justify-around q-row-gutter-xs q-py-sm bg-grey-1">
      <!-- 예측 값 테이블 -->
        <div class="row bg-grey-1 q-pa-md">
          <q-table  
            :data="data"
            :columns="columns"
            row-key="Date"
            hide-bottom
            :pagination.sync="pagination"
            class="bg-info my-sticky-table q-pa-md shadow-3 text-Jua"
          />
        </div>
      <!-- 예측 값 그래프 캐롯셀 -->
        <div class="row bg-grey-1 q-pa-md">
          <q-carousel
            v-model="slide"
            transition-prev="scale"
            transition-next="scale"
            swipeable
            animated
            control-color="primary"
            navigation
            padding
            arrows
            class="bg-info text-white shadow-3 rounded-borders my-sticky-carousel q-pa-sm"
          >
            <q-carousel-slide name="style" class="row justify-center items-center">
                <!-- <div class="bg-grey-1 rounded-borders"> -->
                    <!-- <q-card-section class="bg-primary">
                            <div class="col">
                                <div class="text-h6 text-white text-center text-Do-Hyeon">주간 예측량</div>
                            </div>
                    </q-card-section> -->
                    <div class="bg-grey-1" style="width: 580px">
                    <bar-chart :chart-data="datacollectionBar" :options="optionsBar" :styles="myStyles"></bar-chart>
                    </div>
                <!-- </div> -->
            </q-carousel-slide>

            <q-carousel-slide name="Line" class="column flex-center">
                <div class="bg-grey-1 rounded-borders">
                    <!-- <q-card-section class="bg-primary">
                        <div class="row items-center no-wrap">
                            <div class="col">
                                <div class="text-h6 text-white text-center text-Do-Hyeon">Line Chart</div>
                            </div>
                        </div>
                    </q-card-section> -->
                    <div style="width: 580px">
                    <line-chart :chart-data="datacollectionLine" :options="optionsLine"></line-chart>
                    </div>
                </div>
            </q-carousel-slide>

            <q-carousel-slide name="ef" class="column no-wrap flex-center">
                <div class="bg-grey-1 rounded-borders">
                    <!-- <q-card-section class="bg-primary">
                        <div class="row items-center no-wrap">
                            <div class="col">
                                <div class="text-h6 text-white text-center text-Do-Hyeon">Doughnut Chart</div>
                            </div>
                        </div>
                    </q-card-section> -->
                    <div class="bg-info"> 
                        <Doughnut-chart :chart-data="datacollectionDoughnut" :options="optionsDoughnut"></Doughnut-chart>
                    </div>
                </div>
            </q-carousel-slide>

            <q-carousel-slide name="fe" class="column no-wrap flex-center">
                <div class="bg-grey-1 rounded-borders">
                    <!-- <q-card-section class="bg-primary">
                        <div class="row items-center no-wrap">
                            <div class="col">
                                <div class="text-h6 text-white text-center text-Do-Hyeon">Pie Chart</div>
                            </div>
                        </div>
                    </q-card-section> -->
                    <div class="bg-info">
                        <Pie-chart :chart-data="datacollectionPie" :options="optionsPie"></Pie-chart>
                    </div>
                </div>
            </q-carousel-slide>

          </q-carousel>
        </div>
    </div>
    
  </div>

</template> 

<script>
// import MixedChart from '../components/charts/MixedChart.vue'
import { LocalStorage } from "quasar";
import axios from "axios";
import $ from 'jquery';
import { mapGetters } from "vuex";
import LineChart from '../components/charts/LineChart.js'
import BarChart from '../components/charts/BarChart.js'
import PieChart from '../components/charts/PieChart.js'
import DoughnutChart from '../components/charts/DoughnutChart.js'

// 날씨 API URL
// https://api.openweathermap.org/data/2.5/onecall?lat=35.1333&lon=129.05&exclude=minutely&appid=a21ee35df7c2a4aec3f6efc14cd346bd&units=metric&lang=kr'

$.getJSON('https://api.openweathermap.org/data/2.5/onecall?lat=35.1333&lon=129.05&exclude=minutely&appid=a21ee35df7c2a4aec3f6efc14cd346bd&units=metric&lang=kr', 
function(data){
    this.getDay1WeatherIcon= response.daily[0].weather[0].icon
    console.log(this.getDay1WeatherIcon)
})

export default {
  
  name: "Predict",

  

  components: {
    BarChart,
    LineChart,
    PieChart,
    DoughnutChart
  },

  data () {
    return {

      // Chip Data
      // getdate: '날짜',
      // getstore: '매장명',
      // getproduct: '상품명',
      // getEventDays: '없음',
      // getflag: '휴무일',
      slide: 'style',
      Total: '',
      Mean: '',
      
      // Weather Data
      getDay1WeatherIcon: '',
      getDay2WeatherIcon: '',
      getDay3WeatherIcon: '',
      getDay4WeatherIcon: '',
      getDay5WeatherIcon: '',
      getDay6WeatherIcon: '',
      getDay7WeatherIcon: '',

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
          sortable: true,
          // classes: 'bg-grey-2',
          style: 'height: 58px;',
          // headerClasses: 'bg-grey-2 ellipsis'
        },
        // {
        //   name: 'Weather',
        //   label: '날씨',
        //   align: 'left',
        //   field: 'Weather',
        //   sortable: false,
        //   html: true,
        //   render: function (data, type, full, meta) {
        //       return "<img src=\"" + data + "\" height=\"50\"/>";
        //   },
        // },
        {
          name: 'Predict_Value',
          label: '예측 수량',
          align: 'right',
          field: 'Predict_Value',
          sortable: true,
          // classes: 'bg-grey-2',
          style: 'width: 100px;',
        },
      ],
      data: [
        {
          Date: this.getday1Date (),
          // Weather: "http://openweathermap.org/img/wn/10d@2x.png",
          Predict_Value: this.getday1Value (),
        },
        {
          Date: this.getday2Date (),
          Predict_Value: this.getday2Value (),
          // Weather: this.getDay2WeatherIcon,
        },
        {
          Date: this.getday3Date (),
          Predict_Value: this.getday3Value (),
          // Weather: this.getDay3WeatherIcon,
        },
        {
          Date: this.getday4Date (),
          Predict_Value: this.getday4Value (),
          // Weather: this.getDay4WeatherIcon,
        },
        {
          Date: this.getday5Date (),
          Predict_Value: this.getday5Value (),
          // Weather: this.getDay5WeatherIcon,
        },
        {
          Date: this.getday6Date (),
          Predict_Value: this.getday6Value (),
          // Weather: this.getDay6WeatherIcon,
        },
        {
          Date: this.getday7Date (),
          Predict_Value: this.getday7Value (),
          // Weather: this.getDay7WeatherIcon,
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
    // this.getWeather()
  },
  
  // mounted () {
  //   this.onvariableClick()
  // },

  methods: {
    // getWeather () {
    //   axios.get('https://api.openweathermap.org/data/2.5/onecall?lat=35.1333&lon=129.05&exclude=minutely&appid=a21ee35df7c2a4aec3f6efc14cd346bd&units=metric&lang=kr')
    //     .then((response) => {
    //       this.getDay1WeatherIcon= JSON.stringify(response.daily)
    //       this.getDay2WeatherIcon= JSON.stringify(response.daily[1].weather[0].icon)
    //       this.getDay3WeatherIcon= JSON.stringify(response.daily[2].weather[0].description)
    //       this.getDay4WeatherIcon= JSON.stringify(response.daily[3].weather[0].description)
    //       this.getDay5WeatherIcon= JSON.stringify(response.daily[4].weather[0].description)
    //       this.getDay6WeatherIcon= JSON.stringify(response.daily[5].weather[0].description)
    //       this.getDay7WeatherIcon= JSON.stringify(response.daily[6].weather[0].description)
    //       console.log("Day1WWWWICON",this.getDay1WeatherIcon )
    //     })
    // },

    //'<img src="~assets/Weather/' + 아이콘 + '.png" alt=""/>'

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
      this.myStyles = {height: '400px',
        width: '100%',
        position: 'relative',

      },
      this.optionsBar = {
        legend: {
          display: false,
          labels: {
            usePointStyle: true,
            boxWidth: 5
          }
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
              },
              gridLines : {
                display: true
              }
            }
          ],
          xAxes: [
              {
              gridLines : {
                display: false
              }
            }
          ]
        },
        title: {
          display: true,
          text: 'Predict Value'
        },
        responsive: true,
        maintainAspectRatio: false,
        height: 100,
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
            borderWidth: 2.4,
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
      this.optionsDoughnut = {
        legend: {
          display: true
        },
        title: {
          display: true,
          text: 'Predict Value'
        }
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
      this.getbreak = LocalStorage.getItem("break_1");
      if (this.getbreak === "1") {
        this.getflag = "휴무: 일요일"
      } else if (this.getbreak == "0") {
        this.getflag = "휴무: 휴무일 없음"
      } else {
        this.getflag = "휴무일"
      };
      this.getEventDays = LocalStorage.getItem('edate')
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

    getTotal() {
      this.Total = (this.getday1Value() + this.getday2Value() + this.getday3Value()+
                    this.getday4Value() + this.getday5Value() + this.getday6Value() + this.getday7Value())
    },
    getMean() {
      this.Mean = (this.getday1Value() + this.getday2Value() + this.getday3Value()+
                    this.getday4Value() + this.getday5Value() + this.getday6Value() + this.getday7Value())/7
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
.my-sticky-table
  /* height or max-height is important */
  // overflow: auto
  height: 520px
  width: 300px
  // max-width: 15rem
.my-sticky-carousel
  /* height or max-height is important */
  // overflow: auto
  height: 520px
  width: 700px
  // max-width: 60rem
.my-sticky-chart
  /* height or max-height is important */
  // overflow: auto
  height: 450px
  width: 550px
  // max-width: 60rem
  

</style>
