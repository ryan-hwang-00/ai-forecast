<template>

  <main class="q-page q-pa-sm" style="min-height: 704px;">

    <!-- main 이 있으면 그 아래에 같은 class인 div 여러 개 쓸 수 있음 -->

  <div class="row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly" >  <!-- div 2 -->
    <q-btn-dropdown color="primary" size="15px" label="상품명">
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

  </div>
  <div class="q-pa-md">
    <div class="row justify-evenly content-center">
  <!-- <div class="row q-col-gutter-sm q-py-md content-center items-center justify-evenly" >  div 3 -->

      <q-btn-dropdown color="primary" size="15px" label="상품명">
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


    <q-btn-dropdown color="primary" size="15px" label="상품명">
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


    <q-btn-dropdown color="primary" size="15px" label="상품명">
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


    <q-btn-dropdown color="primary" size="15px" label="상품명">
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

    </div> <!-- test div -->
  
  
  </div>

  </main>
</template>