<template>
  <div style="margin: 0px 15% 200px">
    <div style="display: flex" class="mainText">
      <!-- 영화 포스터 및 버튼 영역 -->
      <div style="max-width: 220px; margin-right: 30px">
        <img :src="posterURL" alt="" style="width: 100%" />
        <div>
          <v-btn
            v-if="isBookmark"
            @click="clickBookmark"
            style="width: 100%; margin-top: 20px"
          >
            <v-icon left> mdi-star </v-icon>
            Bookmark
          </v-btn>
          <v-btn
            v-if="!isBookmark"
            @click="clickBookmark"
            style="width: 100%; margin-top: 20px"
          >
            <v-icon left> mdi-star-outline </v-icon>
            Bookmark
          </v-btn>
          <v-btn
            style="width: 100%; margin-top: 20px"
            @click="openMessageModal"
          >
            <v-icon left> mdi-message </v-icon>
            Message
          </v-btn>
        </div>
        <!-- <v-btn style="width: 100%; margin-top: 30px">
          <v-icon left> mdi-pencil </v-icon>
          Review
        </v-btn> -->
      </div>

      <!-- 영화 정보 -->
      <div>
        <!-- 제목 영역 -->
        <div style="display: flex; align-items: flex-end">
          <h1 style="font-weight: bold">{{ movie.title }}</h1>
          <p style="margin-bottom: 11px">{{ movie.original_title }}</p>
        </div>

        <!-- 영화 정보 영역 -->
        <div style="display: flex; margin: 10px 0px 30px">
          <!-- 영화 상세 정보 -->
          <div style="width: 35%">
            <h2>Info</h2>
            <MovieDetailBasic :movie="movie" />
          </div>

          <!-- 영화 캐스팅 -->
          <div style="width: 35%">
            <h2>Cast</h2>
            <MovieDetailCastBoard
              :movie="movie"
              style="
                font-family: 'ONE-Mobile-Regular';
                font-weight: bold;
                font-size: 15px;
              "
            />
          </div>
          <!-- 커뮤니티 영역 -->
          <div style="width: 30%" v-show="movie.video_key">
            <h3>Trailer</h3>
            <MovieDetailCommunity :movie="movie" />
          </div>
        </div>

        <!-- 영화 줄거리 -->
        <div>
          <h2>Overview</h2>
          <p
            style="
              line-height: 200%;
              font-family: 'ONE-Mobile-Regular';
              font-weight: bold;
            "
          >
            {{ movie.overview }}
          </p>
        </div>
      </div>

      <!-- 메시지 보내기 모달 -->
      <b-modal hide-footer hide-header-close id="sendMessageModal">
        <template #modal-header>
          <h3 class="logoText">RECOMMEND TO YOUR FRIEND</h3>
        </template>
        <div class="mainText">
          <h5 class="logoText">To</h5>
          <v-toolbar flat dense style="margin-top: 30px; margin-left: -15px">
            <v-autocomplete
              clearable
              outlined
              auto-select-first
              :loading="loading"
              :search-input.sync="searchUser"
              :items="items"
              v-model="select"
              label="Search Users..."
            ></v-autocomplete>
          </v-toolbar>
          <br />
          <h5 class="logoText">Message</h5>
          <v-text-field clearable outlined v-model="message"></v-text-field>
          <v-btn dark style="float: right" @click="sendMessage">SEND</v-btn>
        </div>
      </b-modal>
    </div>
    <div style="margin-top: 30px">
      <b><h2 class="mainText">관련 영화 추천</h2></b>
      <v-sheet style="background-color: transparent">
        <v-slide-group active-class="success" show-arrows class="pa-5">
          <v-slide-item
            v-for="movie in recommendMovieListAtDetail"
            :key="movie.id"
          >
            <div class="m-3">
              <v-card
                class="zoom"
                width="150px"
                height="220px"
                @click="goDetail(movie.id)"
              >
                <v-img
                  :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
                  height="220px"
                ></v-img>
              </v-card>
            </div>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </div>
  </div>
</template>

<script>
import MovieDetailCastBoard from "@/components/MovieDetailCastBoard.vue"
import MovieDetailBasic from "@/components/MovieDetailBasic.vue"
import MovieDetailCommunity from "@/components/MovieDetailCommunity.vue"

export default {
  name: "MovieDetail",
  components: {
    MovieDetailCastBoard,
    MovieDetailBasic,
    MovieDetailCommunity,
  },
  props: {
    movie: Object,
  },
  data() {
    return {
      loading: false,
      searchUser: null,
      select: null,
      message: null,
    }
  },
  watch: {
    searchUser(val) {
      val && val !== this.select && this.querySelections(val)
    },
    movie() {
      this.$store.dispatch("loadRecommendMoviesAtDetail", this.movie.id)
    },
  },
  computed: {
    recommendMovieListAtDetail() {
      return this.$store.state.recommendMovieListAtDetail
    },
    posterURL() {
      const path = this.movie.poster_path

      return `https://image.tmdb.org/t/p/original${path}`
    },
    isBookmark() {
      if (this.$store.state.user) {
        return this.$store.state.user.bookmarks.find(
          (b) => b.id === this.movie.id
        )
      } else {
        return false
      }
    },
    user() {
      return this.$store.state.user
    },
    users() {
      const following = []
      if (this.$store.state.user) {
        this.user.following.forEach((element) => {
          const name = element.username
          following.push(name)
        })
      }
      return following
    },
    items: {
      get() {
        const following = []
        if (this.$store.state.user) {
          this.user.following.forEach((element) => {
            const name = element.username
            following.push(name)
          })
        }
        return following
      },
      set(newValue) {
        return newValue
      },
    },
  },
  methods: {
    querySelections(v) {
      this.loading = true
      setTimeout(() => {
        if (this.$store.state.user) {
          this.items = this.users.filter((e) => {
            return (e || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1
          })
          this.loading = false
        }
      }, 500)
    },
    clickBookmark() {
      if (this.$store.state.user) {
        return this.$store.dispatch("clickBookmark", this.movie.id)
      } else {
        alert("로그인이 필요한 서비스입니다.")
      }
    },
    openMessageModal() {
      if (this.$store.state.user) {
        this.$bvModal.show("sendMessageModal")
      } else {
        alert("로그인이 필요한 서비스입니다.")
      }
    },
    sendMessage() {
      let to_user_id
      this.user.following.forEach((element) => {
        if (this.select === element.username) {
          to_user_id = element.id
        }
      })
      const payload = {
        to_user_id: to_user_id,
        from_user_id: this.user.id,
        content: this.message,
        movie_id: this.movie.id,
      }
      this.$store.dispatch("sendMessage", payload)
      this.$bvModal.hide("sendMessageModal")
      alert("메시지가 정상적으로 전송되었습니다!")
      this.message = null
      this.select = null
    },
    goDetail(id) {
      this.$store.dispatch("getMovieById", id)
    },
  },
  created() {
    this.$store.dispatch("loadRecommendMoviesAtDetail", this.movie.id)
  },
}
</script>

<style></style>
