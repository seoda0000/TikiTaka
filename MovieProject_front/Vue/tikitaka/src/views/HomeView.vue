<template>
  <div id="home" class="mainText">
    <!-- 좌측(프로필) -->
    <!-- <div v-if="isLogin" id="profile-container">
      <community-profile-default/>
    </div> -->
    <div v-if="!isLogin" id="profile-container2">
      <community-profile-default />
    </div>

    <div v-if="isLogin" id="profile-container">
      <community-profile :user="user" />
    </div>

    <!-- 우측(영화출력) -->
    <div id="movie-container">
      <div>
        <movie-video-list
          :movieList="nowPlayingMovieVideoList.movies"
          :titleText="nowPlayingMovieVideoList.title"
        />
      </div>
      <div id="container-box">
        <br /><br />
        <!-- 당신을 위한 영화 -->
        <movie-list
          v-if="bookmarkPop"
          :movieList="recommendMovieList.movies"
          :titleText="recommendMovieList.title"
        /><br /><br />
        <movie-list
          :movieList="popularMovieList.movies"
          :titleText="popularMovieList.title"
        /><br /><br />
        <!-- <hr class="movielist-divide" /> -->
        <movie-list
          :movieList="nowPlayingMovieList.movies"
          :titleText="nowPlayingMovieList.title"
        /><br /><br />
        <!-- <hr class="movielist-divide" /> -->
        <movie-list
          :movieList="topratedMovieList.movies"
          :titleText="topratedMovieList.title"
        /><br /><br />
        <!-- <hr class="movielist-divide" /> -->
        <!-- <movie-list
          :movieList="nowPlayingMovieList.movies"
          :titleText="nowPlayingMovieList.title"
        /><br /><br /> -->
      </div>
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue"
import MovieVideoList from "../components/MovieVideoList.vue"
import CommunityProfile from "../components/CommunityProfile.vue"
import CommunityProfileDefault from "../components/CommunityProfileDefault.vue"
export default {
  name: "HomeView",
  components: {
    MovieList,
    MovieVideoList,
    CommunityProfile,
    CommunityProfileDefault,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    bookmarkPop() {
      if (this.isLogin) {
        return this.$store.state.recommendMovieList.movies.length !== 0
      } else {
        return false
      }
    },
    popularMovieList() {
      return this.$store.state.popularMovieList
    },
    topratedMovieList() {
      return this.$store.state.topratedMovieList
    },
    recommendMovieList() {
      return this.$store.state.recommendMovieList
    },
    nowPlayingMovieList() {
      return this.$store.state.nowPlayingMovieList
    },
    nowPlayingMovieVideoList() {
      return this.$store.state.nowPlayingMovieVideoList
    },
    user() {
      return this.$store.state.user
    },
    username() {
      if (this.user) {
        return this.user.username
      } else {
        return "로그인해주세요"
      }
    },
  },
  created() {
    this.$store.dispatch("getMe", this.username)
  },
  updated() {
    this.$store.dispatch("getUser", this.username)
  },
  watch: {
    user() {
      this.$store.dispatch("getUser", this.username)
      // this.$store.dispatch("getMe", this.username)
      // this.$store.dispatch("loadFeedList", this.username)
      // this.$store.dispatch("loadUserCalendar", this.tempUser.id)
      if (this.isLogin) {
        this.$store.dispatch("loadRecommendMovieList", this.user.id)
      }
    },
  },
}
</script>

<style>
#home {
  display: grid;
  grid-template-columns: 17% 75%;
  grid-template-rows: 100%;
  height: 100%;
  grid-template-areas: "profile movie";
  grid-gap: 35px;
  margin: 0 5% 0;
}

#profile-container {
  grid-area: profile;
  width: 230px;
  margin-left: auto;
  /* margin-left: 10px;
  margin-top: 10px; */
}
#profile-container2 {
  /* grid-area: profile; */
  width: 230px;
  margin-left: auto;
}

#movie-container {
  grid-area: movie;
}

#container-box {
  background-color: transparent;
  border-radius: 80px;
}

.movielist-divide {
  width: 95%;
  height: 7px;
  background-color: gray;
  margin: 0 auto;
  border: 0;
  border-radius: 50px;
  margin-bottom: 30px;
}
</style>
