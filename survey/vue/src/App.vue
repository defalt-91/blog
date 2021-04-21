<template>
    <div class="container-fluid m-1">
        <div class="row justify-content-around my-3">
            <div class="d-grid d-flex gap-2 col-6">
                <LoadSurveys @getSurveys="getSurveys"/>
                <NewSurvey @addsurvey='getSurveys' />
            </div>
        </div>
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
                .get('http://127.0.0.1:8000/api/v2/survey')
                .then(res => { this.surveys = res.data });
        }
    }
};
</script>
<style lang="css" scoped>
</style>