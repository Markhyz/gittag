import { SET_ACCESS_TOKEN, SET_USER } from "./mutation-types";

export default {
  [SET_ACCESS_TOKEN](state, accessToken) {
    state.accessToken = accessToken;
  },
  [SET_USER](state, user) {
    state.user = user;
  }
};
