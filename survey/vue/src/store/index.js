import { createStore } from "vuex";
import axios from "axios";
export default createStore({
  state: {
    surveys: [],
    address: "https://arman-blog.herokuapp.com/api/v2/survey/",
    surveyText: "",
    animsec:1,

  },
  getters: {
    survaysList: (state) => {
      return state.surveys;
    },
    ADDsurveyText: (state) => {
      return state.surveyText;
    },
    animsec:(state) => {
      return state.animsec
}
  },
  mutations: {
    ADD_SURVEYS(state, apiData) {
      state.surveys = apiData;
    },
    updateMessage(state, value) {
      state.surveyText = value;
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
    addSurvey: async function({commit},data){
      try {
        const response = await axios.post(this.state.address,{
          question:data
        }).then(this.dispatch('getApisurvays'))
      }catch(error){
        console.log(error)
      }
},
    addAPISurvey: function () {},
  },
});
