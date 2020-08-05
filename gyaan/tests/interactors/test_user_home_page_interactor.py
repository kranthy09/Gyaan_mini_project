import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions \
    import BadRequest
from gyaan.interactors.get_user_home_page_interactor \
    import UserHomePageInteractor


class TestUserHomePageInteractor:

    @pytest.fixture
    def post_storage(self):
        from gyaan.interactors.storages.post_storage_interface \
            import PostStorageInterface
        return create_autospec(PostStorageInterface)

    @pytest.fixture
    def post_presenter(self):
        from gyaan.interactors.presenters.post_presenter_interface \
            import PostPresenterInterface
        return create_autospec(PostPresenterInterface)

    def test_for_user_home_page_interactor_with_invalid_offset(self, post_storage, post_presenter):
        # Arrange
        user_id = 1
        offset = -1
        limit = 3

        interactor = UserHomePageInteractor(post_storage=post_storage)

        post_presenter.get_response_for_invalid_offset.side_effect = BadRequest

        # Act
        with pytest.raises(BadRequest):
            interactor.get_user_home_page_wrapper(
                offset=offset,
                limit=limit,
                user_id=user_id,
                post_presenter=post_presenter
            )

        # Assert
        post_presenter.get_response_for_invalid_offset \
            .assert_called_once()

    def test_for_user_home_page_with_invalid_limit(self, post_storage, post_presenter):
        # Arrange
        user_id = 1
        offset = 1
        limit = -3

        interactor = UserHomePageInteractor(post_storage=post_storage)

        post_presenter.get_response_for_invalid_limit.side_effect = BadRequest

        # Act
        with pytest.raises(BadRequest):
            interactor.get_user_home_page_wrapper(
                offset=offset,
                limit=limit,
                user_id=user_id,
                post_presenter=post_presenter
            )

        # Assert
        post_presenter.get_response_for_invalid_limit \
            .assert_called_once()

    @patch('gyaan.interactors.get_posts_interactor.GetPost.get_posts')
    def test_for_get_user_home_page_interactor(self,
                                               get_posts,
                                               post_storage,
                                               post_presenter):
        # Arrange
        user_id = 1
        limit = 1
        offset = 5
        user_following_domain_ids = [1, 2]
        approved_post_ids = [1]
        mock_post_response = {
            "total_posts_count": 2,
            "result": [
                {
                    "post_id": 1,
                    "post_title": "title_1",
                    "post_content": "content_1",
                    "posted_at": "2020-08-05T04:24:50.743Z",
                    "post_comments_count": 1,
                    "posted_by": {
                        "user_id": 1,
                        "name": "skywaler",
                        "profile_pic": "profile.pic",
                        "username": "kranthi",
                        "role": "USER"
                    },
                    "post_tags": [
                        {
                            "tag_id": 0,
                            "tag_name": "Python"
                        }
                    ],
                    "post_reactions": {
                        "reactions_count": 1,
                        "reacted_by": [
                            {
                                "user_id": 28,
                                "name": "some_name",
                                "profile_pic": "some_pic.pic",
                                "username": "username",
                                "role": "USER"
                            }
                        ]
                    },
                    "post_comments": [
                        {
                            "comment_id": 1,
                            "comment_content": "comment_1",
                            "commented_at": "2020-08-05T04:24:50.743Z",
                            "commented_by": {
                                "user_id": 28,
                                "name": "some_name",
                                "profile_pic": "some_pic.pic",
                                "username": "username",
                                "role": "USER"
                            },
                            "replies": []
                        }
                    ],
                    "post_answer": {
                        "answer_id": 1,
                        "answer_content": "comment_1",
                        "answered_at": "2020-08-05T04:24:50.743Z",
                        "answered_by": {
                            "user_id": 28,
                            "name": "some_name",
                            "profile_pic": "some_pic.pic",
                            "username": "username",
                            "role": "USER"
                        },
                        "approved_by": {
                            "user_id": 1,
                            "name": "domain_expert_name",
                            "domain_name": "Python"
                        }
                    }
                }
            ]
        }

        interactor = UserHomePageInteractor(
            post_storage=post_storage
        )
        post_storage.get_user_following_domain_ids \
            .return_value = user_following_domain_ids
        post_storage.get_approved_post_ids_in_user_domains \
            .return_value = approved_post_ids
        get_posts.return_value = mock_post_response

        # Act
        response = interactor.get_user_home_page_wrapper(
            limit=limit, offset=offset,
            user_id=user_id, post_presenter=post_presenter
        )

        # Assert
        post_storage.get_user_following_domain_ids \
            .assert_called_once_with(user_id=user_id)
        post_storage.get_approved_post_ids_in_user_domains \
            .assert_called_once_with(domain_ids=user_following_domain_ids)
        assert response == mock_post_response
