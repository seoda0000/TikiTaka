<template>
  <div>
    <div id="container-box">
      <movie-list />
      <movie-list />
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue"
export default {
  name: "HomeView",
  components: { MovieList },
}
</script>

<style>
#container-box {
  background-color: #004e66;
  border-radius: 80px;
  margin: 20px;
  padding: 20px;
}
</style>
