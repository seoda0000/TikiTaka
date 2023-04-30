<template>
  <div class="mainText">
    <!-- 영화 선택(검색) -->
    <div class="mb-3" style="width: 40%; margin-left: -15px">
      <div style="margin-top: 30px">
        <v-toolbar flat dense>
          <v-autocomplete
            clearable
            outlined
            auto-select-first
            :loading="loading"
            :search-input.sync="searchMovie"
            :items="items"
            item-text="title"
            item-value="id"
            v-model="select"
            @change="selectMovie"
            label="Select Movies..."
          ></v-autocomplete>
        </v-toolbar>
      </div>
    </div>

    <!-- 피드 작성 폼(포스터 선택 & 내용 채우기) // 수정할 때 & 디테일 페이지에서 작성할 때 재사용!!! -->
    <feed-create-form
      :isFeedRequest="isFeedRequest"
      :isCalendarRequest="isCalendarRequest"
      :feedMovieId="feedMovieId"
      :feedBackDropList="feedBackDropList"
      @close-modal="closeModal"
      @select-image-for-calendar="selectImageForCalendar"
    />
  </div>
</template>

<script>
import FeedCreateForm from "./FeedCreateForm.vue"
export default {
  components: { FeedCreateForm },
  name: "FeedCreateModal",
  props: {
    isFeedRequest: Boolean,
    isCalendarRequest: Boolean,
  },
  data() {
    return {
      keyword: "",
      loading: false,
      items: [],
      searchMovie: null,
      select: null,
      movies: this.$store.state.allMovieList,
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    },
    feedMovieId() {
      return this.$store.state.feedMovieId
    },
    feedBackDropList() {
      return this.$store.state.feedBackDropList
    },
  },
  watch: {
    searchMovie(val) {
      val && val !== this.select && this.querySelections(val)
    },
  },
  methods: {
    querySelections(v) {
      this.loading = true
      setTimeout(() => {
        this.items = this.movies.filter((e) => {
          return (
            (e.title || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1
          )
        })
        this.loading = false
      }, 500)
    },
    selectMovie() {
      this.$store.dispatch("getBackDropList", this.select)
    },
    closeModal() {
      this.$emit("close-modal")
    },
    selectImageForCalendar(payload) {
      this.$emit("select-image-for-calendar", payload)
    },
  },
}
</script>

<style></style>
