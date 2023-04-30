<template>
  <div>
    <iframe
      id="ytplayer, frame"
      type="text/html"
      width="100%"
      :src="videoPath"
      frameborder="0"
    />
    <!-- <img v-if="!movie.video_key" :src="posterURL" alt="" /> -->
  </div>
</template>

<script>
export default {
  name: "MovieDetailCommunity",
  props: {
    movie: Object,
  },
  data() {
    return {}
  },
  computed: {
    videoPath() {
      // 유튜브 무한 반복 재생
      return `https://www.youtube.com/embed/${this.movie.video_key}?mute=1&rel=0&showsearch=0&controls=0&fs=0&loop=1&modestbranding=1&loop=1&playlist=${this.movie.video_key}`
      // return `https://www.youtube.com/embed/${this.movie.key}?&mute=1&rel=0&showsearch=0&controls=0&fs=0&loop=1&modestbranding=1&loop=1&playlist=${this.movie.key}`
    },
    posterURL() {
      const path = this.movie["backdrop_set"][0].path

      return `https://image.tmdb.org/t/p/original${path}`
    },
  },
  created: {
    getvideoPath() {
      this.videoPath()
    },
  },
}
</script>

<style>
.sentence {
  height: 30px;
  margin: 5px;
}
</style>
