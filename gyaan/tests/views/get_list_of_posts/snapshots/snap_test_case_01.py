# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetListOfPostsAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01GetListOfPostsAPITestCase.test_case body'] = {
    'result': [
        {
            'post_answer': {
                'answer_content': 'string',
                'answer_id': 1,
                'answered_at': '2099-12-31 00:00:00',
                'answered_by': {
                    'name': 'string',
                    'profile_pic': 'string',
                    'role': 'USER',
                    'user_id': 'string',
                    'username': 'string'
                },
                'approved_by': {
                    'domain_name': 'string',
                    'name': 'string',
                    'user_id': 1
                }
            },
            'post_comments': [
                {
                    'comment_content': 'string',
                    'comment_id': 1,
                    'commented_at': '2099-12-31 00:00:00',
                    'commented_by': {
                        'name': 'string',
                        'profile_pic': 'string',
                        'role': 'USER',
                        'user_id': 'string',
                        'username': 'string'
                    },
                    'replies': [
                        {
                            'replied_at': '2099-12-31 00:00:00',
                            'replied_by': {
                                'name': 'string',
                                'profile_pic': 'string',
                                'role': 'USER',
                                'user_id': 'string',
                                'username': 'string'
                            },
                            'reply_content': 'string',
                            'reply_id': 1
                        }
                    ]
                }
            ],
            'post_content': 'string',
            'post_id': 1,
            'post_reactions': {
                'reacted_by': [
                    {
                        'name': 'string',
                        'profile_pic': 'string',
                        'role': 'USER',
                        'user_id': 'string',
                        'username': 'string'
                    }
                ],
                'reactions_count': 1
            },
            'post_tags': [
                {
                    'tag_id': 1,
                    'tag_name': 'string'
                }
            ],
            'posted_by': {
                'name': 'string',
                'profile_pic': 'string',
                'role': 'USER',
                'user_id': 'string',
                'username': 'string'
            }
        }
    ],
    'total_posts_count': 1
}
