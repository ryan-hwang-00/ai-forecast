<template>
  <main
    class="q-page q-pa-sm"
    style="min-height: 704px;"
  >
    <br />
    <br />
    <div class="row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly">
      <q-avatar
        rounded
        size="300px"
      >
        <img src="~assets/FMLogo2.svg">
      </q-avatar>
    </div>

    <div class="row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly">
      <q-card-section class="text-center q-pa-none">
        <p class="text-grey-10">포카머신을 시작해 볼까요?</p>

        <q-btn
          rounded
          standout
          v-model=text
          label="Start"
          to="/login"
        />

      </q-card-section>
    </div>

  </main>
</template>