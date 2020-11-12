<template>
  <q-card class="bg-white full-width">
    <q-card-section class="bg-primary">
      <div class="row items-center no-wrap">
        <div class="col">
          <div class="text-h6 text-white text-center">Mixed Chart</div>
        </div>
      </div>
    </q-card-section>
    <q-card-section>
      <canvas id="mixed-chart" height="80px" ></canvas>
    </q-card-section>
  </q-card>
</template>

<script>
import Chart from 'chart.js'
export default {
  data () {
    return {
    }
  },
  mounted () {
    this.createChart('mixed-chart')
  },
  methods: {
    createChart (chartId) {
      const ctx = document.getElementById(chartId)
      const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
          datasets: [{
            label: 'Value1',
            type: 'line',
            borderColor: '#8e5ea2',
            data: [localStorage.day1, localStorage.day2, localStorage.day3, localStorage.day4, localStorage.day5, localStorage.day6, localStorage.day7],
            fill: false
          }, {
            label: 'Value2',
            type: 'line',
            borderColor: '#3e95cd',
            data: [2478, 1267, 734, 784, 433, 341, 1342],
            fill: false
          }, {
            label: 'Value1',
            type: 'bar',
            backgroundColor: 'rgba(0,0,0,0.2)',
            data: [localStorage.day1, localStorage.day2, localStorage.day3, localStorage.day4, localStorage.day5, localStorage.day6, localStorage.day7]
          }, {
            label: 'Value2',
            type: 'bar',
            backgroundColor: 'rgba(0,0,0,0.2)',
            backgroundColorHover: '#3e95cd',
            data: [2478, 1267, 734, 784, 433, 341, 1342]
          }
          ]
        },
        options: {
          title: {
            display: true,
            text: 'Value'
          },
          legend: { display: false }
        }
      })
      return myChart
    }
  }
}
</script>

<style>
</style>
