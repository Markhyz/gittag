import api from "@/api";

async function load() {
  this.showLoading = true;

  await this.loadRepositories();
  await this.loadTags();

  this.setNameDescriptionFuse();
  this.setTagFuse();

  this.showLoading = false;
}

async function loadRepositories() {
  const { data: repositories } = await api.authenticatedAxios.get(
    api.githubUserStarredPath
  );

  this.repositories = repositories;
  this.shownRepositories = [...this.repositories];
}

async function loadTags() {
  this.tags = this.repositories.reduce((tags, repo) => {
    tags[repo.id] = {
      values: [],
      loading: true
    };

    return tags;
  }, {});

  const { data: tags } = await api.authenticatedAxios.get(api.tagPath());

  tags.forEach(tag => {
    if (this.tags[tag.repository_id]) {
      // Inserts tag if repository is starred (unstarred repositories tags are not removed from database)
      this.tags[tag.repository_id].values.push(tag);
    }
  });

  this.tags = Object.keys(this.tags).reduce((tags, key) => {
    tags[key] = { ...this.tags[key], loading: false };

    return tags;
  }, {});
}

export default {
  load,
  loadRepositories,
  loadTags
};
