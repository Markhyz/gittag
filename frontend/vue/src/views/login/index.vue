<template>
  <div
    class="gt-login container h-100 d-flex align-items-center justify-content-center"
  >
    <b-overlay :show="showLoading">
      <b-card class="gt-login-card" align="center">
        <div
          class="gt-login-card__content m-3 h-100 d-flex flex-column justify-content-between"
        >
          <div class="gt-login-card__header">
            <b-card-title title-tag="h1">
              Welcome
            </b-card-title>
            <b-card-sub-title sub-title-tag="h5">
              GitHub authentication is necessary to continue
            </b-card-sub-title>
          </div>
          <div class="gt-login-card__button">
            <b-button variant="dark" :href="githubAuthURL">
              <b-img :src="GitHubMark" class="mr-2" />
              Login with GitHub
            </b-button>
          </div>
        </div>
      </b-card>
    </b-overlay>
  </div>
</template>

<script>
import GitHubMark from "@/assets/GitHub-Mark-Light-32px.png";

import api from "@/api";
import { login } from "@/utils";

export default {
  name: "LoginView",
  data() {
    return {
      GitHubMark,
      githubAuthURL: api.githubAuthURL,
      showLoading: null
    };
  },
  created() {
    if (this.$route.query.code) {
      this.showLoading = true;
      api.authenticatedAxios
        .post(api.authPath, { code: this.$route.query.code })
        .then(({ data }) => login(data.access_token))
        .finally(() => {
          this.showLoading = false;
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.gt-login {
  .gt-login-card {
    .gt-login-card__content {
      .gt-login-card__button {
        margin-top: 7rem;
      }
    }
  }
}
</style>
