<template>
  <div class="alert-info col-12 card">
    <div class="bg-light">
      <h5 class="alert alert-info card-title p-1 shadow">My Site Surveys</h5>
      <div class="list-group" v-for="item in surveys" :key="item.id">
        <div
          class="alert alert-danger list-group-item shadow list-group-item-action flex-column align-items-center"
        >
          <div
            id="cardss"
            class="d-flex w-100 justify-content-between alert alert-info shadow"
          >
            <p
              class=""
              id="pfont"
              style="margin-top: auto; margin-bottom: auto"
            >
              <small
                class="text-start rounded-pill alert shadow py-3 border border-light border-2"
                >Survey :</small
              >
            </p>
            <h5
              style="height: 40px"
              class="mb-1 fs-6 shadow text-wrap alert alert-info border disabled close rounded-pill"
            >
              Survey id : {{ item.id }}
            </h5>
            <button
              class="border border-light border-1 rounded-pill btn btn-sm"
              @click="deletesurvey(item.id)"
            >
              <i
                style="color: dimgrey"
                class="fas fa-2x close fa-trash-alt"
              ></i>
            </button>
          </div>
          <div
            style="min-height: 50px"
            class="col-12 text-start fs-5 alert alert-success"
          >
            <div class="row">
              <div style="width:90%">{{ item.question }}</div>
              <button style="width:10%;height: 33px" class="btn btn-info badge badge-primary">Edit</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
import axios from "axios";
export default {
  name: "Todos",
  computed: {
    ...mapGetters({ surveys: "survaysList", Address: "Address" }),
  },
  methods: {
    ...mapActions(["getApisurvays"]),
    async deletesurvey(id) {
      try {
        const response = await axios
          .delete(this.Address + `${id}/`)
          .then(this.getApisurvays);
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>
<style scoped>
#cardss:hover {
  background-color: #5bc0de;
  color: #122b40;
  font-family: Roboto, "Bitstream Vera Sans Mono", Monaco, "Courier New",
    Courier, monospace;
}
#pfont {
  font-family: "Lucida Grande", "Lucida Sans Unicode", "Geneva", "Verdana",
    sans-serif;
  font-size: 100%;
  position: inherit;
  left: -10px;
}
</style>
