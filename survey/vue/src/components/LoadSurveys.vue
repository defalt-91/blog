<template><div class="col-6">
    <button class="btn btn-sm btn-outline-info" @click='$emit("getSurveys")'>Load surveys</button></div>
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