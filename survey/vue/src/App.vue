<template>
  <div class="container">
    <div class="row gx-3">
      <div class="container border-start border-3 border-info border-end">
        <img
          id="imageAnimation"
          alt="vue animation"
          class="card-img"
          src="./assets/logo.png"
          :style="{
            'animation-play-state': animation,
            'animation-duration': animsec + 's',
          }"
        />
      </div>
    </div>
    <div class="progress">
      <div
        class="progress-bar progress-bar-striped progress-bar-animated"
        role="progressbar"
        aria-valuenow="75"
        aria-valuemin="0"
        aria-valuemax="100"
        :style="{'width':Speedy+'%'}"
      ></div>
    </div>
    <div class="row gx-5">
      <Button @stopAnime="stopAnimation" />
    </div>
    <div class="row gy-2 gx-5">
      <Todos />
    </div>
    <p>{{ ADDsurveyText }}</p>
  </div>
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
  computed: { ...mapGetters(["ADDsurveyText", "animsec","Speedy"])},
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
