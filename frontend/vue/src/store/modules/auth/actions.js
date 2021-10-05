import api from "@/api";
import { SET_ACCESS_TOKEN, SET_USER } from "./mutation-types";

/**
 * Saves access token and retrieves user data from github
 * @param {Object} state
 * @param {String} accessToken
 */
async function login({ commit }, accessToken) {
  commit(SET_ACCESS_TOKEN, accessToken);

  const { data } = await api.authenticatedAxios.get(api.githubUserPath);

  commit(SET_USER, { name: data.name, avatarURL: data.avatar_url });
}

/**
 * Clears access token and user data
 * @param {Object} state
 */
function logout({ commit }) {
  commit(SET_ACCESS_TOKEN, null);
  commit(SET_USER, null);
}

export default {
  login,
  logout
};
