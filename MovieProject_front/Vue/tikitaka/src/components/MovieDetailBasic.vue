<template>
  <div>
    <div class="sentence">
      <b>감독</b> &nbsp;
      <span
        style="
          font-family: 'ONE-Mobile-Regular';
          font-weight: bold;
          font-size: 15px;
        "
      >
        {{ movie.director.name }}
      </span>
    </div>
    <div class="sentence">
      <b>장르</b> &nbsp;
      <span
        v-for="(genre, idx) in movie.genres"
        :key="idx"
        style="
          font-family: 'ONE-Mobile-Regular';
          font-weight: bold;
          font-size: 15px;
        "
      >
        <span>{{ genre.name }} &nbsp;</span>
      </span>
    </div>
    <div class="sentence">
      <b>개봉</b> &nbsp;
      <span
        style="
          font-family: 'ONE-Mobile-Regular';
          font-weight: bold;
          font-size: 15px;
        "
      >
        {{ movie.release_date }}
      </span>
    </div>
    <div class="sentence">
      <b>정보</b> &nbsp;
      <span
        style="
          font-family: 'ONE-Mobile-Regular';
          font-weight: bold;
          font-size: 15px;
        "
        >{{ movie.runtime }}분&nbsp;|&nbsp;</span
      >
      <span v-for="(country, idx) in movie.countries" :key="idx">
        <img
          :src="`https://flagpedia.net/data/flags/w702/${country.toLowerCase()}.png`"
          alt=""
          style="width: 24px; height: 16px; margin-right: 3px"
        />
      </span>
    </div>
    <div class="sentence">
      <span
        v-for="(provider, idx) in movie.watch_providers"
        :key="idx"
        style="display: inline-block; vertical-align: middle"
      >
        <img
          :src="`https://image.tmdb.org/t/p/original${provider.logo_path}`"
          alt=""
          style="width: 16px; height: 16px; margin-right: 3px"
        />
        <span style="font-size: 12px">{{ provider.name }}&nbsp;</span>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieDetailBasic",
  props: {
    movie: Object,
  },
}
</script>

<style>
.sentence {
  height: 30px;
  margin: 5px;
}
</style>
