<template>
    <button class="btn btn-sm m-1 d-inline">Yes {{ yeses.length}}</button>
    <button class="btn btn-sm d-inline">No  {{ nos.length}}</button>
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
            this.yeses = this.choices.filter((x) => { x.choicefield === 'yes' })
        },
        noFunc() {
            this.nos = this.choices.filter((x) => { x.choicefield == !'yes' })
        }
    },
    created() {
        this.getChoices()
        this.yesFunc()
        this.noFunc()
    },
    
}
</script>
<style lang="css" scoped>
span {
    font-size: 1.5rem;
    font-weight: 600;
}
</style>