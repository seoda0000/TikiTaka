<!-- 프로필 + 유저네임
피드사진
제목
콘텐츠
댓글 -->
<template>
  <div>
    <div class="col">
      <!-- 프로필 + 유저네임 출력 부분 -->
      <div
        class="mainText"
        style="display: flex; margin-bottom: 10px; margin-left: 5px"
      >
        <img
          @click="clickFeedUser"
          style="width: 45px; border-radius: 50%"
          :src="require(`@/assets/tikitaka_${feed.user.profile_img}.png`)"
        />
        <h4
          @click="clickFeedUser"
          style="
            align-self: center;
            margin-left: 10px;
            margin-top: auto;
            margin-bottom: auto;
          "
        >
          {{ feed.user.username }}
        </h4>
      </div>
      <!-- 콘텐츠 영역 -->
      <div
        class="card"
        style="
          border-radius: 20px;
          margin-bottom: 25px;
          box-shadow: 4px 4px 4px rgb(200, 200, 200);
          font-family: 'ONE-Mobile-Regular';
          font-weight: bold;
        "
      >
        <img :src="imgPath" id="feed-image" />
        <div class="card-body">
          <!-- 이미지 / 타이틀 / 피드 내용 출력 -->
          <div>
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
                <p style="font-size: 14px; color: rgb(93, 93, 93)">
                  {{ feed.movie.title }} - {{ feed.movie.original_title }}
                </p>
                <p style="font-size: 12px; color: gray; margin-bottom: -5px">
                  좋아요 {{ likeCount }}개
                </p>
              </div>
              <v-btn icon color="red lighten-2" @click="clickLikeBtn">
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
          <br />
          <!-- 댓글 출력 -->
          <div>
            <hr />
            <h5 style="font-weight: bold; margin-bottom: 15px">댓글</h5>
            <div>
              <div v-for="comment in feed.comment_set" :key="comment.id">
                <div style="display: flex" class="my-3">
                  <!-- 프로필 이미지 -->
                  <!-- <img
                    style="width: 30px; border-radius: 50%; align-self: center"
                    :src="
                      require(`@/assets/tikitaka_${comment.user.profile_img}.png`)
                    "
                  /> -->
                  <h6
                    @click="clickUser(comment.user.username)"
                    style="
                      align-self: center;
                      font-weight: bolder;
                      margin-top: auto;
                      margin-bottom: auto;
                      /* margin-left: 10px; */
                    "
                  >
                    {{ comment.user.username }}
                  </h6>
                  <h6
                    style="
                      align-self: center;
                      margin-left: 10px;
                      margin-top: auto;
                      margin-bottom: auto;
                    "
                  >
                    {{ comment.content }}
                  </h6>
                  <div v-show="isWriteUser(comment)" style="margin-left: 10px">
                    <v-btn icon @click="deleteComment(comment)">
                      <v-icon
                        size="20"
                        style="margin-top: auto; margin-bottom: auto"
                        >mdi-close-circle-outline</v-icon
                      >
                    </v-btn>
                  </div>
                </div>
              </div>

              <!-- 댓글 작성 -->
              <div style="display: flex">
                <v-text-field
                  rounded
                  outlined
                  dense
                  label="댓글을 남겨주세요"
                  flat
                  hide-details
                  v-model="comment"
                  @keyup.enter="createComment"
                ></v-text-field>
                <div style="margin-left: 15px">
                  <v-btn icon @click="createComment"
                    ><v-icon size="30">mdi-send</v-icon></v-btn
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FeedDetailItem",
  props: {
    feed: Object,
  },
  data() {
    return {
      comment: null,
    }
  },
  computed: {
    imgPath() {
      return "https://image.tmdb.org/t/p/original" + this.feed.backdrop.path
    },
    user_id() {
      return this.$store.state.user.id
    },
    isWriteUser() {
      return (comment) => {
        if (this.user_id === comment.user.id) {
          return true
        } else {
          return false
        }
      }
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
  },
  methods: {
    // 좋아요 버튼 클릭
    clickLikeBtn() {
      const payload = {
        feed_id: this.feed.id,
        user_id: this.$store.state.user.id,
      }
      this.$store.dispatch("clickLikeBtn", payload)
    },
    // 댓글 작성
    createComment() {
      const payload = {
        feed_id: this.feed.id,
        content: this.comment,
        user_id: this.$store.state.user.id,
      }
      this.$store.dispatch("createComment", payload)
      this.comment = ""
    },
    deleteComment(comment) {
      const payload = {
        feed_id: this.feed.id,
        comment_id: comment.id,
      }
      this.$store.dispatch("deleteComment", payload)
    },
    clickUser(user) {
      this.$store.dispatch("getUser", user)
      this.$router
        .push({ name: "mypage", params: { username: user } })
        .catch(() => {})
      this.$emit("close-modal")
    },
    clickFeedUser() {
      this.$router
        .push({ name: "mypage", params: { username: this.feed.user.username } })
        .catch(() => {})
      this.$emit("close-modal")
    },
  },
}
</script>

<style></style>
