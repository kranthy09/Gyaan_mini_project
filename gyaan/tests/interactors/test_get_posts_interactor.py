import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions \
    import NotFound
from gyaan.exceptions.exceptions import InvalidPostId
from gyaan.interactors.get_posts_interactor import GetPost
from gyaan.interactors.storages.dtos import PostDto


class TestGetPostInteractor:

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

    def test_get_posts_for_invalid_post_ids(self,
                                            post_storage,
                                            post_presenter):

        # Arrange
        post_ids = [-1, -2, -3]

        interactor = GetPost(
            post_storage=post_storage
        )

        post_storage.validate_post_ids.side_effect = InvalidPostId
        post_presenter.get_response_for_invalid_post_ids \
            .side_effect = NotFound


        # Act
        with pytest.raises(NotFound):
            interactor.get_posts_wrapper(
                post_ids=post_ids,
                post_presenter=post_presenter
            )

        # Assert
        post_storage.validate_post_ids \
            .assert_called_once_with(post_ids=post_ids)
        post_presenter.get_response_for_invalid_post_ids \
            .assert_called_once()

    def test_get_posts_interactor(self, post_storage, post_presenter):

        # Arrange
        user_id = 1
        post_ids = [1, 2]
        post_dtos = [
            PostDto(
                post_id=1,
                post_title="post_title_1",
                post_content="post_content_1",
                posted_at="2020-08-07"
            ),
            PostDto(
                post_id=1,
                post_title="post_title_2",
                post_content="post_content_2",
                posted_at="2020-08-04"
            )

        ]

        interactor = GetPost(
            post_storage=post_storage
        )
        post_storage.get_basic_post_details \
            .return_value = post_dtos

        # Act
        response = interactor.get_posts_wrapper(
            post_ids=post_ids,
            post_presenter=post_presenter
        )


        # Assert