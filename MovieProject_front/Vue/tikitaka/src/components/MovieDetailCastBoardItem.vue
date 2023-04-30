<template>
    <div style="display: flex; align-items:center; margin:5px">
      <div class="circle-box">
        <img :src="profileURL" alt="" class="profile">
      </div>
      
      <span style="margin-left: 10px">{{ cast.name }}</span>
    </div>
  
</template>

<script>

export default {
  name: 'MovieDetailCastBoardItem',
  props: {
    cast: Object
  },
  data() {
    return {
    }
  },
  computed: {
    profileURL() {
      const path = this.cast.profile_path
      return `https://image.tmdb.org/t/p/original${path}`
    }
  }


}
</script>

<style>

.circle-box {
    width: 30px;
    height: 30px; 
    border-radius: 70%;
    overflow: hidden;
}
.profile {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

</style>