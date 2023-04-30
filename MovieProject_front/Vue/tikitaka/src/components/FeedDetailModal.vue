<template>
  <div>
    <feed-detail-item :feed="clickedFeed" @close-modal="closeModal" />
    <div style="float: right" v-show="isUser">
      <v-btn dark class="mx-3" @click="deleteFeed">DELETE</v-btn>
      <v-btn dark @click="updateFeed">EDIT</v-btn>
    </div>
  </div>
</template>

<script>
import FeedDetailItem from "./FeedDetailItem.vue"
export default {
  components: { FeedDetailItem },
  name: "FeedDetailModal",
  props: {
    clickedFeed: Object,
  },
  data() {
    return {
      // requestFromDetail: true,
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
  },
  methods: {
    // 피드 삭제
    deleteFeed() {
      this.$store.dispatch("deleteFeed", this.clickedFeed.id)
      this.$emit("close-modal")
    },
    // 피드 업데이트
    updateFeed() {
      this.$emit("close-modal") //현재 피드 닫고
      this.$emit("open-update-feed-modal") // 수정모달 띄우기
    },
    closeModal() {
      this.$emit("close-modal")
    },
  },
}
</script>

<style></style>
