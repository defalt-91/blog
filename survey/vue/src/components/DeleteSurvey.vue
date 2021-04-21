<template>
    <div class="col-3 btn btn-lg" @click="$emit('deletesurvey')">
        <i style="color:#ffb330" class="fas fa-backspace"></i>
    </div>
</template>
<script>
export default {name: 'DeleteSurvey'}
</script>
<style lang="css" scoped>
</style>