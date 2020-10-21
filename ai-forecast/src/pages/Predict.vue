<template>
  <div class="q-pa-md">
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
  }
}
</script>