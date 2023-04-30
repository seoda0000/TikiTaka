<template>
    <div>
      <div v-for="(cast, idx) in movie.casts" :key="idx">
        <MovieDetailCastBoardItem
          :cast="cast"
        />
      </div>
    </div>
  
</template>

<script>
import MovieDetailCastBoardItem from "@/components/MovieDetailCastBoardItem.vue"

export default {
  name: 'MovieDetailCastBoard',
  components: {
    MovieDetailCastBoardItem
  },
  props: {
    movie: Object
  }

}
</script>

<style>

</style>