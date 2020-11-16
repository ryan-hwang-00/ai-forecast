<template>
  <div class="TextEffect2">
    <span class="item delay-anime delay-color">
        Foreca Machine
    </span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: 'Foreca Machine'
    }
  }
}
</script>

<style lang="stylus" scoped>
@font-face {
  font-family: "paybooc-Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-Bold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
}
span {font-family: "paybooc-Bold"}
@keyframes text-in {
  0% {
    transform: translate(0, -20px);
    opacity: 0;
  }
}
.item {
  display: inline-block;
  min-width: 0.3em;
  font-size: 3rem;
  animation: text-in 0.8s cubic-bezier(0.22, 0.15, 0.25, 1.43) 0s backwards;
}
for co in 0 .. 13 {
//   .delay-anime:nth-child({co + 1}) {
//     animation-delay: co * 100ms + 200ms;
//   }
  .delay-color:nth-child({co + 1}) {
    if (co == 0){
      color: red
    } else if (co == 7) {
      color: red
    } else {
      color: white
    }
  }
}
</style>