<template>
    <div class="row">
        <LoadSurveys @getSurveys="getSurveys" />
        <NewSurvey @addsurvey='getSurveys' />
    </div>
    <div id="survey" class="p-1">
        <Survey :surveys="surveys" @deleteCompleted="getSurveys" />
    </div>
</template>
<script>
import LoadSurveys from './components/LoadSurveys'
import axios from 'axios';
import Survey from './components/Survey';
import NewSurvey from './components/NewSurvey';
export default {
    name: 'App',
    components: {
        Survey,
        NewSurvey,
        LoadSurveys,
    },

    data() {
        return {
            surveys: {}
        };
    },
    created() {
        this.getSurveys()
    },
    methods: {
        getSurveys() {
            axios
                .get('https://arman-blog.herokuapp.com/api/v2/survey')
                .then(res => { this.surveys = res.data });
        }
    }
};
</script>
<style lang="css" scoped>

</style>