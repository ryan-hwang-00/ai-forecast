<template>
    <div class="q-pa-md">
      <q-table
        title="주간 예측량"
        :data="data"
        :columns="columns"
        row-key="Date"
      />
    </div>
</template>

<script>
export default {
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
      data : [textGetJson,
        // {
        //   Date: '2020-10-23',
        //   Predict_Value: 118,
        // },
        // {
        //   Date: '2020-10-24',
        //   Predict_Value: 131,
        // },
        // {
        //   Date: '2020-10-25',
        //   Predict_Value: 159,
        // },
        // {
        //   Date: '2020-10-26',
        //   Predict_Value: 182,
        // },
        // {
        //   Date: '2020-10-27',
        //   Predict_Value: 159,
        // },
        // {
        //   Date: '2020-10-28',
        //   Predict_Value: 284,
        // },
        // {
        //   Date: '2020-10-29',
        //   Predict_Value: 568,
        // },
        ,
      ]
    }
  },

  methods: {
    getLocalStorage: function () {
      this.textGetLocal = LocalStorage.getItem("textSetLocal");
    },

    getMultiLocalStorage: function () {
      //json to string 형태로 변환
      this.textGetJson = JSON.stringify(LocalStorage.getItem("textSetJson"));

    },
  }
}
</script>