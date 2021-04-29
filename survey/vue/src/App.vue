<template>
    <div class="row">
        <div class="container border-start border-3 border-info ">
            <img id="imageAnimation" class="img-thumbnail" src="./assets/logo.png" :style="{'animation-play-state': animation,'animation-duration':animsec+'s'}" />
        </div>
    </div>
        <div class="row gy-5 px-4">
            <Button @stopAnime="stopAnimation" />
            <Todos />
        </div>
    <p>{{ ADDsurveyText }}</p>
</template>
<script>
import Button from "./components/Button";
import Todos from "./components/Todos";
import { mapGetters, mapActions } from "vuex";

export default {
    name: "App",
    components: { Button, Todos },
    data() {
        return {
            surVeys: [],
            animation: "running",
        };
    },
    methods: {
        ...mapActions(["getApisurvays"]),
        stopAnimation() {
            if (this.animation === "running") {
                this.animation = "paused";
            } else {
                this.animation = "running";
            }
        },
    },
    computed: { ...mapGetters(["ADDsurveyText", "animsec"]), },
    mounted() {
        this.getApisurvays();

    },
};
</script>
<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}

#imageAnimation {
    height: 100px;
    width: 100px;
    animation: mymove 6s infinite alternate-reverse;
    position: relative;
}

@keyframes mymove {
    from {
        left: -43%;
    }

    to {
        left: 43%;
    }
}
</style>