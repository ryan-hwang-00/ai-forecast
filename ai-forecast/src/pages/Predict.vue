<template>
  <div class="justify-center q-ma-sm">

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
       <q-btn
        color="white"
        text-color="black"
        label="예측 정보 불러오기"
        @click="onPredictClick()"
      />
    </div>

    <div class="row justify-center q-col-gutter-sm q-py-sm">
      <div class="col-md-4 col-md-6 col-lg-6 col-lg-10 col-xs-12 q-pa-sm">
        <q-table
          title="주간 예측량"
          :data="data"
          :columns="columns"
          row-key="Date"
        />
      </div>

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
          height="700px"
          width="500px"
          class="bg-primary text-white shadow-1 rounded-borders"
        >
          <q-carousel-slide
            name="style"
            class="column no-wrap flex-center"
          >
            <bar-chart :chart-data="datacollectionBar"></bar-chart>
          </q-carousel-slide>

          <q-carousel-slide
            name="tv"
            class="column no-wrap flex-center"
          >
            <line-chart v-if="loaded" :chart-data="datacollectionLine"></line-chart>
          </q-carousel-slide>

          <q-carousel-slide
            name="layers"
            class="column no-wrap flex-center"
          >
            <mixed-chart></mixed-chart>
          </q-carousel-slide>

          <q-carousel-slide
            name="ef"
            class="column no-wrap flex-center"
          >
            <pie-chart></pie-chart>
          </q-carousel-slide>

        </q-carousel>
      </div>
    </div>

  </div>
</template>

<script>
import PieChart from '../components/charts/PieChart'
import MixedChart from '../components/charts/MixedChart'
import { LocalStorage } from "quasar";
import LineChart from '../components/charts/LineChart.js'
import BarChart from '../components/charts/BarChart.js'

export default {
  name: "Predict",
  components: {
    BarChart,
    LineChart,
    PieChart,
    MixedChart
  },
  data () {
    return {
      datacollectionBar: null,
      datacollectionLine: null,
      getdate: '날짜',
      getstore: '매장명',
      getproduct: '상품명',
      getevent: '행사',
      getflag: '휴무일',
      slide: 'style',

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
      // Chart Data
    }
  },

  created () {
    this.fillDataBar()
    this.fillDataLine()
    this.onPredictClick()
  },

  // mounted () {
  //   this.fillDataBar()
  //   this.fillDataLine()
  //   this.onPredictClick()
  // },

  methods: {
    fillDataBar () {
      this.datacollectionBar = {
        labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
        datasets: [
          {
            label: 'Value',
            backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
            // Data for the x-axis of the chart
            data: [120, 22, 20, 333, 22, 333, 22]
          }
        ]
      }
      // BarChart.update();
    },
    fillDataLine () {
      this.datacollectionLine = {
        labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
        datasets: [{
          data: [120, 22, 33, 44, 1, 33, 222],
          label: 'Predict Value',
          borderColor: 'white',
          fill: false,
          lineTension: 0.7
        }
        ]
      }
    },

    onPredictClick: function () {
      this.getdate = LocalStorage.getItem("date");
      this.getstore = LocalStorage.getItem("store");
      this.getproduct = LocalStorage.getItem("item_1");
      this.getevent = LocalStorage.getItem("event_1");
      this.getbreak = LocalStorage.getItem("break_1");
      if (this.getbreak == "1") {
        this.getflag = "휴무: 일요일";        
      } else {
        this.getflag = "휴무: 휴무일 없음"
      }
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    },
    // fillData () {
    //   this.datacollection = {
    //     labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
    //     datasets: [
    //       {
    //         label: 'Value',
    //         backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
    //         // Data for the x-axis of the chart
    //         data: [this.getLocalStorageproduct(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
    //       }
    //     ]
    //   }
    // },
    // getRandomInt () {
    //   return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    // }
  }
}
</script>
