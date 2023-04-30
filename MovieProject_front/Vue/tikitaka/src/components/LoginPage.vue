<template>
  <!-- 말풍선 보류 -->
  <!-- <div style="display:flex;">
    <div style="margin-left:auto; margin-right: 10%;;">
      <div id="bubble">
        <div style="margin-right:25px; width: 90%;">
          <form @submit.prevent="logIn" style="margin: auto; width: 60%;">
            <h1 style="margin:auto; text-align: center;">Log In</h1>
            <br/>
            <v-text-field
              type="text" id="email" v-model="email" label="E-mail"
              :rules="emailRules"
              required
            >
            </v-text-field>
            <v-text-field
              type="text" id="password" v-model="password" label="password"
              :rules="passwordRules"
              required
            />
            <v-btn @click="logIn" style="width: 100%; margin: 10px 0px 10px;" color="secondary">submit</v-btn>
            <v-btn @click="kakaoLogIn" style="width: 100%" color="yellow">카카오로 로그인</v-btn>
            <br/>
          </form>
        </div>
      </div>
      <img
        src="../assets/tikitaka_logo_l.png" alt=""
        style="width: 200px; margin-left: 300px; margin-top: -100px;"
      />
    </div>
  </div> -->

  <div
    style="
      margin-left: auto;
      margin-right: auto;
      margin-top: auto;
      margin-bottom: auto;
    "
  >
    <form @submit.prevent="logIn" style="margin: auto; width: 80%">
      <h1 class="mainText" style="margin: auto; text-align: center">Log In</h1>
      <br />
      <v-text-field
        type="text"
        id="email"
        v-model="email"
        label="E-mail"
        :rules="emailRules"
        required
      >
      </v-text-field>
      <v-text-field
        type="password"
        id="password"
        v-model="password"
        label="password"
        :rules="passwordRules"
        required
        @keyup.enter="logIn"
      />
      <v-btn
        @click="logIn"
        style="width: 100%; margin: 10px 0px 10px"
        color="secondary"
        >submit</v-btn
      >
      <v-btn @click="kakaoLogIn" style="width: 100%" color="yellow"
        >카카오로 로그인</v-btn
      >
      <br />
      <br />
    </form>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+/.test(v) || "E-mail must be valid",
      ],
      passwordRules: [
        (v) => !!v || "Password is required",
        // v => v.length <= 10 || 'Name must be less than 10 characters',
      ],
    }
  },
  methods: {
    logIn() {
      const email = this.email
      const password = this.password
      const payload = {
        email,
        password,
      }
      this.$store.dispatch("logIn", payload)
    },
    kakaoLogIn() {
      this.$store.dispatch("kakaoLogIn")
    },
  },
  computed: {},
  mounted: {},
}
</script>

<style>
#bubble {
  width: 353px;
  height: 400px;
  background-image: url("../assets/bubble2.png");
  background-size: cover;
  display: flex;
  align-content: center;
  align-items: center;
  /* margin: auto; */
  margin-top: 50px;
}
</style>
