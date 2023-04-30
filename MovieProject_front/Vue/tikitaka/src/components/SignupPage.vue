<template>
  <div
    style="
      margin-left: auto;
      margin-right: auto;
      margin-top: 50px;
      margin-bottom: 50px;
    "
  >
    <form @submit.prevent="signUp" style="margin: auto; width: 80%">
      <v-text-field
        type="text"
        id="username"
        v-model="username"
        label="Username"
        :rules="nameRules"
        :counter="10"
        required
      ></v-text-field>
      <v-text-field
        type="text"
        id="email"
        v-model="email"
        label="E-mail"
        :rules="emailRules"
        required
      ></v-text-field>
      <v-text-field
        type="password"
        id="password"
        v-model="password1"
        label="password"
        :rules="passwordRules"
        required
      /><v-text-field
        type="password"
        id="password2"
        v-model="password2"
        label="Confirm password"
        :rules="passwordRules"
        required
      />

      <v-btn
        @click="signUp"
        style="width: 100%; margin: 10px 0px 10px"
        color="secondary"
        >Sign Up</v-btn
      >
      <v-btn @click="kakaoLogIn" style="width: 100%" color="yellow"
        >카카오로 계속하기</v-btn
      >
    </form>
  </div>
</template>

<script>
export default {
  name: "SignupPage",
  data() {
    return {
      username: "",
      email: null,
      password1: null,
      password2: null,
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+/.test(v) || "E-mail must be valid",
      ],
      nameRules: [
        (v) => !!v || "Username is required",
        (v) => v.length <= 10 || "username must be less than 10 characters",
      ],
      passwordRules: [(v) => !!v || "Password is required"],
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const email = this.email
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username,
        email,
        password1,
        password2,
      }

      this.$store.dispatch("signUp", payload)
    },
  },

  computed: {},
  mounted: {},
}
</script>

<style></style>
