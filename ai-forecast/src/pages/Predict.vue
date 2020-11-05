<template>
  <div class="q-pa-xl">
     
     <div class="q-gutter-sm">
      <q-chip color="red-6" text-color="white" icon="date_range">
        날짜
      </q-chip>
      <q-chip color="amber-10" text-color="white" icon="store">
        매장명
      </q-chip>
      <q-chip color="blue-12" text-color="white" icon="fastfood">
        상품명
      </q-chip>
      <q-chip color="purple-13" text-color="white" icon="notifications_active">
        행사
      </q-chip>
      <q-chip color="deep-purple-8" text-color="white" icon="beach_access">
        휴무
      </q-chip>
    </div>

    <div class="q-pa-md">
      <q-table
        title="주간 예측량"
        :data="data"
        :columns="columns"
        row-key="Date"
      />
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
        <q-carousel-slide name="style" class="column no-wrap flex-center">
          <q-icon name="style" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem1 }}
          </div>
        </q-carousel-slide>
        <q-carousel-slide name="tv" class="column no-wrap flex-center">
          <q-icon name="card_travel" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem2 }}
          </div>
        </q-carousel-slide>
        <q-carousel-slide name="layers" class="column no-wrap flex-center">
          <q-icon name="layers" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem3 }}
          </div>
        </q-carousel-slide>
        <q-carousel-slide name="map" class="column no-wrap flex-center">
          <q-icon name="terrain" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem4 }}
          </div>
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>


<script>
export default {
  data () {

    return {
      slide: 'style',
      lorem1: '주간 예측 판매량',
      lorem2: '전년 동기 비교 그래프',
      lorem3: '전월 동기 비교 그래프',
      lorem4: '뭐 넣을까 고민중...',
    }
    
  },

  data () {
    return {
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
    }
  }
}
</script>