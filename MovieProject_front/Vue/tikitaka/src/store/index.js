import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

import axios from "axios"
import router from "@/router"
import createPersistedState from "vuex-persistedstate" // 로컬에 데이터 자동저장을 학기 위한 패키지

const DJ_URL = "http://127.0.0.1:8000"
// const DJ_URL = "http://34.204.166.25"

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    allMovieList: [],
    allUserList: [],
    nowPlayingMovieList: { title: "현재 상영작", movies: [] },
    popularMovieList: { title: "박스 오피스", movies: [] },
    topratedMovieList: { title: "스테디 셀러", movies: [] },
    recommendMovieList: { title: "당신을 위한 영화", movies: [] },
    nowPlayingMovieVideoList: { title: "상영중 영화 비디오", movies: [] },
    recommendMovieListAtDetail: null, // 영화 디테일 페이지에서 추천 영화
    searchMovieList: [],
    feedMovieId: null, // 안 필요할 수도 있음

    // 캘린더 등록시 필요
    feedBackDropList: [],
    cal_movie_title: null, //캘린더에서 사용할 영화 제목
    calendarItems: [],

    movie: null,
    token: null,
    // 현재 로그인 유저
    user: null,
    // 현재 로그인 유저 닉네임
    nickname: "로그인????",

    feedList: [],
    relatedFeedList: [],
    tempUser: null,
    selectedFeed: null,
    allMessage: null,
    unreadMessage: null,
  },
  getters: {
    followList(state) {
      return state.user.following
    },
    isLogin(state) {
      return state.token ? true : false
    },
    followingCnt(state) {
      return state.tempUser.follower_count
    },
    followerCnt(state) {
      return state.tempUser.following.length
    },
    profile_img(state) {
      return state.tempUser.profile_img
    },
    isFollowing(state) {
      let pushFollow = false
      state.user.following.forEach((element) => {
        if (element.id === state.tempUser.id) {
          pushFollow = true
        }
      })
      return pushFollow
      // return state.user.following.includes(state.tempUser.id)
    },
  },
  mutations: {
    // ***************************************************************
    // MOVIE
    // ***************************************************************
    // 인기 영화
    LOAD_POPULAR_MOVIE_LIST(state, response) {
      state.popularMovieList.movies = response
      // console.log(state.popularMovieList.movies)
    },
    // 평점순 영화
    LOAD_TOPRATED_MOVIE_LIST(state, response) {
      state.topratedMovieList.movies = response
      console.log(state.topratedMovieList.movies)
    },
    // 추천 영화
    LOAD_RECOMMEND_MOVIE_LIST(state, response) {
      state.recommendMovieList.movies = response
      console.log(state.recommendMovieList.movies)
    },
    // 현재 상영중 영화
    LOAD_NOW_PLAYING_MOVIE_LIST(state, response) {
      state.nowPlayingMovieList.movies = response
    },
    // 현재 상영중 영화(예고편)
    LOAD_NOW_PLAYING_MOVIE_VIDEO_LIST(state, response) {
      state.nowPlayingMovieVideoList.movies = response
    },
    LOAD_RECOMMEND_MOVIES_AT_DETAIL(state, response) {
      state.recommendMovieListAtDetail = response
    },
    // 키워드 검색 영화
    SEARCH_MOVIE_LIST(state, response) {
      state.searchMovieList = []
      state.searchMovieList.push(...response)
    },
    // detail로 들어갈 때 필요한 영화
    GET_MOVIE_BY_ID_AND_GO_DETAIL(state, response) {
      state.movie = response.movie
      router
        .push({ name: "detail", params: { id: response.id } })
        .catch(() => {}) // Avoided redundant navigation 에러 해결
    },

    // ***************************************************************
    // 인증 관련
    // ***************************************************************
    SAVE_TOKEN(state, data) {
      state.user = data.user
      state.token = data.access_token
      axios({
        method: "get",
        url: `${DJ_URL}/accounts/${data.user.pk}/user/`,
      }).then((res) => {
        state.user = res.data
      })
      router.push({ name: "home" })
    },
    DROP_TOKEN(state) {
      localStorage.removeItem("user")
      localStorage.removeItem("token")
      state.user = null
      state.token = null
      state.nickname = "로그인해주세요!"
      router.push({ name: "home" })
    },
    LOAD_ALL_USER_LIST(state, response) {
      state.allUserList = response
    },

    // ***************************************************************
    // COMMUNITY
    // ***************************************************************
    // DB에 저장된 모든 영화 데이터 가져오기
    LOAD_ALL_MOVIE_LIST(state, response) {
      state.allMovieList = response
    },
    // 피드 작성시 필요한 영화
    SEARCH_MOVIE(state, response) {
      state.feedMovie = response[0]
    },

    // 페이지 접근 시 유저 달력 불러오기
    // LOAD_USER_CALENDAR(state, response) {
    //   state.calendarItems =
    // },

    // 달력에 아이템 업데이트
    UPDATE_CALENDAR(state, response) {
      console.log("달력 업데이트!!!!")
      console.log("달력", response)
      state.calendarItems = response.map((element) => {
        const newObject = {
          cal_id: element.id,
          title: element.movie.title,
          start: element.start,
          image_url:
            "https://image.tmdb.org/t/p/original" + element.backdrop.path,
        }
        return newObject
      })
    },

    GET_BACKDROP_LIST(state, payload) {
      state.cal_movie_title = payload.movie_title
      state.feedMovieId = payload.movie_id
      state.feedBackDropList = payload.response
    },

    // 백드롭 리스트 초기화
    INITIALIZE_BACKDROP_LIST(state) {
      state.feedBackDropList = []
    },

    // 유저별 피드 리스트 받아오기
    LOAD_FEED_LIST(state, response) {
      console.log("현재 페이지 피드리스트 변경")
      state.feedList = response
    },
    // 나 포함, 팔로잉 유저 피드 받아오기
    LOAD_RELATED_FEED_LIST(state, response) {
      state.relatedFeedList = response
    },
    // 선택한 피드 가져오기
    LOAD_FEED(state, response) {
      state.selectedFeed = response
    },
    // 유저 가져오기
    GET_USER(state, response) {
      console.log("현재 페이지 유저 변경")
      state.tempUser = response
    },
    GET_ME(state, response) {
      state.user = response
    },
    // 전체 받은 메시지 반환
    LOAD_ALL_MESSAGE(state, response) {
      state.allMessage = response
    },
    // 안 읽은 메시지 반환
    LOAD_UNREAD_MESSAGE(state, response) {
      state.unreadMessage = response
    },
  },
  actions: {
    // ***************************************************************
    // MOVIE
    // ***************************************************************
    // 인기영화 서버 통신
    loadPopularMovieList(context) {
      axios({
        method: "get",
        url: `${DJ_URL}/movies/popular_movie/`,
      })
        .then((response) => {
          context.commit("LOAD_POPULAR_MOVIE_LIST", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 최고평점영화 서버 통신
    loadTopratedMovieList(context) {
      axios({
        method: "get",
        url: `${DJ_URL}/movies/top_rated_movie/`,
      })
        .then((response) => {
          context.commit("LOAD_TOPRATED_MOVIE_LIST", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 추천 영화 서버 통신
    loadRecommendMovieList(context, user_id) {
      axios({
        method: "get",
        url: `${DJ_URL}/accounts/${user_id}/recommend/`,
      })
        .then((response) => {
          console.log("되어주세여")
          console.log(response.data)
          context.commit("LOAD_RECOMMEND_MOVIE_LIST", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 현재 상영 중 영화 서버 통신
    loadNowPlayingMovieList(context) {
      axios({
        method: "get",
        url: `${DJ_URL}/movies/now_playing_movie/`,
      })
        .then((response) => {
          context.commit("LOAD_NOW_PLAYING_MOVIE_LIST", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 현재 상영 중 영화 예고편 서버 통신
    loadNowPlayingMovieVideoList(context) {
      axios({
        method: "get",
        url: `${DJ_URL}/movies/now_playing_movie_video/`,
      })
        .then((response) => {
          // console.log(response)
          context.commit("LOAD_NOW_PLAYING_MOVIE_VIDEO_LIST", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 디테일 페이지 추천 영화 서버 통신
    loadRecommendMoviesAtDetail(context, movie_id) {
      if (context.state.user) {
        axios({
          method: "get",
          params: {
            id: context.state.user.id,
          },
          url: `${DJ_URL}/movies/${movie_id}/recommend/`,
        })
          .then((response) => {
            context.commit("LOAD_RECOMMEND_MOVIES_AT_DETAIL", response.data)
          })
          .catch((error) => {
            console.log(error)
          })
      } else {
        axios({
          method: "get",

          url: `${DJ_URL}/movies/${movie_id}/recommend/`,
        })
          .then((response) => {
            context.commit("LOAD_RECOMMEND_MOVIES_AT_DETAIL", response.data)
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },
    // detail 영화 서버 통신
    getMovieById(context, movie_id) {
      axios({
        method: "get",
        params: {
          id: movie_id,
        },
        url: `${DJ_URL}/movies/movie_detail/`,
      })
        .then((response) => {
          const payload = {
            movie: response.data,
            id: movie_id,
          }
          context.commit("GET_MOVIE_BY_ID_AND_GO_DETAIL", payload)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovieIdByTitle(context, movie_title) {
      axios({
        method: "get",
        params: {
          title: movie_title,
        },
        url: `${DJ_URL}/movies/movie_id/`,
      })
        .then((response) => {
          context.dispatch("getMovieById", response.data.id)
        })
        .catch(() => {
          alert("영화아이디 못 받아옴")
        })
    },
    // 영화 검색 키워드 서버 통신 (영화감독,배우로 / 당장은 구현X)
    // searchMovieListByPerson(context, payload) {
    //   axios({
    //     method: "get",
    //     params: {
    //       search: payload.keyword,
    //       // genres: payload.genres,
    //     },
    //     url: `${DJ_URL}/movies/search_movie_people/`,
    //   })
    //     .then((response) => {
    //       context.commit("SEARCH_MOVIE_LIST", response.data)
    //       console.log(response)
    //     })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    // },
    // 영화 검색 키워드 서버 통신 (영화제목으로)
    searchMovieListByTitle(context, payload) {
      axios({
        method: "get",
        params: {
          search: payload.keyword,
          genres: payload.genres,
        },
        url: `${DJ_URL}/movies/search_movie/`,
      })
        .then((response) => {
          context.commit("SEARCH_MOVIE_LIST", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },

    // ***************************************************************
    // 인증 관련
    // ***************************************************************
    // 로그인 서버 통신
    logIn(context, payload) {
      axios({
        method: "post",
        url: `${DJ_URL}/accounts/login/`,
        data: {
          email: payload.email,
          password: payload.password,
        },
      }).then((res) => {
        context.commit("SAVE_TOKEN", res.data)
      })
    },
    // 카카오 로그인 서버 통신
    kakaoLogIn(context) {
      axios({
        method: "get",
        url: `${DJ_URL}/accounts/kakao/login`,
      }).then((res) => {
        context.commit("SAVE_TOKEN", res.data)
      })
    },
    // 회원 가입 서버 통신
    signUp(context, payload) {
      axios({
        method: "post",
        url: `${DJ_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          email: payload.email,
          password1: payload.password1,
          password2: payload.password2,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 로그아웃
    logOut(context) {
      context.commit("DROP_TOKEN")
    },
    // DB 내 모든 유저 받아오기
    loadAllUserList(context) {
      axios({
        method: "get",
        url: `${DJ_URL}/accounts/all_user_list/`,
      })
        .then((response) => {
          context.commit("LOAD_ALL_USER_LIST", response.data)
        })
        .catch((e) => {
          console.log("loadUser", e)
        })
    },

    // ***************************************************************
    // COMMUNITY
    // ***************************************************************
    // DB 내 모든 영화 받아오기 ([{id: , title: }] 형식)
    loadAllMovieList(context) {
      axios({
        method: "get",
        url: `${DJ_URL}/community/all_movie_list/`,
      })
        .then((response) => {
          context.commit("LOAD_ALL_MOVIE_LIST", response.data)
        })
        .catch((e) => {
          console.log("loadMovie", e)
        })
    },

    // 유저 검색 서버 통신
    searchUser(context, userName) {
      axios({
        method: "get",
        params: {
          search: userName,
        },
        url: `${DJ_URL}/movies/search_user/`,
      })
        .then((response) => {
          console.log(response)
          // context.commit("SEARCH_MOVIE_LIST", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 닉네임으로 유저 반환
    getUser(context, username) {
      if (username) {
        axios({
          method: "get",
          params: {
            name: username,
          },
          url: `${DJ_URL}/accounts/get_user/`,
        })
          .then((response) => {
            context.commit("GET_USER", response.data)
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },
    // 나 반환
    getMe(context, username) {
      axios({
        method: "get",
        params: {
          name: username,
        },
        url: `${DJ_URL}/accounts/get_user/`,
      })
        .then((response) => {
          context.commit("GET_ME", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    follow(context, payload) {
      axios({
        method: "post",
        data: {
          id: payload.me,
        },
        url: `${DJ_URL}/accounts/${payload.you}/follow/`,
      })
        .then((response) => {
          console.log(response.data)
          context.dispatch("getMe", context.state.user.username)
          context.dispatch("getUser", context.state.tempUser.username)
        })
        .catch(() => {
          alert("팔로우 실패!!!")
        })
    },
    // 피드(리뷰)에서 영화 검색 -> 백드롭 이미지 5개 받아오기
    getBackDropList(context, movie_id) {
      console.log("여기 들어와야 합", movie_id)
      axios({
        method: "get",
        params: {
          id: movie_id,
        },
        url: `${DJ_URL}/community/get_backdrop/`,
      }).then((response) => {
        const payload = {
          movie_id: movie_id,
          response: response.data.backdrops,
          movie_title: response.data.title,
        }
        context.commit("GET_BACKDROP_LIST", payload)
      })
    },
    // 피드 작성
    addFeed(context, payload) {
      axios({
        method: "post",
        data: {
          title: payload.title,
          content: payload.content,
          backdrop: payload.img_id,
          user: context.state.user.id,
        },
        url: `${DJ_URL}/community/${payload.movie_id}/create_review/`,
      })
        .then((response) => {
          context.state.feedList.push(response.data)
        })
        .catch(() => {
          alert("필수 항목이 빠졌어요!!")
        })
    },
    // 피드 수정
    updateFeed(context, payload) {
      axios({
        method: "put",
        data: {
          title: payload.title,
          content: payload.content,
          backdrop: payload.img_id,
          user: context.state.user.id,
        },
        url: `${DJ_URL}/community/review/${payload.feed_id}/`,
      })
        .then(() => {
          context.dispatch("loadFeedList", context.state.user.username)
        })
        .catch(() => {
          console.log("업데이트 실패")
        })
    },

    //피드 삭제
    deleteFeed(context, feed_id) {
      axios({
        method: "delete",
        url: `${DJ_URL}/community/review/${feed_id}/`,
      })
        .then((response) => {
          context.dispatch("loadFeedList", response.data)
        })
        .catch(() => {
          alert("필수 항목이 빠졌어요!!")
        })
    },

    // 유저 달력 불러오기
    loadUserCalendar(context, user_id) {
      axios({
        method: "get",
        url: `${DJ_URL}/community/calendar/list/${user_id}/`,
      }).then((response) => {
        context.commit("UPDATE_CALENDAR", response.data)
      })
    },
    // 달력에 아이템 추가
    addCalendar(context, payload) {
      axios({
        method: "post",
        data: {
          movie: payload.movie_id,
          backdrop: payload.backdrop_id,
          user: context.state.user.id,
          start: payload.start,
        },
        url: `${DJ_URL}/community/calendar/create/`,
      }).then((response) => {
        context.commit("UPDATE_CALENDAR", response.data)
      })
    },
    // 달력에 아이템 삭제
    deleteCalendar(context, start) {
      console.log(start, context.state.user.id)
      axios({
        method: "post",
        data: {
          user: context.state.user.id,
          start: start,
        },
        url: `${DJ_URL}/community/calendar/delete/`,
      }).then((response) => {
        context.commit("UPDATE_CALENDAR", response.data)
      })
    },

    // 유저별 피드 받아오기
    loadFeedList(context, username) {
      axios({
        method: "get",
        url: `${DJ_URL}/community/review/${username}`,
      }).then((response) => {
        console.log("받아오기 성공", response)
        context.commit("LOAD_FEED_LIST", response.data)
      })
    },

    // 나 포함 팔로잉 피드 받아오기
    loadRelatedFeedlist(context, user_id) {
      axios({
        method: "get",
        url: `${DJ_URL}/community/feed/${user_id}`,
      })
        .then((response) => {
          context.commit("LOAD_RELATED_FEED_LIST", response.data)
          console.log(response.data)
        })
        .catch((e) => {
          console.log("에러발생", e)
        })
    },

    // 좋아요 클릭 -> DB에 저장
    clickLikeBtn(context, payload) {
      axios({
        method: "post",
        url: `${DJ_URL}/community/review/${payload.feed_id}/like/`,
        data: {
          id: payload.user_id,
        },
      })
        .then(() => {
          // 저장 성공했으면 받아온 피드 정보 업데이트
          context.dispatch("loadFeedList", context.state.tempUser.username)
          context.dispatch("loadRelatedFeedlist", context.state.user.id)
          context.dispatch("loadFeed", payload.feed_id)
        })
        .catch((e) => {
          console.log("에러가 발생", e)
        })
    },

    // 댓글 작성
    createComment(context, payload) {
      axios({
        method: "post",
        url: `${DJ_URL}/community/review/${payload.feed_id}/create_comment/`,
        data: {
          user: payload.user_id,
          content: payload.content,
        },
      })
        .then(() => {
          // 저장 성공했으면 받아온 피드 정보 업데이트
          context.dispatch("loadFeed", payload.feed_id)
        })
        .catch((e) => {
          console.log("에러가 발생", e)
        })
    },
    // 댓글 삭제
    deleteComment(context, payload) {
      axios({
        method: "delete",
        url: `${DJ_URL}/community/comment/${payload.comment_id}/`,
      }).then((response) => {
        console.log(response)
        context.dispatch("loadFeed", payload.feed_id)
      })
    },

    // 피드 아이디로 피드 조회
    loadFeed(context, feed_id) {
      axios({
        method: "get",
        url: `${DJ_URL}/community/review/${feed_id}`,
      }).then((response) => {
        context.commit("LOAD_FEED", response.data)
      })
    },

    // 프로필 수정
    editProfile(context, payload) {
      axios({
        method: "post",
        url: `${DJ_URL}/accounts/edit_profile/`,
        data: {
          id: context.state.user.id,
          profile_img: payload.profile_img,
          description: payload.description,
          genre_id_list: payload.selectedGenreIds,
        },
      })
        .then((response) => {
          console.log(payload)
          console.log("프로필 변경 완료!!", response)
          context.dispatch("getMe", context.state.user.username)
        })
        .catch((e) => {
          console.log("프로필 변경 실패", e)
        })
    },
    // 북마크 추가/해제
    clickBookmark(context, id) {
      axios({
        method: "post",
        url: `${DJ_URL}/community/${id}/bookmark/`,
        data: {
          user: context.state.user.id,
        },
      })
        .then((response) => {
          console.log("북마크 완료!!", response)
          context.dispatch("getMe", context.state.user.username)
          context.dispatch("getUser", context.state.user.username)
        })
        .catch((e) => {
          console.log("북마크 실패", e)
        })
    },
    // 메시지 보내기
    sendMessage(context, payload) {
      axios({
        method: "post",
        data: {
          from_user: payload.from_user_id,
          to_user: payload.to_user_id,
          content: payload.content,
        },
        url: `${DJ_URL}/community/${payload.movie_id}/send_message/`,
      })
        .then((response) => {
          // 메시지 보내기 성공했으면
          console.log("메시지 보내기 성공")
          console.log(response)
        })
        .catch(() => {
          alert("메시지 보내기 실패...")
        })
    },
    // 모든 메시지 목록 받아오기
    loadAllMessageList(context, user_id) {
      axios({
        method: "get",
        url: `${DJ_URL}/community/message/list/${user_id}/`,
      }).then((response) => {
        context.commit("LOAD_ALL_MESSAGE", response.data)
      })
    },
    // 안읽은 메시지 목록 받아오기
    loadUnreadMessageList(context, user_id) {
      axios({
        method: "get",
        url: `${DJ_URL}/community/message/new/${user_id}/`,
      }).then((response) => {
        context.commit("LOAD_UNREAD_MESSAGE", response.data)
      })
    },
    // 메시지 읽음 표시
    checkReed(context, message_id) {
      console.log("메시지 읽음", message_id)
      axios({
        method: "post",
        data: {
          message_id: message_id,
        },
        url: `${DJ_URL}/community/message/check/${context.state.user.id}/`,
      }).then(() => {
        context.dispatch("loadAllMessageList", context.state.user.id)
        context.dispatch("loadUnreadMessageList", context.state.user.id)
      })
    },
  },

  modules: {},
})
