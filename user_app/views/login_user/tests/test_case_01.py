"""
# TODO: Update test case description
"""
import json
from unittest.mock import patch
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from common.dtos import UserAuthTokensDTO
from user_app.models.models import User


REQUEST_BODY = """
{
    "username": "username",
    "password": "pass"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01LoginUserAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username: str, password: str):
        super(TestCase01LoginUserAPITestCase, self).setupUser(
            username=username,
            password=password
        )

    @patch('common.oauth_user_auth_tokens_service.OAuthUserAuthTokensService.create_user_auth_tokens')
    def test_case(self,create_user_auth_tokens):
        user_auth_token_dto = UserAuthTokensDTO(
            user_id=28,
            access_token="token",
            refresh_token="refresh_token",
            expires_in=10000
        )
        create_user_auth_tokens.return_value = user_auth_token_dto
        user = User.objects.create(username="username", password="pass", user_role="")
        response = self.default_test_case()
        response_content = json.loads(response.content)
        self.assert_match_snapshot(
            name="username",
            value=user.username
        )
        self.assert_match_snapshot(
            name="user_id",
            value=response_content['user_id']
        )
        self.assert_match_snapshot(
            name="access_token",
            value=response_content['access_token']
        )
        self.assert_match_snapshot(
            name="user_role",
            value=response_content['user_role']
        )
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.