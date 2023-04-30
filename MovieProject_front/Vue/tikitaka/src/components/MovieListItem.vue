<template>
  <div>
    <v-card class="zoom" width="150px" height="220px">
      <v-img
        :src="posterPath"
        height="220px"
        @click="goDetail(movie.id)"
      ></v-img>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "MovieListItem",
  props: {
    movie: Object,
    title: String,
  },
  computed: {
    posterPath() {
      return "https://image.tmdb.org/t/p/original" + this.movie.poster_path
    },
  },
  methods: {
    goDetail(id) {
      this.$store.dispatch("getMovieById", id)
    },
  },
}
</script>

<style>
.zoom {
  transition: transform 0.2s; /* Animation */
}

.zoom:hover {
  transform: scale(
    1.1
  ); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
}
</style>
