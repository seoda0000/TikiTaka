<template>
  <div>
    <v-sheet id="sidebar-box" class="mainText" elevation="3">
      <!-- 유저 검색 -->
      <div style="margin: 20px 0">
        <v-toolbar flat dense>
          <v-autocomplete
            clearable
            outlined
            auto-select-first
            :loading="loading"
            :search-input.sync="searchUser"
            :items="items"
            v-model="select"
            label="Search Users..."
            @change="selectUser"
          ></v-autocomplete>
        </v-toolbar>
      </div>

      <!-- 추천 유저(with 프로필) -->
      <!-- <div style="margin-top: 30px">
        <h4>Perhaps you may like</h4>
        <v-sheet style="background-color: transparent">
          <v-slide-group active-class="success" show-arrows>
            <v-slide-item>
              <community-feed-user-list-item style="margin-right: 7px" />
            </v-slide-item>
            <v-slide-item>
              <community-feed-user-list-item style="margin-right: 7px" />
            </v-slide-item>
            <v-slide-item>
              <community-feed-user-list-item style="margin-right: 7px" />
            </v-slide-item>
            <v-slide-item>
              <community-feed-user-list-item style="margin-right: 7px" />
            </v-slide-item>
            <v-slide-item>
              <community-feed-user-list-item style="margin-right: 7px" />
            </v-slide-item>
            <v-slide-item>
              <community-feed-user-list-item style="margin-right: 7px" />
            </v-slide-item>
            <v-slide-item>
              <community-feed-user-list-item style="margin-right: 7px" />
            </v-slide-item>
            <v-slide-item>
              <community-feed-user-list-item style="margin-right: 7px" />
            </v-slide-item>
          </v-slide-group>
        </v-sheet>
      </div> -->

      <!-- 서로 맞팔한 유저 -->
      <div style="margin-top: 30px">
        <h4 class="logoText" style="margin-left: 15px">Mutual Friends</h4>
        <div id="user-box">
          <CommunitySideItem
            v-for="(follow, idx) in followList"
            :key="idx"
            :follow="follow"
          />
        </div>
      </div>
    </v-sheet>
  </div>
</template>

<script>
// import CommunityFeedUserListItem from "./CommunityFeedUserListItem.vue"
import CommunitySideItem from "./CommunitySideItem.vue"
export default {
  components: {
    // CommunityFeedUserListItem,
    CommunitySideItem,
  },
  name: "CommunitySide",
  props: {
    followList: Array,
    allUserList: Array,
  },
  data() {
    return {
      loading: false,
      items: this.allUserList,
      searchUser: null,
      select: null,
      users: this.$store.state.allUserList,
    }
  },
  watch: {
    searchUser(val) {
      val && val !== this.select && this.querySelections(val)
    },
  },
  methods: {
    querySelections(v) {
      this.loading = true
      setTimeout(() => {
        this.items = this.users.filter((e) => {
          return (e || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1
        })
        this.loading = false
      }, 500)
    },
    selectUser() {
      this.$router
        .push({ name: "mypage", params: { username: this.select } })
        .catch(() => {})
    },
  },
  created() {
    this.items = this.allUserList
  },
}
</script>

<style>
#sidebar-box {
  border-radius: 15px;
  height: 80vh;
  padding: 30px 10px;
  background-color: white;
  position: fixed;
  max-width: 17%;
  width: 100%;
  float: right;
  margin-left: auto;
  margin-right: 0;
  /* margin-right: 10px; */
  margin-top: 0px;
}
#user-box {
  background-color: white;
  border-radius: 40px;
  padding: 30px 10px;
  overflow: auto;
  height: 42vh;
}
</style>
