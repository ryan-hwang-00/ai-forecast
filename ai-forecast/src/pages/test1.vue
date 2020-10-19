<template>
  
  

  <div class="row q-pa-md justify-around">

    <q-btn-dropdown color="primary" label="상품명">
      <q-list>
        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>백산수 2L</q-item-label>                      <!-- 1 -->
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>백산수 500ml</q-item-label>                   <!-- 2 -->
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>신라면 멀티</q-item-label>                    <!-- 3 -->
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>안성탕면 멀티</q-item-label>                  <!-- 4 -->
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>진라면 멀티(순한맛)</q-item-label>            <!-- 5 -->
          </q-item-section>
        </q-item>   
      </q-list>
    </q-btn-dropdown>
  

    <!-- 두 번째 버튼 추가해봄 -->
    <q-btn-dropdown color="primary" label="행사구분">
      <q-list>
        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>할인없음</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>할인진행</q-item-label>
          </q-item-section>
        </q-item>        
      </q-list>
    </q-btn-dropdown>


    <!-- 세 번째 버튼 -->
    <q-btn-dropdown color="primary" label="휴무">
      <q-list>
        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>정상영업</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>매장휴무</q-item-label>
          </q-item-section>
        </q-item>        
      </q-list>
    </q-btn-dropdown>

<!-- 날짜 선택창  -->
    <!-- <div class="q-pb-sm">
      Model: {{ model }}
    </div>

    <q-date v-model="model" range /> -->
<!-- 날짜 선택창  -->


    <!-- 네 번째 버튼 -->
    <!-- <q-btn-dropdown color="primary" label="광고등급">
      <q-list>
        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>정상영업</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>매장휴무</q-item-label>
          </q-item-section>
        </q-item>        
      </q-list>
    </q-btn-dropdown> -->


    

  
  </div>
    

  

</template>