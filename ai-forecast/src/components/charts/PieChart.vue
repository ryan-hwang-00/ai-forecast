<template>
  <q-card class="bg-white full-width">
    <q-card-section class="bg-primary">
      <div class="row items-center no-wrap">
        <div class="col">
          <div class="text-h6 text-white text-center">Pie Chart</div>
        </div>
      </div>
    </q-card-section>
    <q-card-section>
      <canvas id="pie-chart"></canvas>
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
    this.createChart('pie-chart')
  },
  methods: {
    createChart (chartId) {
      const ctx = document.getElementById(chartId)
      const myChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
          datasets: [{
            label: 'Value',
            backgroundColor: ['#FA6060', '#FFD85B', '#D8F961', '#81D071', '#8193D5', '#6C349D', '#1D2758'],
            data: [localStorage.day1, localStorage.day2, localStorage.day3, localStorage.day4, localStorage.day5, localStorage.day6, localStorage.day7]
          }]
        },
        options: {
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
