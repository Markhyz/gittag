import router from "@/router";
import store from "@/store";

async function login(accessToken) {
  await store.dispatch("auth/login", accessToken);
  router.replace("/");
}

function logout() {
  store.dispatch("auth/logout");
  router.push({ name: "Login" });
}

export { login, logout };
