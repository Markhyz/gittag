import Vue from "vue";
import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

import { shallowMount } from "@vue/test-utils";
import RepositoryCard from "@/components/RepositoryCard";

describe("Repository card", () => {
  const repositoryName = "Test";
  const repositoryURL = "www.example.com";
  const repositoryTags = ["test-1", "test-2", "test-3"];
  const repositoryDescription = "This is a test description";

  const wrapper = shallowMount(RepositoryCard, {
    propsData: {
      name: repositoryName,
      url: repositoryURL,
      tags: repositoryTags
    },
    slots: {
      default: repositoryDescription
    }
  });

  it("renders title correctly", () => {
    expect(wrapper.get(".gt-repository-card__title").text()).toBe(
      repositoryName
    );
  });

  it("renders url correctly", () => {
    expect(wrapper.get(".gt-repository-card__header").attributes().href).toBe(
      repositoryURL
    );
  });

  it("renders description correctly", () => {
    expect(wrapper.get(".gt-repository-card__body").text()).toBe(
      repositoryDescription
    );
  });
});
