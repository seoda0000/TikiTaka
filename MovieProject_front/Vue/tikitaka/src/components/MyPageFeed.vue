<template>
  <div>
    <h5 v-show="isNoneFeedList">작성된 피드가 없습니다</h5>

    <!-- 피드 작성 버튼 -->
    <v-btn
      v-show="isEqualUser"
      icon
      color="black lighten-2"
      height="70pxs"
      @click="openCreateFeedModal"
      style="bottom: 50px; right: 1.8%; z-index: 100"
      fixed
    >
      <img src="@/assets/add_btn.png" alt="" width="70px" />
    </v-btn>
    <!-- 게시글 작성 모달 -->
    <b-modal hide-footer hide-header-close size="medi" id="createFeedModal">
      <template #modal-header>
        <h2 class="logoText">CREATE YOUR OWN POST</h2>
      </template>
      <feed-create-modal
        :isFeedRequest="isFeedRequest"
        @close-modal="closeCreateFeedModal"
      />
    </b-modal>

    <!-- 작성 게시글 출력 영역 -->
    <div style="width: 100%">
      <v-card flat width="100%">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3">
          <my-page-feed-item
            v-for="(feed, idx) in feedList"
            :key="idx"
            :feed="feed"
            @click-feed="clickFeed"
            @click-like="clickLike"
          />
        </div>
      </v-card>
    </div>

    <!-- 게시글 디테일 모달 -->
    <b-modal
      hide-header
      hide-footer
      hide-header-close
      size="medi"
      id="feedDetailModal"
    >
      <feed-detail-modal
        :clickedFeed="clickedFeed"
        @close-modal="closeFeedModal"
        @open-update-feed-modal="openUpdateFeedModal"
      />
      <!-- <feed-detail-modal /> -->
    </b-modal>

    <!-- 게시글 수정 모달 -->
    <b-modal hide-footer hide-header-close size="medi" id="updateFeedModal">
      <template #modal-header>
        <h2 class="logoText">UPDATE THE POST</h2>
      </template>
      <feed-update-modal
        :clickedFeed="clickedFeed"
        @close-modal="closeUpdateFeedModal"
      />
      <!-- <feed-create-form
        :isFeedRequest="isFeedRequest"
        @close-modal="closeCreateFeedModal"
      /> -->
    </b-modal>
  </div>
</template>

<script>
import FeedCreateModal from "./FeedCreateModal.vue"
import FeedDetailModal from "./FeedDetailModal.vue"
import FeedUpdateModal from "./FeedUpdateModal.vue"
import MyPageFeedItem from "./MyPageFeedItem.vue"
export default {
  components: {
    FeedCreateModal,
    MyPageFeedItem,
    FeedDetailModal,
    FeedUpdateModal,
  },
  name: "MyPageFeed",
  props: {
    feedList: Array,
  },
  data() {
    return {
      isFeedRequest: true,
    }
  },
  computed: {
    // 현재 로그인한 유저
    user() {
      return this.$store.state.user
    },
    // 현재 유저와 피드 작성 유저가 같은지 판단 -> 같을 때만 삭제,수정 가능
    isUser() {
      if (this.user.id === this.clickedFeed.user.id) {
        return true
      }
      return false
    },
    clickedFeed: {
      get() {
        return this.$store.state.selectedFeed
      },
      set(newValue) {
        return newValue
      },
    },
    feedBackDropList: {
      get() {
        return this.$store.state.feedBackDropList
      },
      set(newValue) {
        return newValue
      },
    },
    isEqualUser() {
      if (this.user.id === this.$store.state.tempUser.id) {
        return true
      } else {
        return false
      }
    },
    isNoneFeedList() {
      if (this.feedList.length === 0) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    openCreateFeedModal() {
      this.$bvModal.show("createFeedModal")
      this.$store.commit("INITIALIZE_BACKDROP_LIST")
    },
    closeCreateFeedModal() {
      this.$bvModal.hide("createFeedModal")
    },
    clickFeed(feed) {
      this.clickedFeed = feed
      this.$bvModal.show("feedDetailModal")
      console.log("선택된 영화", this.clickedFeed)
      // this.$store.dispatch("getBackDropList", this.feed.movie.id)
    },
    closeFeedModal() {
      this.$bvModal.hide("feedDetailModal")
    },
    clickLike(feed) {
      this.clickedFeed = feed
    },
    openUpdateFeedModal() {
      this.$bvModal.show("updateFeedModal")
    },
    closeUpdateFeedModal() {
      this.$bvModal.hide("updateFeedModal")
    },
  },
  updated() {},
}
</script>

<style></style>
