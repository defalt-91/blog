<template>
    <div class="alert"> <button class="btn btn-block btn-info" @click="getChoices">
            Choices
        </button>
        <legend class="border spinner-border my-2">{{choices.length}} Peoples have been answer to this question and <small class="alert alert-primary">{{yeses.length}}</small> said i was and <small class="alert alert-primary">{{nos.length}}</small> said that they're not </legend>
    </div>
    <div class="btn btn-sm m-1">Yes  
        <button class="d-inline-flex m-1 p-2 alert-danger">{{ yeses.length}}</button>
    </div>
        <button class="btn btn-sm m-1">{{ nos.length}}</button>
</template>
<script>
export default {

    name: 'Choices',

    data() {
        return {
            choices: [],
            yeses: [],
            nos: [],
        }
    },
    methods: {
        async getChoices() {
            const res = await fetch('https://arman-blog.herokuapp.com/api/v2/choice/')
            const data = await res.json()
            this.choices = data

            return data
        },
        yesFunc() {
            this.yeses = this.choices.filter((x) => {
                x.choicefield === 'yes'
                console.log(x.choicefield)
            })
        },
        noFunc() {
            this.nos = this.choices.filter((x) => {
                x.choicefield == !'yes'
            })
        }
    },
    created() {
        this.getChoices()
        this.yesFunc()
        this.noFunc()
    }
}
</script>
<style lang="css" scoped>
span {
    font-size: 1.5rem;
    font-weight: 600;
}
</style>