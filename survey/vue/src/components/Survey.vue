<template>
    <div class="row">
        <div v-for="item in surveys" :key="item.id" class="row">
            <div class="col-9">
                <h1 class="m-1">{{item.question}}</h1>
            </div>
            <div class="col-3 btn btn-lg" @click="deleteSurvey(item.id)">
                <i style="color:#ffb330" class="fas fa-backspace"></i>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'Survey',
    props: {
        surveys: {
            type: Object,
            required: true,
            default: null,
        },
    },
    methods: {
        deleteSurvey(id) {
            axios.delete(`http://127.0.0.1:8000/api/v2/survey/${id}/`)
            this.$emit("deleteCompleted")
        }
    },
};
</script>
<style lang="css" scoped>
</style>