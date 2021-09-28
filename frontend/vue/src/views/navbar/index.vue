<template>
  <b-navbar type="dark" class="gt-navbar">
    <router-link to="/">
      <b-navbar-brand>
        GitTag
      </b-navbar-brand>
    </router-link>
    <b-navbar-nav class="ml-auto" v-if="userName">
      <b-nav-item-dropdown right no-caret>
        <template #button-content>
          <b-avatar :src="userAvatarURL" size="sm" />
        </template>
        <b-dropdown-text text-class="font-weight-bold" class="text-nowrap">
          {{ userName }}
        </b-dropdown-text>
        <b-dropdown-divider />
        <b-dropdown-item @click="logout">Sign Out</b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
import { mapGetters } from "vuex";

import { logout } from "@/utils";

export default {
  name: "NavbarView",
  computed: {
    ...mapGetters("auth", ["getUser"]),
    userName() {
      return this.getUser?.name;
    },
    userAvatarURL() {
      return this.getUser?.avatarURL;
    }
  },
  methods: {
    logout
  }
};
</script>

<style lang="scss" scoped>
.gt-navbar {
  background: #323441;
}
</style>
