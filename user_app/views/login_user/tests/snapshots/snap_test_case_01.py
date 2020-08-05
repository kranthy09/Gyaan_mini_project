# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01LoginUserAPITestCase::test_case status'] = 404

snapshots['TestCase01LoginUserAPITestCase::test_case body'] = {
    'http_response_code': 404,
    'res_status': 'INVALID_PASSWORD',
    'response': 'Given Password is incorrect'
}

snapshots['TestCase01LoginUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '99',
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

snapshots['TestCase01LoginUserAPITestCase::test_case username'] = 'username'
