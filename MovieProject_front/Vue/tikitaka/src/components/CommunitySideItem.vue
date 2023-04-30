<template>
  <div @click="clickUser">
    <div style="display: flex">
      <img
        style="width: 40px; border-radius: 50%; margin-left: 20px"
        :src="require(`@/assets/tikitaka_${follow.profile_img}.png`)"
      />
      <h6
        style="
          align-self: center;
          margin-left: 10px;
          margin-top: auto;
          margin-bottom: auto;
        "
      >
        {{ follow.username }}
      </h6>
    </div>
    <hr />
  </div>
</template>

<script>
export default {
  name: "CommunitySideItem",
  props: {
    follow: Object,
  },
  methods: {
    clickUser() {
      this.$router
        .push({ name: "mypage", params: { username: this.follow.username } })
        .catch(() => {})
    },
  },
}
</script>

<style></style>
