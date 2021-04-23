<template>
    <div v-for="item in surveys" :key="item.id" class="col-12 mb-1" id="survey">
        <div class="row">
            <div class="col-11">
                <p class="m-1">{{item.question}}</p><br/>
            </div>
            <div class="col-1 btn btn-sm" @click="deleteSurvey(item.id)">
                <i style="color:#ffb330" class="fas fa-backspace"></i>
            </div>
            <button class="btn btn-sm btn-info d-inline" @click="ShowAnswers">Answers</button>
            <div v-show="ChoiceClick">
                <Choices />
            </div>
        </div>
    </div>
</template>
<script>
import Choices from './Choices'
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
    components: {
        Choices
    },
    methods: {
        deleteSurvey(id) {
            axios.delete(`https://arman-blog.herokuapp.com/api/v2/survey/${id}/`)
            this.$emit("deleteCompleted")
        },
        ShowAnswers() {
            this.ChoiceClick = !this.ChoiceClick
        }
    },
    data() {
        return {
            ChoiceClick: false
        };
    }
};
</script>
<style lang="css" scoped>
#survey {
    border-left: 6px solid lightblue;
}
</style>