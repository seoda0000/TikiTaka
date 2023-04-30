<template>
  <div>
    <!-- 영화 리스트 타이틀 -->
    <h1 style="color: #000000">
      {{ titleText }}
    </h1>

    <!-- 영화 리스트 -->
    <v-sheet style="border-radius: 15px" elevation="3">
      <v-slide-group class="pa-5" active-class="success" show-arrows>
        <v-slide-item v-for="(movie, idx) in movieList" :key="idx">
          <!-- 리스트 뷰 내 아이템  -->
          <movie-list-item :movie="movie" class="m-3" />
        </v-slide-item>
      </v-slide-group>
    </v-sheet>
  </div>
</template>

<script>
import MovieListItem from "./MovieListItem.vue"
export default {
  name: "MovieList",
  data() {
    return {}
  },
  components: { MovieListItem },
  props: {
    movieList: Array,
    titleText: String,
  },
}
</script>

<style></style>
