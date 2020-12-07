<template>
  <q-card class="bg-white full-width">
    <q-card-section class="bg-primary">
      <div class="row items-center no-wrap">
        <div class="col">
          <div class="text-h6 text-white text-center">Line Chart</div>
        </div>
      </div>
    </q-card-section>
    <q-card-section>
      <canvas id="line-chart"></canvas>
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
    this.createChart('line-chart')
  },
  methods: {
    createChart (chartId) {
      const ctx = document.getElementById(chartId)
      const myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
          datasets: [{
            data: [localStorage.day1, localStorage.day2, localStorage.day3, localStorage.day4, localStorage.day5, localStorage.day6, localStorage.day7],
            label: 'Value',
            borderColor: '#34495E',
            fill: false,
            lineTension: 0.9
          }
          ]
        },
        options: {
          legend: {
            display: false
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
