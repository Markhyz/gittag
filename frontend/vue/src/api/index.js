import axios from "axios";

import store from "@/store";
import { logout } from "@/utils";

const appOrigin = global.window.location.origin;
const apiURL = process.env.VUE_APP_API_URL || `${appOrigin}/api`;

const githubAuthURL = `https://github.com/login/oauth/authorize?client_id=${process.env.VUE_APP_GITHUB_OAUTH_CLIENT_ID}&redirect_uri=${appOrigin}/login`;

const authPath = "/auth";
const tagPath = id => (id ? `/tags/${id}/` : "/tags/");
const githubUserPath = "/github/user";
const githubUserStarredPath = "/github/user/starred";

const authenticatedAxios = axios.create({
  baseURL: apiURL
});

authenticatedAxios.interceptors.request.use(
  config => {
    const accessToken = store.getters["auth/getAccessToken"];
    if (accessToken) {
      config.headers["Authorization"] = accessToken;
    }

    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

authenticatedAxios.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error?.response?.status === 403) {
      logout();
    }
    return Promise.reject(error);
  }
);

export default {
  githubAuthURL,
  authPath,
  tagPath,
  githubUserPath,
  githubUserStarredPath,
  authenticatedAxios
};
