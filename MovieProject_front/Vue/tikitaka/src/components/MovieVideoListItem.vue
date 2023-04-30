<template>
  <div style="position: relative; width: 100%; height: auto">
    <!-- <button id="info" class="btn btn-warning" @click="goDetail">
      자세히 보기
    </button> -->
    <iframe
      id="ytplayer, frame"
      type="text/html"
      width="100%"
      height="500px"
      :src="videoPath"
      frameborder="0"
      allowfullscreen
    />
  </div>
</template>

<script>
export default {
  name: "MovieVideoListItem",
  props: {
    movie: Object,
  },
  computed: {
    videoPath() {
      // 유튜브 무한 반복 재생
      return `https://www.youtube.com/embed/${this.movie.key}?autoplay=1&mute=1&rel=0&showsearch=0&controls=0&fs=0&loop=1&modestbranding=1&loop=1&playlist=${this.movie.key}`
      // return `https://www.youtube.com/embed/${this.movie.key}?&mute=1&rel=0&showsearch=0&controls=0&fs=0&loop=1&modestbranding=1&loop=1&playlist=${this.movie.key}`
    },
  },
  methods: {
    // 버튼 누르면 상세페이지로 이동
    goDetail() {
      console.log("here!!")
    },
  },
  // mounted() {
  //   console.log(this.movie)
  // },
}
</script>

<style>
#frame {
  position: absolute;
  z-index: 1;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

#info {
  position: absolute;
  bottom: 17px;
  right: 10px;
  z-index: 10;
  height: 50px;
  width: 140px;
}
</style>
