import pytest
from unittest.mock import create_autospec


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
        pass

        # Act

        # Assert
