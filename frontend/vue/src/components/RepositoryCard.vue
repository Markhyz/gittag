<template>
  <b-overlay :show="loading">
    <b-card class="mb-5">
      <a :href="url" class="text-decoration-none" target="_blank">
        <b-card-title>
          {{ name }}
        </b-card-title>
      </a>
      <slot />
      <div class="mt-4">
        <label :for="`${name}-tags`">Tags</label>
        <b-form-tags
          :input-id="`${name}-tags`"
          :value="tags"
          @input="$emit('tag-change', $event)"
        />
      </div>
    </b-card>
  </b-overlay>
</template>

<script>
export default {
  name: "RepositoryCard",
  props: {
    loading: Boolean,
    name: String,
    tags: Array,
    url: String
  }
};
</script>
