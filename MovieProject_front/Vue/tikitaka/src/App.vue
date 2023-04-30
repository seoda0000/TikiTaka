<template>
  <v-app style="background-color: rgb(250, 250, 250)">
    <!-- 최상단 nav bar -->
    <v-app-bar
      app
      fixed
      clipped-left
      dark
      color="black"
      elevate-on-scroll
      scroll-target="#scrolling-techniques-7"
    >
      <!-- 메뉴 호출 아이콘 -->
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

      <!-- 메세지 영역 -->
      <v-toolbar-title class="logoText">TikiTaka</v-toolbar-title>
      <img
        src="@/assets/tikitaka_logo_small.png"
        style="width: 60px; border-radius: 50%"
      />

      <v-spacer></v-spacer>
      <v-menu offset-y v-if="isLogin">
        <template v-slot:activator="{ on, attrs }">
          <v-badge
            :content="messages"
            :value="messages"
            color="yellow"
            overlap
            dot="true"
          >
            <v-icon v-bind="attrs" v-on="on"> mdi-bell</v-icon>
          </v-badge>
        </template>
        <v-card v-if="isLogin">
          <v-card-title>Message</v-card-title>
          <v-card-subtitle
            >안 읽은 메세지가 {{ unreadMessage.length }}통
            있습니다.</v-card-subtitle
          >
          <hr />
          <div v-for="message in unreadMessage" :key="message.id">
            <div @click="checkRead(message.id)">
              <div
                class="mx-3"
                style="display: flex; justify-content: space-between"
              >
                <div>
                  <div
                    style="
                      display: flex;
                      justify-content: flex-start;
                      align-items: center;
                    "
                  >
                    <div>
                      <b>{{ message.from_user.username }} </b>
                    </div>
                  </div>
                  <p style="font-size: 14px; color: grey">
                    {{ message.content }}
                  </p>
                </div>

                <div>
                  <img
                    style="width: 35px"
                    :src="`https://image.tmdb.org/t/p/original/${message.movie.poster_path}`"
                  />
                </div>
              </div>
              <p
                class="mx-3"
                style="
                  font-size: 5px;
                  color: grey;
                  float: right;
                  margin-bottom: 10px;
                "
              >
                {{ new Date(message.send_at).toLocaleString() }}
              </p>
              <hr style="width: 80%; margin-left: auto; margin-right: auto" />
            </div>
          </div>
        </v-card>
      </v-menu>

      <v-btn
        v-if="!isLogin"
        @click="goSignUp"
        style="margin-right: 15px; margin-left: 15px"
      >
        SignUp
      </v-btn>
      <v-btn v-if="!isLogin" @click="goLogIn"> LogIn </v-btn>
      <v-btn
        v-if="isLogin"
        @click="logOut"
        style="margin-right: 15px; margin-left: 15px"
      >
        LogOut
      </v-btn>
    </v-app-bar>

    <!-- 왼쪽 side nav bar -->
    <!-- introView에서는 나타나지 않도록 -->
    <v-navigation-drawer
      app
      permanent
      expand-on-hover
      clipped
      fixed
      mini-variant
      left
      v-if="!['intro'].includes($route.name)"
    >
      <v-list nav dense fixed>
        <!-- 홈 버튼 -->
        <v-list-item link @click="goHome" style="margin-bottom: 20px">
          <v-list-item-icon>
            <v-img src="@/assets/icon_home.png" height="24px" width="24px">
            </v-img>
          </v-list-item-icon>
          <v-list-item-title>Home</v-list-item-title>
        </v-list-item>

        <!-- 영화 검색 버튼 -->
        <v-list-item link @click="openSearchModal" style="margin-bottom: 20px">
          <v-list-item-icon>
            <v-img src="@/assets/icon_search.png" height="24px" width="24px">
            </v-img>
          </v-list-item-icon>
          <v-list-item-title>Search Movies</v-list-item-title>
        </v-list-item>

        <!-- 커뮤니티 버튼 -->
        <v-list-item link @click="goCommunity" style="margin-bottom: 20px">
          <v-list-item-icon>
            <v-img
              src="@/assets/icon_community.png"
              height="24px"
              width="24px"
            ></v-img>
          </v-list-item-icon>
          <v-list-item-title>Community</v-list-item-title>
        </v-list-item>

        <!-- 마이페이지 버튼 -->
        <v-list-item link @click="goMyPage" style="margin-bottom: 20px">
          <v-list-item-icon>
            <v-img
              src="@/assets/icon_mypage.png"
              height="24px"
              width="24px"
            ></v-img>
          </v-list-item-icon>
          <v-list-item-title>My Page</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- 메인 화면 -->
    <v-main style="margin: 80px 0px">
      <router-view />
    </v-main>

    <!-- 영화 검색 모달 -->
    <b-modal id="searchModal" size="huge" hide-footer>
      <template #modal-header>
        <h2 class="logoText">SEARCH MOVIES</h2>
      </template>
      <div style="display: flex">
        <!-- 검색 섹션 -->
        <v-sheet
          class="p-3"
          style="border-radius: 30px; width: 15%; height: 45%"
          elevation="5"
        >
          <!-- 검색 카테고리 (영화인 검색은 일단 생략) -->
          <!-- <v-select
          class="mt-4"
          v-model="selectedOption"
          :items="searchOptions"
          dense
          outlined
        ></v-select> -->

          <!-- 입력폼 -->
          <v-text-field
            label="검색어를 입력해주세요"
            class="mainText"
            filled
            prepend-inner-icon="mdi-magnify"
            outlined
            dense
            solo
            flat
            v-model="keyword"
            @input="inputFunc"
          ></v-text-field>

          <!-- 장르 선택 -->
          <div class="mainText">
            <v-checkbox
              v-model="selectedGenres"
              label="모험"
              value="모험"
              hide-details
              @click="inputFunc"
            ></v-checkbox>
            <v-checkbox
              v-model="selectedGenres"
              label="공포/스릴러"
              value="공포/스릴러"
              hide-details
              @click="inputFunc"
            ></v-checkbox>
            <v-checkbox
              v-model="selectedGenres"
              label="애니메이션"
              value="애니메이션"
              hide-details
              @click="inputFunc"
            ></v-checkbox>
            <v-checkbox
              v-model="selectedGenres"
              label="액션"
              value="액션"
              hide-details
              @click="inputFunc"
            ></v-checkbox>
            <v-checkbox
              v-model="selectedGenres"
              label="SF/판타지"
              value="SF/판타지"
              hide-details
              @click="inputFunc"
            ></v-checkbox>
            <v-checkbox
              v-model="selectedGenres"
              label="로맨스"
              value="로맨스"
              hide-details
              @click="inputFunc"
            ></v-checkbox>
            <v-checkbox
              v-model="selectedGenres"
              label="코미디"
              value="코미디"
              hide-details
              @click="inputFunc"
            ></v-checkbox>
            <v-checkbox
              v-model="selectedGenres"
              label="음악"
              value="음악"
              hide-details
              @click="inputFunc"
            ></v-checkbox>
            <v-checkbox
              v-model="selectedGenres"
              label="Etc."
              value="Etc."
              hide-details
              @click="inputFunc"
            ></v-checkbox>
          </div>
          <br />
        </v-sheet>

        <!-- <div>
        </div> -->

        <!-- 결과 섹션 -->
        <div class="scroll" style="width: 100%; height: 65rem">
          <v-card flat width="100%">
            <div class="m-3">
              <div>
                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3">
                  <search-movie-list-item
                    v-for="(movie, idx) in searchMovieList"
                    :key="idx"
                    :movie="movie"
                    @close-modal="closeSearchModal"
                  />
                </div>
              </div>
            </div>
          </v-card>
        </div>
      </div>
    </b-modal>
  </v-app>
</template>

<script>
import SearchMovieListItem from "./components/SearchMovieListItem.vue"

// 장르 이름 -> 장르아이디 매핑
function matchGenreId(name) {
  switch (name) {
    case "모험":
      return 12
    case "공포/스릴러":
      return [27, 53]
    case "애니메이션":
      return 16
    case "액션":
      return 28
    case "SF/판타지":
      return [878, 14]
    case "로맨스":
      return 10749
    case "코미디":
      return 35
    case "음악":
      return 10402
    case "Etc.":
      return [18, 36, 37, 80, 99, 9648, 10751, 10752, 10770]
  }
}
export default {
  components: {
    SearchMovieListItem,
  },
  name: "App",
  data() {
    return {
      keyword: "",
      // selectedOption: "영화 제목",
      // searchOptions: ["영화 제목", "영화 배우/감독"],
      checked: false,
      selectedGenres: [
        "모험",
        "공포/스릴러",
        "애니메이션",
        "액션",
        "SF/판타지",
        "로맨스",
        "코미디",
        "음악",
        "Etc.",
      ],
    }
  },
  computed: {
    unreadMessage: {
      get() {
        return this.$store.state.unreadMessage
      },
      set(newValue) {
        return newValue
      },
    },
    messages() {
      return this.unreadMessage.length
    },
    searchMovieList() {
      return this.$store.state.searchMovieList
    },
    username() {
      return this.$store.state.user.username
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
    user: {
      get() {
        return this.$store.state.user
      },
      set(newValue) {
        return newValue
      },
    },
  },
  watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val)
    },
    user() {
      this.$store.dispatch("loadUnreadMessageList", this.user.id)
    },
  },
  methods: {
    goHome() {
      this.$router.push({ name: "home" }).catch(() => {}) // Avoided redundant navigation 에러 해결
    },
    goCommunity() {
      if (this.isLogin) {
        this.$router.push({ name: "community" }).catch(() => {})
      } else {
        this.$router.push({ name: "login" })
      }
    },
    goMyPage() {
      if (this.isLogin) {
        this.$router
          .push({ name: "mypage", params: { username: this.username } })
          .catch(() => {})
      } else {
        this.$router.push({ name: "login" })
      }
    },

    openSearchModal() {
      this.$bvModal.show("searchModal")
    },
    closeSearchModal() {
      this.$bvModal.hide("searchModal")
    },

    inputFunc() {
      // this.keyword = event.target.value
      const selectedGenreIds = []
      this.selectedGenres.forEach((element) => {
        const id = matchGenreId(element)
        if (Array.isArray(id)) {
          selectedGenreIds.push(...id)
        } else {
          selectedGenreIds.push(id)
        }
      })
      const payload = { keyword: this.keyword, genres: selectedGenreIds }
      this.$store.dispatch("searchMovieListByTitle", payload)
      // if (this.selectedOption == "영화 제목") {
      //   this.$store.dispatch("searchMovieListByTitle", payload)
      // } else {
      //   this.$store.dispatch("searchMovieListByPerson", payload)
      // }
      // console.log(this.searchMovieList)
      // console.log("herererere")
    },
    goSignUp() {
      this.$router.push({ name: "signup" })
    },
    goLogIn() {
      this.$router.push({ name: "login" })
    },
    logOut() {
      this.$store.dispatch("logOut")
    },
    checkRead(message_id) {
      // console.log("이거 읽었음!", message_id)
      this.$store.dispatch("checkReed", message_id)
    },
  },
  created() {
    this.$router.push({ name: "home" })
    this.$store.dispatch("loadAllMovieList")
    this.$store.dispatch("loadPopularMovieList")
    this.$store.dispatch("loadTopratedMovieList")
    this.$store.dispatch("loadNowPlayingMovieList")
    this.$store.dispatch("loadNowPlayingMovieVideoList")
    if (this.user) {
      this.$store.dispatch("loadUnreadMessageList", this.user.id)
    }
    if (this.isLogin) {
      this.$store.dispatch("loadRecommendMovieList", this.user.id)
    }
    this.$router.push({ name: "home" })
  },
}
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Pacifico&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Pacifico&family=Titan+One&display=swap");

.logoText {
  font-family: "Titan One", cursive;
}

.v-toolbar__title {
  font-size: 1.7rem !important;
}

.mainText {
  font-family: "Do Hyeon", sans-serif;
}

.modal .modal-huge {
  max-width: 75%;
  width: 75%;
}
/* 
#font-face {
  font-family: "S-CoreDream-3Light";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
} */
@font-face {
  font-family: "ChosunGu";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@1.0/ChosunGu.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "ONE-Mobile-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/ONE-Mobile-Regular.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

.modal .modal-medi {
  max-width: 60%;
  width: 60%;
}

.scroll {
  overflow-y: scroll;
}
</style>

<style scoped>
.v-text-field {
  width: 280px;
}
.v-navigation-drawer >>> .v-navigation-drawer__border {
  display: none;
}
</style>
