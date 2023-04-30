<template>
  <div>
    heart
    <p>{{ user }}</p>
    <hr />
    <p>{{ feedList }}</p>
  </div>
</template>

<script>
export default {
  name: "MyPageHeartFeed",
  props: {
    user: Object,
    feedList: Object,
  },
  created() {
    console.log("heart")
    console.log(this.feedList)
  },
}
</script>

<style></style>
