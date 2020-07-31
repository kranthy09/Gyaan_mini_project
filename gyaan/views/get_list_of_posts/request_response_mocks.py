


RESPONSE_201_JSON = """
{
    "total_posts_count": 1,
    "result": [
        {
            "post_id": 1,
            "post_title": "string",
            "post_content": "string",
            "post_comments_count": 1,
            "posted_by": {
                "user_id": "string",
                "name": "string",
                "profile_pic": "string",
                "username": "string",
                "role": "USER"
            },
            "post_tags": [
                {
                    "tag_id": 1,
                    "tag_name": "string"
                }
            ],
            "post_reactions": {
                "reactions_count": 1,
                "reacted_by": [
                    {
                        "user_id": "string",
                        "name": "string",
                        "profile_pic": "string",
                        "username": "string",
                        "role": "USER"
                    }
                ]
            },
            "post_comments": [
                {
                    "comment_id": 1,
                    "comment_content": "string",
                    "commented_at": "2099-12-31 00:00:00",
                    "commented_by": {
                        "user_id": "string",
                        "name": "string",
                        "profile_pic": "string",
                        "username": "string",
                        "role": "USER"
                    },
                    "replies": [
                        {
                            "reply_id": 1,
                            "reply_content": "string",
                            "replied_at": "2099-12-31 00:00:00",
                            "replied_by": {
                                "user_id": "string",
                                "name": "string",
                                "profile_pic": "string",
                                "username": "string",
                                "role": "USER"
                            }
                        }
                    ]
                }
            ],
            "post_answer": {
                "answer_id": 1,
                "answer_content": "string",
                "answered_at": "2099-12-31 00:00:00",
                "answered_by": {
                    "user_id": "string",
                    "name": "string",
                    "profile_pic": "string",
                    "username": "string",
                    "role": "USER"
                },
                "approved_by": {
                    "user_id": 1,
                    "name": "string",
                    "domain_name": "string"
                }
            }
        }
    ]
}
"""

