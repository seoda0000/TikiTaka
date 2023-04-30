<!-- 피드사진
제목
콘텐츠 -->
<template>
  <div>
    <div class="col">
      <div
        class="card"
        style="
          border-radius: 20px;
          margin-bottom: 25px;
          box-shadow: 4px 4px 4px rgb(200, 200, 200);
        "
      >
        <img :src="imgPath" id="feed-image" @click="clickFeed" />
        <div class="card-body">
          <!-- 이미지 / 타이틀 / 컨텐츠만 보이게 (피드 출력에서 사용) -->
          <div @click="clickFeed">
            <div
              style="
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin: -6px 0;
              "
            >
              <div>
                <h5
                  style="
                    margin-top: -1px;
                    margin-bottom: -0.5px;
                    font-family: 'ONE-Mobile-Regular';
                    font-weight: bold;
                  "
                >
                  {{ feed.title }}
                </h5>
                <p style="font-size: 13px; color: rgb(93, 93, 93)">
                  {{ feed.movie.title }} - {{ feed.movie.original_title }}
                </p>
                <p style="font-size: 12px; color: gray; margin-bottom: -5px">
                  좋아요 {{ likeCount }}개
                </p>
              </div>
              <v-btn icon color="red lighten-2" @click.stop="clickLikeBtn">
                <v-icon
                  v-if="isLike"
                  color="red"
                  size="25"
                  style="align-self: center"
                  >mdi-heart
                </v-icon>
                <v-icon v-else color="red" size="25" style="align-self: center"
                  >mdi-heart-outline
                </v-icon>
              </v-btn>
            </div>
            <hr />
            <div id="feed-content">
              {{ feed.content }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyPageFeedItem",
  props: {
    feed: Object,
    requestFromDetail: Boolean,
  },
  computed: {
    imgPath() {
      return "https://image.tmdb.org/t/p/original" + this.feed.backdrop.path
    },
    user_id() {
      return this.$store.state.user.id
    },
    isLike() {
      let pushLike = false
      this.feed.like_users.forEach((element) => {
        if (element.id === this.user_id) {
          pushLike = true
        }
      })
      return pushLike
    },
    likeCount() {
      return this.feed.like_users.length
    },
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
    clickFeed() {
      this.$store.dispatch("loadFeed", this.feed.id)
      this.$emit("click-feed", this.clickedFeed)
    },
    clickLikeBtn() {
      const payload = {
        feed_id: this.feed.id,
        user_id: this.$store.state.user.id,
      }
      this.$store.dispatch("clickLikeBtn", payload)
      this.$emit("click-like", this.clickedFeed)
    },
  },
  updated() {
    this.clickedFeed = this.$store.state.selectedFeed
  },
}
</script>

<style></style>
