<template>
  <div>
    <h1>INTRO</h1>
    <button class="btn btn-warning" @click="goHome">HOME</button>
  </div>
</template>

<script>
export default {
  name: "IntroPage",
  methods: {
    goHome() {
      this.$router.push({ name: "home" })
    },
  },
}
</script>

<style></style>
