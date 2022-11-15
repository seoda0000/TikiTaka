import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

import axios from "axios"
// const API_KEY = "70b2ea614813cf15cf942ed13cffefa7"
// const TOP_RATED_URL = "https://api.themoviedb.org/3/movie/top_rated"
const DJ_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  state: {
    movieList: [],
  },
  getters: {},
  mutations: {
    LOAD_MOVIE_LIST(state, response) {
      for (const movie of response) {
        console.log(movie)
        // overview 존재하는 영화만 가져오기
        if (movie.overview.length > 0) {
          state.movieList.push(movie)
        }
      }
    },
  },
  actions: {
    loadMovieList(context) {
      axios({
        method: "get",
        url: `${DJ_URL}/movies/popular_movie/`,
        // params: {
        //   api_key: API_KEY,
        //   language: "ko-KR",
        // },
        // headers: {

        // }
      })
        .then((response) => {
          context.commit("LOAD_MOVIE_LIST", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  modules: {},
})
