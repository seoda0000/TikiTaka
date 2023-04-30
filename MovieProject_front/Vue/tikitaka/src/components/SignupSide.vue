<template>
  <div id="box" style="margin-top: auto; margin-bottom: auto">
    <img
      src="../assets/side_signup.jpg"
      alt=""
      style="
        height: 100%;
        max-width: 50%;
        position: absolute;
        object-fit: cover;
        left: 0;
        top: 0;
        z-index: 1;
      "
    />
    <div>
      <div style="z-index: 10; position: relative">
        <img src="../assets/tikitaka_logo_r.png" alt="" style="width: 150px" />
        <div style="z-index: 20">
          <h1
            class="logoText"
            style="
              margin: auto;
              color: black;
              text-shadow: -2px 0 #fff, 0 2px #fff, 2px 0 #fff, 0 -2px #fff;
            "
          >
            Welcome to TikiTaka
          </h1>
          <br />
          <span
            class="mainText"
            style="
              margin: auto;
              color: white;
              background-color: black;
              padding: 5px;
            "
          >
            티키타카 회원이신가요?
          </span>
          <br />
          <v-btn color="white" style="margin-top: 10px" @click="goLogIn"
            >Log In</v-btn
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginSide",
  methods: {
    goLogIn() {
      this.$router.push({ name: "login" })
    },
  },
}
</script>

<style>
#box {
  width: 50%;
  /* background-color: white; */
  text-align: center;
  /* background-image: url(../assets/cinema-glasses-popcorn.jpg); */
  /* background-size: 300%; */
}
/* #box::after {
  width: 100%;
  height: 100%;
  content: "";
  background: url(../assets/cinema-glasses-popcorn.jpg);
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
} */
</style>
