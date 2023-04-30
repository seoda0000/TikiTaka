<template>
  <div style="margin-right: 20px">
    <FullCalendar
      :options="calendarOptions"
      style="font-family: 'ONE-Mobile-Regular'"
    />

    <!-- 캘린더 포스터 등록 모달 -->
    <b-modal hide-footer hide-header-close size="medi" id="calendarModal">
      <template #modal-header>
        <h2 class="logoText">CUSTOMIZE YOUR OWN CALENDAR</h2>
      </template>

      <feed-create-modal
        :isCalendarRequest="isCalendarRequest"
        @select-image-for-calendar="selectImageForCalendar"
      />

      <v-btn
        id="font-face"
        dark
        height="45"
        @click="addCalendar"
        style="float: right; margin-top: 20px"
        >POST</v-btn
      >
    </b-modal>
  </div>
</template>

<script>
import FullCalendar from "@fullcalendar/vue"
import dayGridPlugin from "@fullcalendar/daygrid"
import interactionPlugin from "@fullcalendar/interaction"
import FeedCreateModal from "./FeedCreateModal.vue"

export default {
  name: "MyPageCalendar",
  components: {
    FullCalendar,
    FeedCreateModal,
  },
  props: {
    calendarItems: Array,
  },
  data() {
    return {
      isCalendarRequest: true,
      movie_title: null,
      movie_id: null,
      backdrop_id: null,
      select_img: null,
      selectedInfo: null,
      calendarOptions: {
        plugins: [dayGridPlugin, interactionPlugin],
        initialView: "dayGridMonth",
        editable: false,
        selectable: true,
        // selectMirror: true,
        dayMaxEvents: true,
        headerToolbar: {
          left: "title",
          right: "prev next today",
          center: "",
        },
        select: this.handleDateSelect,
        eventClick: this.handleEventClick,
        // eventsSet: this.handleEvents,
        eventContent: this.eventContent,
        // eventColor: "black",
        height: "1200px",
        // expandRows: true,
        events: this.calendarItems,
      },
    }
  },
  watch: {
    calendarItems() {
      this.calendarOptions.events = this.calendarItems
    },
  },
  computed: {
    // 현재 로그인한 유저
    user() {
      return this.$store.state.user
    },
    tempUser() {
      return this.$store.state.tempUser
    },
    // 현재 유저와 피드 작성 유저가 같은지 판단 -> 같을 때만 삭제,수정 가능
    isUser() {
      if (this.user.id === this.tempUser.id) {
        return true
      }
      return false
    },
  },
  methods: {
    // handleDateClick: function (arg) {
    //   alert("date click! " + arg.dateStr)
    // },

    // 빈 날짜 클릭시 캘린더 추가 모달 오픈 (유저 본인만 가능)
    handleDateSelect(selectInfo) {
      if (this.isUser) {
        this.$store.commit("INITIALIZE_BACKDROP_LIST")
        this.$bvModal.show("calendarModal")
        this.selectedInfo = selectInfo
      }
    },

    // 선택된 이미지 정보 저장
    selectImageForCalendar(payload) {
      this.movie_id = payload.movie_id
      this.backdrop_id = payload.backdrop_id
      this.select_img = payload.img_url
      this.movie_title = payload.title
    },

    // 달력에 포스터 생성
    addCalendar() {
      // console.log(this.selectedInfo)
      // let image_url = this.select_img
      // let calendarApi = this.selectedInfo.view.calendar
      // calendarApi.unselect()

      // if (image_url) {
      //   calendarApi.addEvent({
      //     title: this.movie_title,
      //     image_url: image_url,
      //     start: this.selectedInfo.startStr,
      //   })
      // }

      // DB에 추가하기 위한 함수 호출
      const payload = {
        movie_id: this.movie_id,
        backdrop_id: this.backdrop_id,
        start: this.selectedInfo.startStr,
      }
      this.$store.dispatch("addCalendar", payload)

      // 모달 닫기
      this.$bvModal.hide("calendarModal")
    },

    // 생성된 일정 다시 누르면 일정 삭제
    handleEventClick(clickInfo) {
      // 본인만 삭제 가능
      if (this.isUser) {
        // 삭제 전 경고창 띄우기
        if (
          confirm(
            `해당 날짜의 ${clickInfo.event.title} 포스터를 삭제하시겠습니까?`
          )
        ) {
          clickInfo.event.remove()
          this.$store.dispatch("deleteCalendar", clickInfo.event.startStr)
        } else {
          console.log(clickInfo)
        }
      }
      // 본인이 아니라면 영화 상세페이지로 이동
      else {
        console.log("가고자하는 영화 제목", clickInfo.event.title)
        this.$store.dispatch("getMovieIdByTitle", clickInfo.event.title)
        // console.log("남의 달력", movie_id_for_detail)
        // this.$store.dispatch("getMovieById", this.movie_id)
      }
    },
    // handleEvents(events) {
    //   this.currentEvents = events
    // },
    // 일정 출력형식 (이미지 출력)
    eventContent(arg) {
      let arrayOfDomNodes = []
      let titleEvent = document.createElement("div")
      if (arg.event._def.title) {
        titleEvent.innerHTML = arg.event._def.title
        // titleEvent.width = "100%"
        // titleEvent.style.wordBreak = "break-all"
        titleEvent.style.backgroundColor = "white"
        titleEvent.style.color = "black"
        titleEvent.style.fontSize = "16px"
        titleEvent.style.fontWeight = "bold"
      }
      // image event
      let imgEventWrap = document.createElement("div")
      if (arg.event.extendedProps.image_url) {
        let imgEvent =
          '<img src="' +
          arg.event.extendedProps.image_url +
          '"  style="width:100%">'
        imgEventWrap.style.width = "100%"
        imgEventWrap.classList = "fc-event-img"
        imgEventWrap.innerHTML = imgEvent
      }
      arg.borderColor = "white"
      arrayOfDomNodes = [imgEventWrap, titleEvent]

      return { domNodes: arrayOfDomNodes }
    },
  },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Pacifico&family=Titan+One&display=swap");

/* #font-face {
  font-family: "S-CoreDream-3Light";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
} */

/* 현재 날짜 */
.fc-day-today {
  background: white !important;
  border: none !important;
}

/* 날짜 형식 */
.fc .fc-daygrid-day-number {
  color: black !important;
  text-decoration: none;
}

/* 요일 형식 */
.fc .fc-col-header-cell-cushion {
  color: black !important;
  text-decoration: none;
  font-weight: bolder;
}

/* 달력 제목 형식 */
.fc .fc-toolbar-title {
  font-family: "Titan One", cursive;
}

/* 글자 짤리는 문제 해결 */
.fc-daygrid-event {
  white-space: normal;
}
</style>
