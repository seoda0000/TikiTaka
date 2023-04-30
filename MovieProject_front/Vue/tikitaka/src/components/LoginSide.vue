<template>
  <div id="box" style="margin-top: auto; margin-bottom: auto">
    <img
      src="../assets/side_login.jpg"
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
    <!-- <div
      style="
        width: 50%;
        height: 50%;
        background-color: white;
        position: absolute;
        opacity: 0.7;
        z-index: 1;
        left: 0;
        top: 50%;
      "
    >
      <p></p>
    </div> -->
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
            Let's <br/>
            TikiTaka
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
            아직 회원이 아니신가요?
          </span>
          <br />
          <v-btn color="white" style="margin-top: 10px" @click="goSignUp"
            >Sign Up</v-btn
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
    goSignUp() {
      this.$router.push({ name: "signup" })
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
