# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserDomainsAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01GetUserDomainsAPITestCase.test_case body'] = {
    'domain_expert_pendings': [
    ],
    'domain_requests': [
        {
            'name': 'name 00',
            'profile_pic': 'profile.com',
            'role': 'USER',
            'user_id': '2',
            'username': 'kranthi'
        }
    ],
    'suggested_domains': [
        {
            'domain_id': 1,
            'domain_name': 'domain_name 00'
        },
        {
            'domain_id': 2,
            'domain_name': 'domain_name 01'
        },
        {
            'domain_id': 3,
            'domain_name': 'domain_name 02'
        },
        {
            'domain_id': 4,
            'domain_name': 'domain_name 03'
        },
        {
            'domain_id': 5,
            'domain_name': 'domain_name 04'
        },
        {
            'domain_id': 6,
            'domain_name': 'domain_name 05'
        },
        {
            'domain_id': 7,
            'domain_name': 'domain_name 06'
        },
        {
            'domain_id': 8,
            'domain_name': 'domain_name 07'
        },
        {
            'domain_id': 9,
            'domain_name': 'domain_name 08'
        },
        {
            'domain_id': 10,
            'domain_name': 'domain_name 09'
        }
    ],
    'user_details': {
        'name': '',
        'profile_pic': '',
        'role': '',
        'user_id': '1',
        'username': 'apiuser'
    },
    'user_domains_posts': {
        'domains': [
        ],
        'total_posts': 0
    },
    'user_following_domains': [
    ],
    'user_pending_domain_posts': {
        'pending_domains': [
        ],
        'total_pending_posts': 0
    }
}
