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
    <div>
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
      <v-btn dark height="45" @click="updateFeed" style="float: right"
        >SAVE</v-btn
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "FeedUpdateModal",
  props: {
    clickedFeed: Object,
  },
  data() {
    return {
      title: this.clickedFeed.title,
      content: this.clickedFeed.content,
      selectedImgId: this.clickedFeed.backdrop.id, // 선택한 이미지 백드롭 아이디
      selectedImgPath: this.clickedFeed.backdrop.path, // 선택한 이미지 백드롭 키(path)
    }
  },
  computed: {
    feedBackDropList() {
      return this.$store.state.feedBackDropList
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
    },
    updateFeed() {
      const payload = {
        img_id: this.selectedImgId,
        title: this.title,
        content: this.content,
        feed_id: this.clickedFeed.id,
      }
      this.$store.dispatch("updateFeed", payload)
      this.$emit("close-modal")
      this.$store.commit("INITIALIZE_BACKDROP_LIST")
    },
  },
  created() {
    this.$store.dispatch("getBackDropList", this.clickedFeed.movie.id)
  },
}
</script>

<style></style>
