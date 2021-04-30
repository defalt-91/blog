import { createStore } from "vuex";
import axios from "axios";
export default createStore({
  state: {
    surveys: [],
    address: "https://arman-blog.herokuapp.com/api/v2/survey/",
    surveyText: "",
    animsec: 5,
    speed: 50,
  },
  getters: {
    survaysList: (state) => {
      return state.surveys;
    },
    ADDsurveyText: (state) => {
      return state.surveyText;
    },
    animsec: (state) => {
      return state.animsec;
    },
    Speedy: (state) => state.speed,
    Address: (state) => {
      return state.address;
    },
  },
  mutations: {
    ADD_SURVEYS(state, apiData) {
      state.surveys = apiData;
    },
    updateMessage(state, value) {
      state.surveyText = value;
    },
    SPEED_CHANGE(state, value) {
      if (state.speed < 100) {
        state.speed += value;
      } else {
        if (value < 0 && state.speed >= 5) {
          state.speed -= 5;
        }
      }
    },
  },
  actions: {
    getApisurvays: async function ({ commit }) {
      try {
        const response = await axios.get(this.state.address);
        const apiData = response.data;
        commit("ADD_SURVEYS", apiData);
      } catch (e) {
        console.log(e);
      }
    },
    addSurvey: async function ({ commit }, data) {
      try {
        const response = await axios.post(this.state.address, {
          question: data,
        });
      } catch (error) {
        console.log(error);
      }
      this.dispatch("getApisurvays");
    },
    addAPISurvey: () => {},
    SpeedChange({ commit }, value) {
      this.commit("SPEED_CHANGE", value);
    },
  },
});
