function search(searchText, searchType) {
  if (searchType === "nameDescription") {
    this.nameDescriptionSearch(searchText);
  } else {
    this.tagSearch(searchText);
  }
}

function nameDescriptionSearch(searchText) {
  if (searchText) {
    const searchResult = this.nameDescriptionFuse.search(searchText);

    this.shownRepositories = searchResult.map(({ item }) => item);
  } else {
    this.shownRepositories = [...this.repositories];
  }
}

function tagSearch(searchText) {
  if (searchText) {
    const searchResult = this.tagFuse.search(searchText);

    this.shownRepositories = searchResult.map(({ item }) =>
      this.repositories.find(repo => repo.id === item.repoId)
    );
  } else {
    this.shownRepositories = [...this.repositories];
  }
}

export default {
  search,
  nameDescriptionSearch,
  tagSearch
};
