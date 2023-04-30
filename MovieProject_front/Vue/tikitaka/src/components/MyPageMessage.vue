<template>
  <div>
    <div class="m-3">
      <h5 v-if="isNoneMessage">메시지함이 비었습니다!</h5>
      <h5 v-else>안 읽은 메시지가 {{ unreadMessageCnt }}통 있습니다!</h5>
    </div>

    <v-card flat width="100%">
      <div class="m-3">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-2">
          <div v-for="message in allMessage" :key="message.id">
            <div class="col m-1">
              <b-card
                :img-src="`https://image.tmdb.org/t/p/original/${message.movie.poster_path}`"
                img-alt="Card image"
                img-right
                v-if="message"
                style="height: 15rem; margin-bottom: 25px"
                class="shadow p-1 mb-5 bg-white rounded zoom"
                @click="checkRead(message.id)"
              >
                <b-card-text style="overflow: auto">
                  <!-- <div> -->
                  <div style="display: flex">
                    <div style="margin-top: auto; margin-bottom: auto">
                      <h5 style="font-weight: bold; margin: 0">
                        {{ message.movie.title }}
                      </h5>
                      <p style="font-size: 14px; color: gray; margin: 0">
                        {{ message.movie.original_title }}
                      </p>
                    </div>
                    <v-btn icon v-show="message.is_checked"
                      ><v-icon
                        color="green"
                        size="45"
                        style="
                          margin-left: 20px;
                          margin-top: auto;
                          margin-bottom: auto;
                        "
                        >mdi-check-circle-outline</v-icon
                      ></v-btn
                    >
                  </div>
                  <hr />
                  <p>{{ message.content }}</p>
                  <br />
                  <hr />
                  <p style="float: right">
                    <b>From.</b> {{ message.from_user.username }}
                  </p>
                  <!-- <v-btn
                      v-show="isUser"
                      dark
                      style="position: absolute; bottom: 15px; right: 15px"
                      @click.stop="messageDelete(message.id)"
                      >DELETE</v-btn
                    > -->
                  <!-- </div> -->
                </b-card-text>
              </b-card>
              <p style="margin-top: -15px; float: right; font-size: 13px">
                {{ new Date(message.send_at).toLocaleString() }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "MyPageMessage",
  computed: {
    allMessage: {
      get() {
        return this.$store.state.allMessage
      },
      set(newValue) {
        return newValue
      },
    },
    isNoneMessage() {
      if (this.allMessage.length === 0) {
        return true
      } else {
        return false
      }
    },
    unreadMessageCnt() {
      return this.$store.state.unreadMessage.length
    },
  },
  methods: {
    checkRead(message_id) {
      this.$store.dispatch("checkReed", message_id)
    },
  },
  created() {
    this.$store.dispatch("loadAllMessageList", this.$store.state.user.id)
  },
}
</script>

<style>
.clickedStyle {
  border: 5px solid black;
}
</style>
