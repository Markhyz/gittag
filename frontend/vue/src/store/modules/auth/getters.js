/**
 * Retrieve access token
 * @param {Object} state
 * @return {String}
 */
function getAccessToken(state) {
  return state.accessToken;
}

/**
 * Retrieve user data
 * @param {Object} state
 * @return {Object}
 */
function getUser(state) {
  return state.user;
}

/**
 * Verifies if access token exists
 * @param {Object} state
 * @return {Boolean}
 */
function isAuthenticated(state, getters) {
  return !!getters.getAccessToken;
}

export default {
  getAccessToken,
  getUser,
  isAuthenticated
};
