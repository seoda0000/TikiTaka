<template>
  <div>
    <v-card width="150px" height="220px">
      <v-img :src="posterPath" height="220px"></v-img>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "MovieListItem",
  props: {
    movie: Object,
  },
  computed: {
    posterPath() {
      return "https://image.tmdb.org/t/p/original" + this.movie.poster_path
    },
  },
}
</script>

<style></style>
