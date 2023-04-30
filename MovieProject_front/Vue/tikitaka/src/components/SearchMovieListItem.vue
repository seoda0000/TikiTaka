<template>
  <div>
    <div class="col m-1">
      <div class="card" style="margin-bottom: 30px" @click="goDetail(movie.id)">
        <img :src="imgPath" class="card-img-top" />
        <h6 class="card-body" style="font-weight: bold">
          {{ movie.title }}
          <br />
          {{ movie.original_title }}
        </h6>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchMovieListItem",
  props: {
    movie: Object,
  },
  computed: {
    imgPath() {
      return "https://image.tmdb.org/t/p/original" + this.movie.poster_path
    },
  },
  methods: {
    goDetail(id) {
      this.$store.dispatch("getMovieById", id)
      this.$emit("close-modal")
    },
  },
}
</script>

<style>
.card-img-top {
  width: 100%;
  height: 480px;
  border-radius: 0 50px 0;
  object-fit: cover;
}
</style>
