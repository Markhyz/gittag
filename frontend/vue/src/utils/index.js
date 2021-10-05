import router from "@/router";
import store from "@/store";

/**
 * Stores login information
 * @param {String} accessToken
 */
async function login(accessToken) {
  await store.dispatch("auth/login", accessToken);
  router.replace("/");
}

/**
 * Clears login information
 */
function logout() {
  store.dispatch("auth/logout");
  router.push({ name: "Login" });
}

export { login, logout };
