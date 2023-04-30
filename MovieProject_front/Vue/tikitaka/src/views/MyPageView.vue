<template>
  <div class="mainText" id="mypage">
    <!-- 프로필 섹션(좌측) -->
    <div id="profile-container" style="margin-top: 34px">
      <community-profile :user="tempUser" />
    </div>

    <!-- 메뉴 이동 섹션(아이콘 바)(우측 상단) -->
    <div id="icon-container">
      <my-page-icon-bar
        @show-feed="showFeed"
        @show-bookmark="showBookmark"
        @show-calendar="showCalendar"
        @show-message="showMessage"
      />
    </div>

    <!-- 콘텐츠 섹션(우측 하단) -->
    <v-sheet
      id="content-container"
      elevation="3"
      style="font-family: 'ONE-Mobile-Regular'; font-weight: bold"
    >
      <my-page-feed v-if="activeTab === 'MyPageFeed'" :feedList="feedList" />
      <my-page-bookmark v-if="activeTab === 'MyPageBookmark'" />
      <!-- <my-page-heart-feed
        v-if="activeTab === 'MyPageHeartFeed'"
        :user="tempUser"
        :feedList="feedList"
      /> -->
      <my-page-calendar
        v-if="activeTab === 'MyPageCalendar'"
        :calendarItems="calendarItems"
      />
      <my-page-message v-if="activeTab === 'MyPageMessage'" />
    </v-sheet>
  </div>
</template>

<script>
import MyPageMessage from "@/components/MyPageMessage.vue"
import CommunityProfile from "../components/CommunityProfile.vue"
import MyPageBookmark from "../components/MyPageBookmark.vue"
import MyPageCalendar from "../components/MyPageCalendar.vue"
import MyPageFeed from "../components/MyPageFeed.vue"
// import MyPageHeartFeed from "../components/MyPageHeartFeed.vue"
import MyPageIconBar from "../components/MyPageIconBar.vue"
export default {
  components: {
    CommunityProfile,
    MyPageIconBar,
    MyPageFeed,
    MyPageBookmark,
    // MyPageHeartFeed,
    MyPageCalendar,
    MyPageMessage,
  },
  name: "MyPageView",
  data() {
    return {
      activeTab: "MyPageFeed",
    }
  },
  computed: {
    // 화면의 유저 네임
    username: {
      get() {
        return this.$route.params.username
      },
      set(newValue) {
        return newValue
      },
    },
    // 현재 로그인한 유저
    user() {
      return this.$store.state.user
    },
    // 화면에서 보여져야 할 유저
    tempUser: {
      get() {
        return this.$store.state.tempUser
      },
      set(newValue) {
        return newValue
      },
    },
    feedList: {
      get() {
        return this.$store.state.feedList
      },
      set(newValue) {
        return newValue
      },
    },
    calendarItems: {
      get() {
        return this.$store.state.calendarItems
      },
      set(newValue) {
        return newValue
      },
    },
    isUser() {
      if (this.user.username === this.tempUser.username) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    showFeed(currentPage) {
      this.activeTab = currentPage
    },
    showBookmark(currentPage) {
      this.activeTab = currentPage
    },
    // showHeartFeed(currentPage) {
    //   this.activeTab = currentPage
    // },
    showCalendar(currentPage) {
      this.activeTab = currentPage
    },
    showMessage(currentPage) {
      this.activeTab = currentPage
    },
  },
  watch: {
    username() {
      this.$store.dispatch("getUser", this.username)
      this.$store.dispatch("loadFeedList", this.username)
    },
    tempUser() {
      this.$store.dispatch("loadUserCalendar", this.tempUser.id)
      this.$store.dispatch("getMe", this.user.username)
    },
  },
  created() {
    this.$store.dispatch("loadFeedList", this.username)
    this.$store.dispatch("getUser", this.username)
    this.$store.dispatch("loadUserCalendar", this.tempUser.id)
    this.$store.dispatch("loadMessageList")
    if (this.isUser) {
      console.log("들어옴???")
      this.$store.dispatch("loadAllMessageList", this.tempUser.id)
    }
  },
  updated() {
    // this.$store.dispatch("loadUserCalendar", this.tempUser.id)
    // this.feedList = this.$store.state.feedList
    // this.tempUser = this.$store.state.tempUser
    // this.$store.dispatch("getUser", this.username)
    // this.$store.dispatch("loadUserCalendar", this.tempUser.id)
  },
}
</script>

<style>
#mypage {
  display: grid;
  grid-template-columns: 17% 1fr;
  grid-template-rows: 0% 1fr;
  height: 100%;
  grid-template-areas:
    "profile iconArea"
    "profile contentArea";
  grid-gap: 35px;
  margin: 0 5% 0;
}

#icon-container {
  grid-area: iconArea;
}

#content-container {
  grid-area: contentArea;
  padding: 50px;
  background-color: white;
  border-radius: 20px;
  margin-bottom: 50px;
  display: fixed;
}
</style>
