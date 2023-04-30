<template>
  <div>
    <!-- 피드 -->
    <div>
      <!-- {{ relatedFeedList }} -->
      <community-feed-item
        v-for="(feed, idx) in relatedFeedList"
        :key="idx"
        :feed="feed"
        @click-feed="clickFeed"
        @click-like="clickLike"
      />
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
      />
    </b-modal>
  </div>
</template>

<script>
import CommunityFeedItem from "./CommunityFeedItem.vue"
import FeedDetailModal from "./FeedDetailModal.vue"
export default {
  components: { CommunityFeedItem, FeedDetailModal },
  name: "CommunityFeed",
  props: {
    relatedFeedList: Array,
  },
  computed: {
    // // 현재 로그인한 유저
    // user() {
    //   return this.$store.state.user
    // },
    // // 현재 유저와 피드 작성 유저가 같은지 판단 -> 같을 때만 삭제,수정 가능
    // isUser() {
    //   if (this.user.id === this.clickedFeed.user.id) {
    //     return true
    //   }
    //   return false
    // },
    clickedFeed: {
      get() {
        return this.$store.state.selectedFeed
      },
      set(newValue) {
        return newValue
      },
    },
  },
  methods: {
    clickFeed(feed) {
      this.clickedFeed = feed
      this.$bvModal.show("feedDetailModal")
    },
    closeFeedModal() {
      this.$bvModal.hide("feedDetailModal")
    },
    clickLike(feed) {
      this.clickedFeed = feed
    },
  },
}
</script>

<style></style>
