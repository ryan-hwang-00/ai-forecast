<template>
  <q-card class="bg-white q-pa-none full-width">
    <q-card-section class="bg-primary">
      <div class="row items-center no-wrap">
        <div class="col">
          <div class="text-h6 text-white text-center">Bar Chart</div>
        </div>
      </div>
    </q-card-section>
    <q-card-section>
      <canvas id="bar-chart"></canvas>
    </q-card-section>
  </q-card>
</template>

<script>
import Chart from 'chart.js'
const { reactiveProp } = mixins;

export default {
  extends: Bar,
  mixins: [reactiveProp],
  props: ["options"],
  data () {
    return {
    }
  },
  mounted () {
    this.createChart('bar-chart')
  },
  methods: {
    createChart (chartId) {
      const ctx = document.getElementById(chartId)
      const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
          datasets: [
            {
              label: 'Value',
              backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
              data: [localStorage.day1, localStorage.day2, localStorage.day3, localStorage.day4, localStorage.day5, localStorage.day6, localStorage.day7]
            }
          ]
        },
        options: {
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
            yAxes: [{
                ticks: {
                  min: 0,
                  max: 2500
                  //stepSize : 250
                }
            }]
          },

          title: {
            display: true,
            text: 'Predict Value'
          }
          
        }
      })
      return myChart
    }
  }
}
</script>

<style>
</style>
