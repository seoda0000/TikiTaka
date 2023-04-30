<template>
  <div>
    <!-- 포스터 선택 영역 -->
    <div>
      <h4>SELECT POSTER</h4>
      <v-sheet style="background-color: transparent">
        <v-slide-group active-class="success" show-arrows>
          <div v-for="backdrop in feedBackDropList" :key="backdrop.id">
            <v-slide-item class="mx-2">
              <v-btn dark height="150px">
                <img
                  width="220px"
                  :src="`https://image.tmdb.org/t/p/original${backdrop.path}`"
                  @click="selectImage(backdrop)"
                />
              </v-btn>
            </v-slide-item>
          </div>
        </v-slide-group>
      </v-sheet>
    </div>

    <!-- 피드 작성 요청시 렌더링 될 영역 -->
    <div v-show="isFeedRequest">
      <hr class="mt-5 mb-4" />
      <!-- (title, content 작성 영역) -->
      <h4>TITLE</h4>
      <div>
        <v-text-field
          outlined
          type="text"
          :value="title"
          @input.native="inputTitle"
        >
        </v-text-field>
      </div>

      <h4>CONTENT</h4>
      <v-textarea
        outlined
        type="text"
        :value="content"
        @input.native="inputContent"
      >
      </v-textarea>

      <!-- 피드 작성 완료 버튼 -->
      <v-btn dark height="45" @click="addFeed" style="float: right"
        >CREATE</v-btn
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "FeedCreateForm",
  props: {
    isFeedRequest: Boolean,
    isCalendarRequest: Boolean,
    feedMovieId: Number,
    feedBackDropList: Array,
  },
  data() {
    return {
      title: null,
      content: null,
      selectedImgId: this.feedBackDropList[0].id, // 선택한 이미지 백드롭 아이디
      selectedImgPath: this.feedBackDropList[0].path, // 선택한 이미지 백드롭 키(path)
    }
  },
  computed: {
    movie_title() {
      return this.$store.state.cal_movie_title
    },
  },
  methods: {
    inputTitle(event) {
      this.title = event.target.value
    },
    inputContent(event) {
      this.content = event.target.value
    },
    selectImage(backdrop) {
      this.selectedImgId = backdrop.id
      this.selectedImgPath = backdrop.path
      // const selectedImgUrl =
      //   "https://image.tmdb.org/t/p/original" + this.selectedImgPath
      const payload = {
        movie_id: this.feedMovieId,
        backdrop_id: this.selectedImgId,
        img_url: "https://image.tmdb.org/t/p/original" + this.selectedImgPath,
        title: this.movie_title,
      }
      this.$emit("select-image-for-calendar", payload)
    },
    addFeed() {
      const payload = {
        movie_id: this.feedMovieId,
        img_id: this.selectedImgId,
        title: this.title,
        content: this.content,
      }
      this.$store.dispatch("addFeed", payload)
      this.$emit("close-modal")
      this.$store.commit("INITIALIZE_BACKDROP_LIST")
    },
    addCalendar() {
      const selectedImgUrl =
        "https://image.tmdb.org/t/p/original" + this.selectedImgPath
      this.$emit("add-calendar", selectedImgUrl)
    },
  },
  created() {
    // console.log(this.feedMovieId)
    // console.log(this.$store.state.movie)
    // console.log("어디보자", this.feedBackDropList)
  },
}
</script>

<style></style>
