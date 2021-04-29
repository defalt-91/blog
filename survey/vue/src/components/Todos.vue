<template>
  <div class="col-12 card ">
    <div class="bg-light">
      <h5 class="card-title text-primary p-1 shadow">My Site Surveys</h5>

      <div class="list-group " v-for="item in surveys" :key="item.id">
        <div
          class="list-group-item list-group-item-action flex-column  align-items-start"
        >
          <div class="d-flex w-100 justify-content-between">
            <h5 class="mb-1  fs-4 shadow text-wrap alert alert-info border close rounded">Survey id : {{ item.id }}</h5>
          </div>
        </div>
        <div
          class="list-group-item shadow list-group-item-action flex-column align-items-start "
        >
          <div class="d-flex w-100 justify-content-between alert alert-info shadow">
            <p class="mb-1 fs-1"><small class="alert fs-6 shadow py-2 border border-light border-5 ">Survey question</small>  : {{ item.question }}</p>
            <div  class="btn " @click="$emit('deletesurvey')">
              <i class="btn btn-lg fas fa-3x close fa-trash-alt"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>
<script>
import { mapGetters } from "vuex";
export default {
  name: "Todos",
  computed: {
    ...mapGetters({ surveys: "survaysList" })
  }
};
</script>
<style scoped></style>

