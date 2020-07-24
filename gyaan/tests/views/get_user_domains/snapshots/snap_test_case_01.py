# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserDomainsAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01GetUserDomainsAPITestCase.test_case body'] = {
    'domain_expert_pendings': [
        {
            'domain_id': 1,
            'domain_name': 'string',
            'posts_count': 1
        }
    ],
    'domain_requests': [
        {
            'name': 'string',
            'profile_pic': 'string',
            'role': 'USER',
            'user_id': 'string',
            'username': 'string'
        }
    ],
    'suggested_domains': [
        {
            'domain_id': 1,
            'domain_name': 'string'
        }
    ],
    'user_details': {
        'name': 'string',
        'profile_pic': 'string',
        'role': 'USER',
        'user_id': 'string',
        'username': 'string'
    },
    'user_domains_posts': {
        'domains': [
            {
                'domain_id': 1,
                'domain_name': 'string',
                'posts_count': 1
            }
        ],
        'total_posts': 1
    },
    'user_following_domains': [
        {
            'domain_id': 1,
            'domain_name': 'string'
        }
    ],
    'user_pending_domain_posts': {
        'pending_domains': [
            {
                'domain_id': 1,
                'domain_name': 'string',
                'posts_count': 1
            }
        ],
        'total_pending_posts': 1
    }
}
