<template>
    <button class="btn btn-outline-info" @click='$emit("getSurveys")'>Load surveys</button>
</template>

<script>
export default {

  name: 'LoadSurveys',

  data () {
    return {

    }
  }
}
</script>

<style lang="css" scoped>
</style>