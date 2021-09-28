function getAccessToken(state) {
  return state.accessToken;
}

function getUser(state) {
  return state.user;
}

function isAuthenticated(state, getters) {
  return !!getters.getAccessToken;
}

export default {
  getAccessToken,
  getUser,
  isAuthenticated
};
