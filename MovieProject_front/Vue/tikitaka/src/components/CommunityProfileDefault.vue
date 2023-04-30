<template>
  <div style="width: 100%">
    <v-sheet
      id="profile-box"
      class="mainText"
      elevation="3"
      style="width: 230px"
    >
      <div>
        <img
          src="@/assets/tikitaka_logo_r.png"
          id="profile-image2"
          style="width: 100%; max-width: 160px"
        />
        <div id="profile-content-box">
          <div id="profile-count-box">
            <div style="margin-left: 10px; margin-right: 10px">
              <h2>Let's TikiTaka!</h2>
              나만의 영화 커뮤니티
              <p style="color: gray; font-size: 14px">로그인 해주세요</p>
              <v-btn style="width: 100%" dark @click="goLogIn">Login</v-btn>
            </div>
          </div>
          <hr />
          <h6 class="logoText">Contact</h6>
          https://github.com/Going777 <br />
          https://github.com/seoda0000
        </div>
      </div>
    </v-sheet>
  </div>
</template>

<script>
export default {
  name: "CommunityProfile",

  methods: {
    goLogIn() {
      this.$router.push({ name: "login" })
    },
  },
}
</script>

<style>
#profile-box {
  border-radius: 15px;
  padding: 30px 10px;
  background-color: white;
  position: fixed;
  margin: auto;
  width: 17%;
}

#profile-content-box {
  background-color: white;
  /* border: 7px black solid; */
  border-radius: 40px;
  /* margin-top: -30px; */
  padding: 30px 10px;
}

#profile-image2 {
  width: 200px;
  border-radius: 50%;
  border: 6px solid black;
  display: block;
  margin: 0px auto 30px;
}

#profile-count-box {
  text-align: center;
  display: flex;
  justify-content: space-around;
}
</style>
