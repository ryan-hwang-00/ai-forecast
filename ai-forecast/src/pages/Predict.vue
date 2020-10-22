<template>
  <div class="q-pa-xl">
     
     <div class="q-gutter-sm">
      <q-chip clickable @click="onClick" color="red-6" text-color="white" icon="date_range">
       날짜
      </q-chip>
      <q-chip clickable @click="onClick" color="yellow-10" text-color="white" icon="fastfood">
       상품명
      </q-chip>
      <q-chip clickable @click="onClick" color="purple-13" text-color="white" icon="notifications_active">
        행사
      </q-chip>
      <q-chip clickable @click="onClick" color="deep-purple-8" text-color="white" icon="beach_access">
        휴무
      </q-chip>
    </div>

    <div class="q-pa-md">
      <q-table
        title="주간 예측량"
        :data="data1"
        :columns="columns"
        row-key="name"
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

  methods: {
    onItemClick () {
      console.log('Clicked on an Item')
      alert('안녕하세요.')
      this.lorem = 'abcde'
    }
  },

  methods: {
    onClick () {
      console.log(onItemClick)
      this.lorem = '신라면멀티'
    }
  },

  // data () {
  //   return {
  //     columns: [
  //       {
  //         name: 'name',
  //         required: true,
  //         label: 'Dessert (100g serving)',
  //         align: 'left',
  //         field: row => row.name,
  //         format: val => `${val}`,
  //         sortable: true
  //       },
  //       { name: 'calories', align: 'center', label: 'Calories', field: 'calories', sortable: true },
  //       { name: 'fat', label: 'Fat (g)', field: 'fat', sortable: true },
  //       { name: 'carbs', label: 'Carbs (g)', field: 'carbs' },
  //       { name: 'protein', label: 'Protein (g)', field: 'protein' },
  //       { name: 'sodium', label: 'Sodium (mg)', field: 'sodium' },
  //       { name: 'calcium', label: 'Calcium (%)', field: 'calcium', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) },
  //       { name: 'iron', label: 'Iron (%)', field: 'iron', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) }
  //     ],
  //     data1 : [
  //       {
  //         name: 'Frozen Yogurt',
  //         calories: 159,
  //         fat: 6.0,
  //         carbs: 24,
  //         protein: 4.0,
  //         sodium: 87,
  //         calcium: '14%',
  //         iron: '1%'
  //       },
  //       {
  //         name: 'Ice cream sandwich',
  //         calories: 237,
  //         fat: 9.0,
  //         carbs: 37,
  //         protein: 4.3,
  //         sodium: 129,
  //         calcium: '8%',
  //         iron: '1%'
  //       },
  //       {
  //         name: 'Eclair',
  //         calories: 262,
  //         fat: 16.0,
  //         carbs: 23,
  //         protein: 6.0,
  //         sodium: 337,
  //         calcium: '6%',
  //         iron: '7%'
  //       },
  //       {
  //         name: 'Cupcake',
  //         calories: 305,
  //         fat: 3.7,
  //         carbs: 67,
  //         protein: 4.3,
  //         sodium: 413,
  //         calcium: '3%',
  //         iron: '8%'
  //       },
  //       {
  //         name: 'Gingerbread',
  //         calories: 356,
  //         fat: 16.0,
  //         carbs: 49,
  //         protein: 3.9,
  //         sodium: 327,
  //         calcium: '7%',
  //         iron: '16%'
  //       },
  //       {
  //         name: 'Jelly bean',
  //         calories: 375,
  //         fat: 0.0,
  //         carbs: 94,
  //         protein: 0.0,
  //         sodium: 50,
  //         calcium: '0%',
  //         iron: '0%'
  //       },
  //       {
  //         name: 'Lollipop',
  //         calories: 392,
  //         fat: 0.2,
  //         carbs: 98,
  //         protein: 0,
  //         sodium: 38,
  //         calcium: '0%',
  //         iron: '2%'
  //       },
  //       {
  //         name: 'Honeycomb',
  //         calories: 408,
  //         fat: 3.2,
  //         carbs: 87,
  //         protein: 6.5,
  //         sodium: 562,
  //         calcium: '0%',
  //         iron: '45%'
  //       },
  //       {
  //         name: 'Donut',
  //         calories: 452,
  //         fat: 25.0,
  //         carbs: 51,
  //         protein: 4.9,
  //         sodium: 326,
  //         calcium: '2%',
  //         iron: '22%'
  //       },
  //       {
  //         name: 'KitKat',
  //         calories: 518,
  //         fat: 26.0,
  //         carbs: 65,
  //         protein: 7,
  //         sodium: 54,
  //         calcium: '12%',
  //         iron: '6%'
  //       }
  //     ]
  //   }
  // }
}
</script>



