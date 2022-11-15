<template>
  <div>
    <!-- <div id="app"> -->
    <!-- <v-app id="inspire"> -->
    <v-sheet
      style="margin: 50px 50px; border-radius: 30px"
      elevation="10"
      max-width="100vw"
    >
      <h1 style="margin-left: 20px">dhdhdh</h1>
      <v-slide-group
        v-model="model"
        class="pa-4"
        active-class="success"
        show-arrows
      >
        <v-slide-item v-for="(movie, idx) in movieList" :key="idx">
          <!-- <v-slide-item
              v-for="movie in movieList"
              :key="movie"
              v-slot="{ active, toggle }"
              > -->
          <movie-list-item :movie="movie" class="m-2" />
          <!-- <v-card
                :color="active ? undefined : 'grey lighten-1'"
                class="ma-4"
                height="200"
                width="100"
                @click="toggle"
              > -->
          <!-- <v-row class="fill-height" align="center" justify="center">
                  <v-scale-transition>
                    <v-icon
                      v-if="active"
                      color="white"
                      size="48"
                      v-text="'mdi-close-circle-outline'"
                    ></v-icon>
                  </v-scale-transition>
                </v-row> -->
          <!-- </v-card> -->
        </v-slide-item>
      </v-slide-group>
    </v-sheet>
    <!-- </v-app> -->
  </div>
  <!-- </div> -->
</template>

<script>
import MovieListItem from "./MovieListItem.vue"
export default {
  name: "MovieList",
  data() {
    return {
      model: null,
    }
  },
  components: { MovieListItem },
  computed: {
    movieList() {
      return this.$store.state.movieList
    },
  },
  created() {
    this.$store.dispatch("loadMovieList")
  },
}
</script>

<style></style>
