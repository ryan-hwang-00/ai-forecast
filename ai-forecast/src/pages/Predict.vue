<template>
  <div class="justify-center q-ma-sm">
    
    <div class="row justify-center q-col-gutter-sm q-py-sm">
      <q-chip size="18px" color="red-6" text-color="white" icon="date_range">
        {{getdate}}
      </q-chip>
      <q-chip size="18px" color="amber-10" text-color="white" icon="store">
        {{getstore}}
      </q-chip>
      <q-chip size="18px" color="blue-12" text-color="white" icon="fastfood">
        {{getproduct}}
      </q-chip>
      <q-chip size="18px" color="purple-13" text-color="white" icon="notifications_active">
        {{getevent}}
      </q-chip>
      <q-chip size="18px" color="deep-purple-8" text-color="white" icon="beach_access">
        {{getflag}}
      </q-chip>
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
          width = "500px"
          class="bg-primary text-white shadow-1 rounded-borders"
        >
          <q-carousel-slide name="style" class="column no-wrap flex-center">
                <bar-chart></bar-chart>
          </q-carousel-slide>
          
          <q-carousel-slide name="tv" class="column no-wrap flex-center">
            <!-- <div class="row justify-center q-col-gutter-sm  q-py-sm">     -->
              <!-- <div class="q-pa-sm"> -->
                <line-chart></line-chart>
              <!-- </div> -->
            <!-- </div> -->
          </q-carousel-slide>

          <q-carousel-slide name="layers" class="column no-wrap flex-center">
                <mixed-chart></mixed-chart>
          </q-carousel-slide>

        </q-carousel>
      </div>
    </div>

  </div>
</template>

<script>

    import BarChart from '../components/charts/BarChart'
    import LineChart from '../components/charts/LineChart'
    import MixedChart from '../components/charts/MixedChart'
    import { LocalStorage } from "quasar";


    export default {
        name: "Predict",
        components: {
          BarChart,
          LineChart,
          MixedChart
        },
        data () {
          return {
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
            data : [
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
        methods: {
          getLocalStoragedate: function () {
            this.getdate = LocalStorage.getItem("date");
          },

          getLocalStoragestore: function () {
            this.getstore = LocalStorage.getItem("store");
          },

          getLocalStorageproduct: function () {
            var getproduct = LocalStorage.getItem("item_1");
          },
          
          getLocalStorageevent: function () {
            this.getevent = LocalStorage.getItem("event_1");
          },

          getLocalStorageflag: function () {
            this.getflag = LocalStorage.getItem("flag");
          }

        }
    }
</script>