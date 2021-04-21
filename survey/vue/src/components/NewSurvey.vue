<template>
    <button type="button" class="btn btn-outline-info " data-bs-toggle="modal" data-bs-target="#exampleModal">
        Add Survey
    </button>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Write your survey question</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body" >
                    <input type="text" name="question" v-model='question'>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" @click="addsurvey" data-bs-dismiss="modal" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {

    name: 'NewSurvey',

    data() {
        return {
            question: ''
        }
    },
    methods: {
        Newsurvey() {
            axios({
                method: 'post',
                url: 'http://127.0.0.1:8000/api/v2/survey/',
                data: {
                    question: this.question
                }
            }).then((response) => {
                console.log(response);
            }, (error) => {
                console.log(error);
            });
        },
        addsurvey(){
            this.Newsurvey()
            this.question=''
            this.$emit('addsurvey')
        }
    }
}
</script>
<style lang="css" scoped>
</style>