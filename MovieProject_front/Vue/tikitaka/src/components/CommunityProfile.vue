<template>
  <div style="width: 100%">
    <v-sheet
      id="profile-box"
      class="mainText"
      elevation="3"
      style="width: 230px"
    >
      <div>
        <!-- 프로필 이미지 -->
        <img
          :src="require(`@/assets/tikitaka_${profile_img}.png`)"
          id="profile-image"
          style="width: 100%; max-width: 200px"
        />
        <!-- 프로필 텍스트 영역 -->
        <div id="profile-content-box">
          <!-- 닉네임 -->
          <h2 style="margin-left: 20px">{{ user.username }}</h2>

          <!-- 영화 MBTI -->
          <!-- <p style="color: gray; margin-top: -7px">나만의 감성 (CJI)</p> -->
          <!-- 팔로워/팔로잉/피드 수 -->
          <div id="profile-count-box">
            <!-- 게시물 수(포스트) -->
            <div style="margin-left: 10px; margin-right: 10px">
              {{ user.review_count }}
              <p style="color: gray; font-size: 14px">Posts</p>
            </div>
            <!-- 팔로워 수 -->
            <div style="margin-left: 10px; margin-right: 10px">
              {{ followingCnt }}
              <p style="color: gray; font-size: 14px">Followers</p>
            </div>
            <!-- 팔로잉 수 -->
            <div style="margin-left: 10px; margin-right: 10px">
              {{ followerCnt }}
              <p style="color: gray; font-size: 14px">Following</p>
            </div>
          </div>
          <div v-if="!isMyPage">
            <v-btn v-if="!isFollowing" style="width: 100%" @click="follow"
              >Follow</v-btn
            >
            <v-btn v-if="isFollowing" style="width: 100%" @click="follow"
              >Unfollow</v-btn
            >
          </div>
          <v-btn v-if="isMyPage" style="width: 100%" @click="openEditProfile"
            >Edit Profile</v-btn
          >
          <hr />
          <!-- IDENTITY 태그 -->
          <h6 class="logoText">ABOUT ME</h6>
          <p>
            {{ user.description }}
          </p>

          <hr />
          <!-- 좋아하는 장르 태그 -->
          <h6 class="logoText">FAVORITE GENRES</h6>
          <div id="profile-tag-box">
            <community-profile-genre
              v-for="(genre, idx) in user.favorite_genres"
              :key="idx"
              :genre="genre"
              >여기요!!!!!!!!{{ genre }}</community-profile-genre
            >
          </div>
        </div>
      </div>
    </v-sheet>

    <!-- 프로필 변경 모달 -->
    <b-modal hide-footer hide-header-close id="profileEditModal">
      <template #modal-header>
        <h3 class="logoText">EDIT YOUR PROFILE</h3>
      </template>
      <!-- 프로필 이미지 -->
      <img :src="selectImgUrl" class="modal-profile-main-image" />
      <br /><br />
      <!-- 선택가능 프로필 이미지 -->
      <h5><strong>프로필 변경 이미지 선택</strong></h5>
      <div>
        <input type="radio" id="img1" style="display: none" name="radio" />
        <label for="img1">
          <img
            src="../assets/tikitaka_chips.png"
            @click="selectImage"
            class="modal-profile-sub-image"
          />
        </label>
        <input type="radio" id="img2" style="display: none" name="radio" />
        <label for="img2">
          <img
            src="../assets/tikitaka_coke.png"
            @click="selectImage"
            class="modal-profile-sub-image"
          />
        </label>
        <input type="radio" id="img3" style="display: none" name="radio" />
        <label for="img3">
          <img
            src="../assets/tikitaka_coffee.png"
            @click="selectImage"
            class="modal-profile-sub-image"
          />
        </label>
        <input type="radio" id="img4" style="display: none" name="radio" />
        <label for="img4">
          <img
            src="../assets/tikitaka_film.png"
            @click="selectImage"
            class="modal-profile-sub-image"
          />
        </label>
        <input type="radio" id="img5" style="display: none" name="radio" />
        <label for="img5">
          <img
            src="../assets/tikitaka_hotdog.png"
            @click="selectImage"
            class="modal-profile-sub-image"
          />
        </label>
        <input type="radio" id="img6" style="display: none" name="radio" />
        <label for="img6">
          <img
            src="../assets/tikitaka_nacho.png"
            @click="selectImage"
            class="modal-profile-sub-image"
          />
        </label>
        <input type="radio" id="img7" style="display: none" name="radio" />
        <label for="img7">
          <img
            src="../assets/tikitaka_popcorn.png"
            @click="selectImage"
            class="modal-profile-sub-image"
          />
        </label>
        <input type="radio" id="img8" style="display: none" name="radio" />
        <label for="img8">
          <img
            src="../assets/tikitaka_ticket.png"
            @click="selectImage"
            class="modal-profile-sub-image"
          />
        </label>
      </div>

      <hr />
      <!-- 외부 파일 첨부 -->
      <!-- <div>
        <p>
          <input type="file" id="file" />
          <label for="file"></label>
        </p>
      </div> -->

      <!-- 본인 소개글 -->
      <h5><strong>본인 소개</strong></h5>
      <v-text-field outlined v-model="description"></v-text-field>

      <!-- 좋아하는 장르 -->
      <h5><strong>선호하는 장르</strong></h5>
      <v-col cols="12">
        <v-combobox
          outlined
          v-model="select"
          :items="items"
          multiple
          chips
          style="margin-left: -17px"
        ></v-combobox>
      </v-col>

      <v-btn dark height="45" style="float: right" @click="editProfile"
        >SAVE</v-btn
      >
    </b-modal>
  </div>
</template>

<script>
function matchGenreId(name) {
  switch (name) {
    case "모험":
      return 12
    case "판타지":
      return 14
    case "애니메이션":
      return 16
    case "드라마":
      return 18
    case "공포":
      return 27
    case "액션":
      return 28
    case "코미디":
      return 35
    case "역사":
      return 36
    case "서부":
      return 37
    case "스릴러":
      return 53
    case "범죄":
      return 80
    case "다큐멘터리":
      return 99
    case "SF":
      return 878
    case "미스터리":
      return 9648
    case "음악":
      return 10402
    case "로맨스":
      return 10749
    case "가족":
      return 10751
    case "전쟁":
      return 10752
    case "TV 영화":
      return 10770
  }
}
import CommunityProfileGenre from "@/components/CommunityProfileGenre.vue"

export default {
  components: { CommunityProfileGenre },
  name: "CommunityProfile",
  props: {
    user: Object,
  },
  data() {
    return {
      // profileImgUrl: require(`@/assets/tikitaka_${this.$store.state.tempUser.profile_img}.png`),
      isSelected: false,
      description: "",
      selectImgUrl: null,
      // select: this.user.favorite_genres,
      select: [],
      items: [
        "모험",
        "판타지",
        "애니메이션",
        "공포",
        "액션",
        "코미디",
        "역사",
        "서부",
        "스릴러",
        "범죄",
        "다큐멘터리",
        "SF",
        "미스터리",
        "음악",
        "로맨스",
        "가족",
        "전쟁",
        "TV 영화",
      ],
    }
  },
  computed: {
    // userame() {
    //   return this.$route.params.username
    // },
    isMyPage() {
      if (this.$route.params.username) {
        return this.$store.state.user.username === this.$route.params.username
      } else {
        return true
      }
    },
    isFollowing() {
      return this.$store.getters.isFollowing
    },
    followingCnt() {
      return this.$store.getters.followingCnt
    },
    followerCnt() {
      return this.$store.getters.followerCnt
    },
    profile_img() {
      return this.$store.getters.profile_img
    },
    profileImgUrl() {
      return require(`@/assets/tikitaka_${this.$store.state.tempUser.profile_img}.png`)
    },
  },
  methods: {
    follow() {
      const payload = {
        me: this.$store.state.user.id,
        you: this.user.id,
      }
      return this.$store.dispatch("follow", payload)
    },
    openEditProfile() {
      this.selectImgUrl = this.profileImgUrl
      this.$bvModal.show("profileEditModal")
    },
    selectImage(event) {
      this.selectImgUrl = event.target.src
    },
    editProfile() {
      let imgKeyword = this.selectImgUrl
      let i = imgKeyword.indexOf("_")
      imgKeyword = imgKeyword.slice(i + 1)
      i = imgKeyword.indexOf(".")
      imgKeyword = imgKeyword.slice(0, i)
      const selectedGenreIds = []
      this.select.forEach((element) => {
        const id = matchGenreId(element)
        selectedGenreIds.push(id)
      })
      const payload = {
        profile_img: imgKeyword,
        description: this.description,
        selectedGenreIds: selectedGenreIds,
      }
      this.$store.dispatch("editProfile", payload)
      this.$store.dispatch("getUser", this.tempUser.username)
      this.$bvModal.hide("profileEditModal")
      this.selectImgUrl = this.profileImgUrl
      this.select = []
    },
  },
}
</script>

<style>
#profile-box {
  border-radius: 15px;
  /* padding: 30px 10px; */
  background-color: white;
  position: fixed;
  /* margin: auto; */
  /* max-width: 17%; */
  width: 100%;
}

#profile-content-box {
  background-color: white;
  /* border: 7px black solid; */
  border-radius: 40px;
  margin-top: -30px;
  padding: 30px 10px;
}

#profile-image {
  width: 200px;
  border-radius: 50%;
  border: 10px solid white;
  display: block;
  margin: 0px auto;
}

#profile-count-box {
  text-align: center;
  display: flex;
  justify-content: space-around;
}

.modal-profile-main-image {
  width: 40%;
  margin: 5px;
  border-radius: 50%;
}
.modal-profile-sub-image {
  width: 100px;
  margin: 5px;
}
input:checked + label > img {
  border: 4px solid black;
}
</style>
