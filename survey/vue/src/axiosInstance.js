import { mapGetters } from "vuex";
import axios from "axios";
const url = mapGetters(["Address"]);

export default {name:"DELETEFUNC",
  deleteSurvey: (id) => {
    axios.delete(url + id), console.log(id);
    console.log(url)
  },
};
