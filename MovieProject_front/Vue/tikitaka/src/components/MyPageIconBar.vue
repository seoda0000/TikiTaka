<template>
  <div id="icon-bar">
    <!-- 피드 아이콘 -->
    <v-btn fab large plain @click="showFeed('MyPageFeed')"
      ><v-icon large>mdi-file</v-icon></v-btn
    >
    <!-- <span class="mx-5">
          <font-awesome-icon icon="fa-solid fa-file" size="2x" />
        </span> -->

    <div class="v-line"></div>

    <!-- 북마크 아이콘 -->
    <v-btn fab large plain @click="showBookmark('MyPageBookmark')"
      ><v-icon large>mdi-bookmark</v-icon></v-btn
    >
    <!-- <span class="mx-5">
            <font-awesome-icon icon="fa-solid fa-bookmark" size="2x" spin-pulse />
        </span> -->

    <!-- <div class="v-line"></div> -->

    <!-- 좋아요한 피드 아이콘 -->
    <!-- <v-btn fab large plain @click="showHeartFeed('MyPageHeartFeed')"
      ><v-icon large>mdi-heart</v-icon></v-btn
    > -->
    <!-- <span class="mx-5">
            <font-awesome-icon icon="fa-solid fa-heart" size="2x" />
        </span> -->

    <div class="v-line"></div>

    <!-- 달력 아이콘 -->
    <v-btn fab large plain @click="showCalendar('MyPageCalendar')"
      ><v-icon large>mdi-calendar</v-icon></v-btn
    >
    <!-- <span class="mx-5">
      <font-awesome-icon icon="fa-solid fa-calendar-days" size="2x" />
    </span> -->

    <div v-show="isUser" class="v-line"></div>

    <!-- 메시지함 아이콘 -->
    <v-btn v-show="isUser" fab large plain @click="showMessage('MyPageMessage')"
      ><v-icon large>mdi-email</v-icon></v-btn
    >
    <!-- <span class="mx-5">
      <font-awesome-icon icon="fa-solid fa-calendar-days" size="2x" />
    </span> -->
  </div>
</template>

<script>
export default {
  name: "MyPageIconBar",
  data() {
    return {}
  },
  computed: {
    isUser() {
      if (
        this.$store.state.user.username === this.$store.state.tempUser.username
      ) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    showFeed(currentPage) {
      this.$emit("show-feed", currentPage)
    },
    showBookmark(currentPage) {
      this.$emit("show-bookmark", currentPage)
    },
    // showHeartFeed(currentPage) {
    //   this.$emit("show-heart-feed", currentPage)
    // },
    showCalendar(currentPage) {
      this.$emit("show-calendar", currentPage)
    },
    showMessage(currentPage) {
      this.$emit("show-message", currentPage)
    },
  },
}
</script>

<style>
#icon-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: -50px;
}

.v-line {
  border-left: thick solid rgba(213, 204, 204, 0.735);
  border-radius: 60px;
  height: 30px;
  margin: 0 40px;
}
</style>
