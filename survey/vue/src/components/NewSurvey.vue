<template>
    <div class="col-6">
    <button type="button" class="btn btn-sm btn-outline-info" data-toggle="modal" data-target="#exampleModal">
        Add Survey
    </button></div>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Write your survey question</h5> <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span> </button>
                </div>
                <div class="modal-body"> <input type="text" name="question" v-model='question'>
                    <h1>{{question}}</h1>
                </div>
                <div class="modal-footer"> <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button> <button type="button" @click="addsurvey" class="btn btn-primary">Save
                        changes</button> </div>
            </div>
        </div>
    </div>
</template>
<script>
import
axios from 'axios';
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
                method: 'POST',
                url: 'https://arman-blog.herokuapp.com/api/v2/survey/',
                data: {
                    question: 'asdasd',
                }
            })
        },
        addsurvey() {
            this.Newsurvey()
            this.question = ''
            this.$emit('addsurvey')
        }
    }
}
</script>
<style lang="css" scoped>
</style>