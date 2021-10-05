import Vue from "vue";
import Vuex from "vuex";

import authModule from "./modules/auth";

import VuexPersistence from "vuex-persist";

// Saves "auth" store in localStorage to persist browser refresh
const vuexLocalstorage = new VuexPersistence({
  storage: window.localStorage,
  modules: ["auth"]
});

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth: authModule
  },
  plugins: [vuexLocalstorage.plugin]
});
