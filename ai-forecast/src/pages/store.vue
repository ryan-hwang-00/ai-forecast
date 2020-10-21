<template>
  <main class="q-page q-pa-sm" style="min-height: 704px;">
    <br/>
    <br/>
    <div class="row  q-col-gutter-sm  q-py-xl content-center items-center justify-evenly" >
      <q-btn color="yellow-10"
      clickable
       @click="on1ItemClick"
       to="/item">
        <q-icon left size="5em" name="store" /> 
        <div>store 1</div>
      </q-btn>
      <q-btn q-btn color="pink"
      clickable
       @click="on2ItemClick"
       to="/item">
        <q-icon left size="5em" name="store" /> 
        <div>store 2</div>
      </q-btn>  
      <!-- <q-btn color="yellow-10" icon-right="store" label="store 1" />
      <q-btn color="pink" icon-right="store" label="store 2" /> -->
    </div> 
  </main>
</template>

<script>
export default {
  data () {
    return {
  }
  },
  methods: {
    on1ItemClick () {
      console.log('store1')
    },
    on2ItemClick () {
      console.log('store2')
    }
  }
}
</script>