import api from "@/api";
import { SET_ACCESS_TOKEN, SET_USER } from "./mutation-types";

async function login({ commit }, accessToken) {
  commit(SET_ACCESS_TOKEN, accessToken);

  const { data } = await api.authenticatedAxios.get(api.githubUserPath);

  commit(SET_USER, { name: data.name, avatarURL: data.avatar_url });
}

function logout({ commit }) {
  commit(SET_ACCESS_TOKEN, null);
  commit(SET_USER, null);
}

export default {
  login,
  logout
};
