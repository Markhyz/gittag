import getters from "./getters";
import mutations from "./mutations";
import actions from "./actions";

export default {
  namespaced: true,
  state: {
    accessToken: null,
    user: {
      name: null,
      avatarURL: null
    }
  },
  getters,
  mutations,
  actions
};
