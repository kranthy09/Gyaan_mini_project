import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions \
    import BadRequest
from gyaan.interactors.get_user_home_page_interactor \
    import UserHomePageInteractor
from gyaan.exceptions.exceptions \
    import (InvalidOffset,
            InvalidLimit)


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

    def test_for_get_user_home_page_interactor(self):

        pass