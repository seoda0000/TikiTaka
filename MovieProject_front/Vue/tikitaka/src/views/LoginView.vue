<template>
  <div
    style="
      /* display: flex; */
      margin-left: auto;
      margin-right: auto;
      margin-top: 150px;
      /* margin-bottom: auto; */
      /* max-width: 800px; */
      /* height: 500px; */
    "
  >
    <v-card
      style="
        display: flex;
        margin-left: auto;
        margin-right: auto;
        margin-top: auto;
        margin-bottom: auto;
        max-width: 800px;
        height: 500px;
      "
    >
      <LoginSide />
      <LoginPage />
    </v-card>
  </div>
</template>

<script>
import LoginPage from "@/components/LoginPage"
import LoginSide from "@/components/LoginSide"
export default {
  name: "LogInView",
  components: {
    LoginPage,
    LoginSide,
  },

  computed: {},
}
</script>
