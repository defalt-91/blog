<template>
  <div
    class="col-sm-10 mx-auto btn-group-sm my-2 border-bottom border-end border-start border-4 border-info pt-2 pb-2"
  >
    <div class="row mx-auto">
      <button
          style="max-width: 33%"
        class="rounded-pill col-sm-4 btn btn-outline-info text-dark shadow-dark border-end border-5"
        @click="fastAnim"
      >
        <strong
          class="rounded-pill badge border-1 border border-light bg-info text-wrap fs-5"
          >Slower
        </strong>
      </button>
      <button
        class="col-sm-4 rounded-pill btn btn-outline-info text-dark shadow border-end border-5 border-start border-5"
        type="button"
        @click="$emit('stopAnime')"
        style="max-width: 33%"
      >
        <strong
          class="border-1 rounded-pill border border-light badge bg-info text-wrap fs-5"
          >Play | Pause</strong
        >
      </button>
      <button
        class="rounded-pill col-sm-4 btn btn-outline-info text-dark shadow border-start border-5"
        @click="slowAnim"
        style="max-width: 33%"
      >
        <strong
          class="border-1 border border-light badge rounded-pill bg-info text-wrap fs-5"
          >Faster
        </strong>
      </button>
    </div>
  </div>

  <div class="col-12 btn-group d-block pt-5">
    <button
      class="btn btn-warning px-4 mx-4"
      @click="getApisurvays"
      type="button"
    >
      Load From API
    </button>
    <button
      class="btn btn-primary"
      data-bs-target="#exampleModal"
      data-bs-toggle="modal"
      type="button"
    >
      Add Survey
    </button>
  </div>
  <div
    class="col-12 modal fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content bg-light alert">
        <div class="modal-header">
          <h5 class="modal-title alert alert-success" id="exampleModalLabel">
            HTTP Put Request to API
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="input-group">
            <span class="input-group-text alert alert-success">Survey :</span>
            <textarea
              v-model="AddsurveyText"
              class="form-control mx-1 border border-3"
              aria-label="With textarea"
            ></textarea>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button
            type="button"
            class="btn btn-primary p-2"
            data-bs-dismiss="modal"
            @click="konsole"
          >
            Add
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions } from "vuex";
export default {
  name: "Button",
  emits: ["stopAnime"],
  computed: {
    AddsurveyText: {
      get() {
        return this.$store.getters.ADDsurveyText;
      },
      set(value) {
        this.$store.commit("updateMessage", value);
      },
    },
  },
  methods: {
    ...mapActions(["getApisurvays", "addSurvey", "SpeedChange"]),
    konsole() {
      this.addSurvey(this.AddsurveyText);
      this.AddsurveyText = "";
    },
    slowAnim() {
      if (this.$store.state.animsec > 0.5) {
        this.$store.state.animsec -= 0.5;
        this.SpeedChange(5);
        console.log(this.$store.state.speed)
      }
    },
    fastAnim() {
      if (this.$store.state.animsec <= 9.5) {
        this.$store.state.animsec += 0.5;
        this.SpeedChange(-5);console.log(this.$store.state.speed)
      }
    },
  },
};
</script>
<style scoped></style>
