<template>
  <span>
    <v-chip color="yellow" text-color="black" style="margin: 5px 3px" small>
      {{ genre.name }}
    </v-chip>
  </span>
</template>

<script>
export default {
  name: "CommunityProfileGenre",
  props: {
    genre: Object,
  },
}
</script>

<style></style>
