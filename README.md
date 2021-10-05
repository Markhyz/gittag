# GitTag

Web application developed with Django that allows GitHub users to list their starred repositories and add tags.

The backend (API) was developed using the Django REST framework, while the frontend (website) was developed using Vue.js 2.

## Configuration

The web server uses the environment variable `DJANGO_ENVIRONMENT` to distinguish between a local development server (`"development"`) and a production server (`"production"`).

For both environments, the environment variables `GITHUB_OAUTH_CLIENT_ID` and `GITHUB_OAUTH_CLIENT_SECRET` must be defined using the credentials of a Github OAuth application.

In the production environment, the environment variable `DJANGO_SECRET_KEY` must be defined.

## Starting the server

To start a local server, the backend (standard Django application) and frontend (standard Vue.js application) must be started separately.

For the production server, the frontend must be built (to generate static files) before starting the Django server.
