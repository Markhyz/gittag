from backend.utils import encode_jwt

TEST_USER_ID = 1

TEST_REPOSITORY_ID = 1

TEST_TAG_NAME = 'test'

TEST_ACCESS_TOKEN = encode_jwt({'user_id': TEST_USER_ID})
