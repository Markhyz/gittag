<template>
  <div class="d-flex flex-column vh-100">
    <navbar-view />
    <main class="gt-main-content flex-grow-1 overflow-hidden">
      <router-view />
    </main>
  </div>
</template>

<script>
import NavbarView from "@/views/navbar";

export default {
  name: "Application",
  components: {
    NavbarView
  }
};
</script>

<style lang="scss" scoped>
.gt-main-content {
  background: #404854;
}
</style>
