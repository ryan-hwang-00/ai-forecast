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
export default {
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
              data: [2478, 1267, 734, 784, 433, 341, 1342]
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
