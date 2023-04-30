<template>
  <div id="feed-item" class="mainText" style="margin-bottom: 30px">
    <!-- 유저프로필 & 유저 닉네임 -->
    <v-sheet
      @click="clickFeed"
      elevation="3"
      style="padding: 20px; background-color: white; border-radius: 20px"
    >
      <!-- 유저 프로필 닉네임 -->
      <div style="display: flex; margin-bottom: 10px">
        <img
          style="width: 8%; min-width: 36px; border-radius: 50%"
          :src="require(`@/assets/tikitaka_${feed.user.profile_img}.png`)"
        />
        <h5
          style="
            align-self: center;
            margin-left: 10px;
            margin-top: auto;
            margin-bottom: auto;
          "
        >
          {{ feed.user.username }}
        </h5>
      </div>
      <!-- 피드 -->
      <div class="card" style="border-radius: 20px">
        <img :src="imgPath" id="feed-image" @click="clickFeed" />
        <div class="card-body">
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
                <h4
                  style="
                    margin-top: -1px;
                    margin-bottom: -0.5px;
                    font-family: 'ONE-Mobile-Regular';
                    font-weight: bold;
                  "
                >
                  {{ feed.title }}
                </h4>
                <p
                  style="
                    font-size: 14px;
                    color: rgb(93, 93, 93);
                    font-family: 'ONE-Mobile-Regular';
                    font-weight: bold;
                  "
                >
                  {{ feed.movie.title }} - {{ feed.movie.original_title }}
                </p>
                <p
                  style="
                    font-size: 12px;
                    color: gray;
                    margin-bottom: -5px;
                    font-family: 'ONE-Mobile-Regular';
                    font-weight: bold;
                  "
                >
                  좋아요 {{ likeCount }}개
                </p>
              </div>
              <v-btn icon color="red lighten-2" @click.stop="clickLikeBtn">
                <v-icon
                  v-if="isLike"
                  color="red"
                  size="30"
                  style="align-self: center"
                  >mdi-heart
                </v-icon>
                <v-icon v-else color="red" size="30" style="align-self: center"
                  >mdi-heart-outline
                </v-icon>
              </v-btn>
            </div>
            <hr />
            <div
              id="feed-content"
              style="font-family: 'ONE-Mobile-Regular'; font-weight: bold"
            >
              {{ feed.content }}
            </div>
          </div>
        </div>
      </div>
    </v-sheet>
  </div>
</template>

<script>
export default {
  name: "CommunityFeedItem",
  props: {
    feed: Object,
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

<style>
#feed-item {
}
#feed-image {
  border-radius: 20px 20px 0 0;
  width: 100%;
}
#feed-content {
  height: 70px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  text-align: justify;
  line-height: 2rem;
}
</style>
