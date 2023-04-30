<template>
  <div style="margin-left: auto; margin-right: auto; margin-top: 150px">
    <v-card
      style="display: flex; margin: auto; max-width: 800px; height: 500px"
    >
      <SignupSide />
      <SignupPage />
    </v-card>
  </div>
</template>

<script>
import SignupPage from "@/components/SignupPage"
import SignupSide from "@/components/SignupSide"
export default {
  name: "SignupView",
  components: {
    SignupPage,
    SignupSide,
  },

  computed: {},
}
</script>
