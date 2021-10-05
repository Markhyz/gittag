import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/repositories"
  },
  {
    path: "/repositories",
    name: "Repositories",
    component: () =>
      import(/* webpackChunkName: "repositories" */ "../views/repositories"),
    meta: {
      auth: true
    }
  },
  {
    path: "/login",
    name: "Login",
    component: () => import(/* webpackChunkName: "login" */ "../views/login"),
    meta: {
      auth: false
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

// For routes that need authentication, checks if the user is logged in
router.beforeEach((to, from, next) => {
  if (to.meta.auth && !store.getters["auth/isAuthenticated"]) {
    next({ name: "Login" });
  } else {
    next();
  }
});

export default router;
