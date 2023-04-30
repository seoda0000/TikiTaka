<template>
  <div>
    <h5 v-show="isNoneBookmark">관심있는 영화를 저장해주세요!</h5>
    <v-card flat width="100%">
      <div class="m-3">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3">
          <div v-for="bookmark in tempUser.bookmarks" :key="bookmark.id">
            <div class="col m-1">
              <b-card
                :img-src="`https://image.tmdb.org/t/p/original/${bookmark.poster_path}`"
                img-alt="Card image"
                img-left
                style="height: 15rem; margin-bottom: 25px"
                class="shadow p-3 mb-5 bg-white rounded zoom"
                @click="goDetail(bookmark.id)"
              >
                <b-card-text>
                  <div>
                    <h4>{{ bookmark.title }}</h4>
                    <p style="font-size: 14px; color: gray">
                      {{ bookmark.original_title }}
                    </p>
                    <v-btn
                      v-show="isUser"
                      dark
                      style="position: absolute; bottom: 15px; right: 15px"
                      @click.stop="bookmarkDelete(bookmark.id)"
                      >DELETE</v-btn
                    >
                  </div>
                </b-card-text>
              </b-card>
            </div>
          </div>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "MyPageBookmark",
  computed: {
    // 현재 로그인한 유저
    user() {
      return this.$store.state.user
    },
    tempUser: {
      get() {
        return this.$store.state.tempUser
      },
      set(newValue) {
        return newValue
      },
    },
    // 현재 유저와 피드 작성 유저가 같은지 판단 -> 같을 때만 삭제,수정 가능
    isUser() {
      if (this.user.id === this.tempUser.id) {
        return true
      }
      return false
    },
    isNoneBookmark() {
      if (this.tempUser.bookmarks.length === 0) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    bookmarkDelete(movie_id) {
      this.$store.dispatch("clickBookmark", movie_id)
    },
    goDetail(movie_id) {
      console.log("디테일로")
      this.$store.dispatch("getMovieById", movie_id)
    },
  },
  updated() {
    this.tempUser = this.$store.state.tempUser
  },
}
</script>

<style></style>
