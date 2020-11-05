<template>
  <div class="justify-center q-ma-sm">
    <div class="row justify-center q-ma-sm">
      <q-chip label="getitem()" size="18px" color="red-6" text-color="white" icon="date_range"/>
      <q-chip label="매장명" size="18px" color="amber-10" text-color="white" icon="store"/>
      <q-chip label="상품명" size="18px" color="blue-12" text-color="white" icon="fastfood"/>
      <q-chip label="행사" size="18px" color="purple-13" text-color="white" icon="notifications_active"/>
      <q-chip label="휴무" size="18px" color="deep-purple-8" text-color="white" icon="beach_access"/>
    </div>

    <div class="row justify-center q-col-gutter-sm  q-py-sm">    
      <div class="col-md-4 col-md-6 col-lg-6 col-lg-10 col-xs-12 q-pa-sm">
        <table1></table1>
      </div>
    </div>

    <div class="q-gutter-md">
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
        height="500px"
        class="bg-primary text-white shadow-1 rounded-borders"
      >
        <q-carousel-slide name="style" class="justify-center q-pa-lg">
          <bar-chart2></bar-chart2>
        </q-carousel-slide>
        <!-- <q-carousel-slide name="tv" class="column no-wrap flex-center">
          <line-chart></line-chart>
        </q-carousel-slide> -->
      </q-carousel>
    </div>

    <div class="row justify-center q-col-gutter-sm  q-py-sm">    
      <div class="col-md-6 col-md-8 col-xs-12 q-pa-sm">
        <bar-chart></bar-chart>
      </div>
    </div>

    <div class="row justify-center q-col-gutter-sm  q-py-sm">    
      <div class="col-md-4 col-md-8 col-xs-12 q-pa-sm">
        <line-chart></line-chart>
      </div>
    </div>

  </div>
</template>

<script>
import BarChart from '../components/charts/BarChart'
import LineChart from '../components/charts/LineChart'
import table1 from '../components/table/table1'


export default {
  name: 'PageIndex',
  components: {
    BarChart,
    BarChart2,
    LineChart,
    table1
  },
  data () {
    return {}
  }
}
</script>