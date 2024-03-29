"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from gyaan.models.factories import (DomainFactory,
                                    DomainExpertsFactory,
                                    DomainRequestsFactory,
                                    DomainPostFactory,
                                    DomainTagFactory)
from user_app.models.factory import UserFactory


class TestCase01GetUserDomainsAPITestCase(TestUtils):
    pytestmark = pytest.mark.django_db
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture()
    def setup(self, api_user):
        DomainFactory.reset_sequence()
        DomainExpertsFactory.reset_sequence()
        DomainRequestsFactory.reset_sequence()
        DomainPostFactory.reset_sequence()
        DomainTagFactory.reset_sequence()
        UserFactory.reset_sequence()

        user = UserFactory(username="kranthi", user_role="USER", profile_pic="profile.com")
        DomainFactory.create_batch(size=10)
        DomainExpertsFactory(domain_expert_id=1)
        DomainRequestsFactory(requested_by=user.id, is_approved=False)
        DomainRequestsFactory(requested_by=user.id, is_approved=True)
        DomainPostFactory(user_id=user.id)
        DomainTagFactory()

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
