# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01LoginUserAPITestCase::test_case status'] = 201

snapshots['TestCase01LoginUserAPITestCase::test_case body'] = {
    'access_token': 'token',
    'user_id': 1,
    'user_role': 'USER'
}

snapshots['TestCase01LoginUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '55',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}

snapshots['TestCase01LoginUserAPITestCase::test_case username'] = 'kranthi'

snapshots['TestCase01LoginUserAPITestCase::test_case user_id'] = 1

snapshots['TestCase01LoginUserAPITestCase::test_case access_token'] = 'token'

snapshots['TestCase01LoginUserAPITestCase::test_case user_role'] = 'USER'
