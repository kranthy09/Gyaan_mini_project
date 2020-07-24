# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01LoginUserAPITestCase.test_case status_code'] = '404'

snapshots['TestCase01LoginUserAPITestCase.test_case body'] = {
    'http_response_code': 404,
    'res_status': 'INVALID_USERNAME',
    'response': 'Given Username is not valid'
}
