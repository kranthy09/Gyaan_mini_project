# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserDomainsAPITestCase.test_case status_code'] = '500'

snapshots['TestCase01GetUserDomainsAPITestCase.test_case body'] = {
    'user_details': {
        'name': [
            'This field may not be blank.'
        ],
        'profile_pic': [
            'This field may not be blank.'
        ]
    }
}
