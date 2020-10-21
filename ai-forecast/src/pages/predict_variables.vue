<template>
  <div class="q-pa-md doc-container">
    <div class="row justify-around">
      <q-btn-dropdown
        color="primary"
        label="상품명"
      >
        <q-list>
          <q-item
            clickable
            v-close-popup
            @click="onItemClick"
          >
            <q-item-section>
              <q-item-label>백산수 2L</q-item-label> <!-- 1 -->
            </q-item-section>
          </q-item>

          <q-item
            clickable
            v-close-popup
            @click="onItemClick"
          >
            <q-item-section>
              <q-item-label>백산수 500ml</q-item-label> <!-- 2 -->
            </q-item-section>
          </q-item>

          <q-item
            clickable
            v-close-popup
            @click="onItemClick"
          >
            <q-item-section>
              <q-item-label>신라면 멀티</q-item-label> <!-- 3 -->
            </q-item-section>
          </q-item>

          <q-item
            clickable
            v-close-popup
            @click="onItemClick"
          >
            <q-item-section>
              <q-item-label>안성탕면 멀티</q-item-label> <!-- 4 -->
            </q-item-section>
          </q-item>

          <q-item
            clickable
            v-close-popup
            @click="onItemClick"
          >
            <q-item-section>
              <q-item-label>진라면 멀티(순한맛)</q-item-label> <!-- 5 -->
            </q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>

      <q-btn-dropdown
        color="primary"
        label="행사구분"
      >
        <q-list>
          <q-item
            clickable
            v-close-popup
            @click="onItemClick"
          >
            <q-item-section>
              <q-item-label>할인없음</q-item-label>
            </q-item-section>
          </q-item>

          <q-item
            clickable
            v-close-popup
            @click="onItemClick"
          >
            <q-item-section>
              <q-item-label>할인진행</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>

      <q-btn-dropdown
        color="primary"
        label="휴무"
      >
        <q-list>
          <q-item
            clickable
            v-close-popup
            @click="onItemClick"
          >
            <q-item-section>
              <q-item-label>정상영업</q-item-label>
            </q-item-section>
          </q-item>

          <q-item
            clickable
            v-close-popup
            @click="onItemClick"
          >
            <q-item-section>
              <q-item-label>매장휴무</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>

    </div>

    <br />
    <!-- <br/> -->

    <!-- <div class="column items-center" style="height: 100px"> -->

    <!-- <div class="col-1">  </div>
          <div class="col-1"> 11 </div>
          <div class="col-1"> 22 </div> -->
    <!-- <div class="col-1 self-center"> 11 </div> -->

    <!-- </div>   -->
    <!-- column items-center 끝 -->

    <div
      class="column items-center"
      style="height: 50px"
    >
      <div class="q-pa-md">

        <div class="col-1 q-pb-sm">{{ model }}</div>
        <q-date
          v-model="model"
          range
        />
      </div>
    </div>

  </div>

</template>