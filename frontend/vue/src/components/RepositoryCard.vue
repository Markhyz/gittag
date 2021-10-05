<template>
  <b-overlay :show="loading">
    <b-card class="gt-repository-card mb-5">
      <a
        :href="url"
        class="gt-repository-card__header text-decoration-none"
        target="_blank"
      >
        <b-card-title>
          <span class="gt-repository-card__title">
            {{ name }}
          </span>
        </b-card-title>
      </a>
      <div class="gt-repository-card__body">
        <!-- @slot Repository description -->
        <slot />
      </div>
      <div class="gt-repository-card__footer mt-4">
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
/**
 * Repository card
 */

export default {
  name: "RepositoryCard",
  props: {
    /**
     * Display loading overlay
     */
    loading: Boolean,
    /**
     * Repository name
     */
    name: String,
    /**
     * Repository tags
     */
    tags: Array,
    /**
     * Repository URL
     */
    url: String
  }
};
</script>
