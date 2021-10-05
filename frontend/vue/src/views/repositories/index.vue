<template>
  <div class="container h-100 d-flex flex-column">
    <div class="mb-3 text-white row">
      <div class="col-sm">
        <label for="search-input" class="mt-3">Search:</label>
        <b-form-input id="search-input" v-model="searchText" />
      </div>
      <div class="col-sm-auto d-flex flex-column">
        <label for="search-type" class="mt-3">Search on:</label>
        <div class="flex-grow-1 d-flex align-items-center">
          <b-form-radio-group id="search-type" v-model="searchType">
            <b-form-radio value="nameDescription">
              Name and description
            </b-form-radio>
            <b-form-radio value="tags"> Tags </b-form-radio>
          </b-form-radio-group>
        </div>
      </div>
    </div>
    <div
      v-if="showLoading"
      class="flex-grow-1 d-flex align-items-center justify-content-center"
    >
      <div class="spinner-border text-light" />
    </div>
    <div
      v-else-if="shownRepositories.length === 0"
      class="flex-grow-1 d-flex align-items-center justify-content-center"
    >
      <h1 class="text-light">
        No starred repositories found :(
      </h1>
    </div>
    <div v-else class="flex-grow-1 overflow-auto">
      <repository-card
        v-for="repo in shownRepositories"
        :key="repo.id"
        :name="repo.name"
        :url="repo.url"
        :tags="getTagNames(tags[repo.id])"
        :loading="tags[repo.id].loading"
        @tag-change="onTagChange(repo.id, $event)"
      >
        {{ repo.description }}
      </repository-card>
    </div>
  </div>
</template>

<script>
/**
 * Repositories view
 */

import Fuse from "fuse.js";

import api from "@/api";

import RepositoryCard from "@/components/RepositoryCard";

import loadMethods from "./methods/load";
import searchMethods from "./methods/search";

export default {
  name: "RepositoriesView",
  components: {
    RepositoryCard
  },
  data() {
    return {
      repositories: [],
      shownRepositories: [],
      tags: null,
      nameDescriptionFuse: null,
      tagFuse: null,
      searchText: null,
      searchType: "nameDescription",
      showLoading: null
    };
  },
  watch: {
    searchText(text) {
      this.search(text, this.searchType);
    },
    searchType(type) {
      this.search(this.searchText, type);
    }
  },
  created() {
    this.load();
  },
  methods: {
    ...loadMethods,
    ...searchMethods,
    getTagNames(tag) {
      return tag.values.map(({ name }) => name);
    },
    setNameDescriptionFuse() {
      this.nameDescriptionFuse = new Fuse(this.repositories, {
        keys: ["name", "description"]
      });
    },
    setTagFuse() {
      const searchableTags = Object.keys(this.tags).map(key => ({
        repoId: parseInt(key),
        tags: this.getTagNames(this.tags[key])
      }));

      this.tagFuse = new Fuse(searchableTags, { keys: ["tags"] });
    },
    async addTag(repoId, currentTags, oldTags) {
      const newTagName = currentTags.filter(tagName => {
        const isOld = oldTags.find(oldTag => oldTag.name === tagName);

        return !isOld;
      })[0];

      const { data } = await api.authenticatedAxios.post(api.tagPath(), {
        repository_id: repoId,
        name: newTagName
      });

      this.tags[repoId].values.push(data);
      this.$set(this.tags, repoId, this.tags[repoId]);
    },
    async removeTag(repoId, currentTags, oldTags) {
      const removedTag = oldTags.filter(oldTag => {
        const tagExists = currentTags.find(tagName => oldTag.name === tagName);

        return !tagExists;
      })[0];

      await api.authenticatedAxios.delete(api.tagPath(removedTag.id));

      this.tags[repoId].values = oldTags.filter(
        tag => tag.name != removedTag.name
      );
      this.$set(this.tags, repoId, this.tags[repoId]);
    },
    async onTagChange(repoId, currentTags) {
      const oldTags = this.tags[repoId].values;
      if (currentTags.length > oldTags.length) {
        await this.addTag(repoId, currentTags, oldTags);
      } else {
        await this.removeTag(repoId, currentTags, oldTags);
      }

      this.setTagFuse();
      this.search(this.searchText, this.searchType);
    }
  }
};
</script>
