import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound
from common.oauth2_storage import OAuth2SQLStorage
from common.dtos import UserAuthTokensDTO
from user_app.exceptions.exceptions \
        import (InvalidUsername,
                InvalidPassword)
from user_app.interactors.storages.dtos import UserRoleDto
from user_app.interactors.login_interactor import LoginInteractor
from user_app.interactors.storages.storage_interface \
    import StorageInterface
from user_app.interactors.presenters.presenter_interface \
    import PresenterInterface


class TestLoginInteractor:

    def test_login_interactor_invalid_username(self):

        # Arrange
        username = "**"
        password = "monty"

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        oauth2_storage = create_autospec(OAuth2SQLStorage)

        interactor = LoginInteractor(
            storage=storage,
            oauth2_storage=oauth2_storage
        )

        storage.validate_username.side_effect = InvalidUsername
        presenter.raise_exception_for_invalid_username.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.login_wrapper(username=username,
                                     password=password,
                                     presenter=presenter)

        # Assert
        storage.validate_username \
                .assert_called_once_with(username=username)
        presenter.raise_exception_for_invalid_username \
                .assert_called_once()

    def test_login_interactor_for_invalid_password(self):
        # Arrange
        username = "**"
        password = "***"

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        oauth2_storage = create_autospec(OAuth2SQLStorage)

        interactor = LoginInteractor(
            storage=storage,
            oauth2_storage=oauth2_storage
        )

        storage.validate_username.return_value = True
        storage.validate_password.side_effect = InvalidPassword
        presenter.raise_exception_for_invalid_password.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.login_wrapper(username=username,
                                     password=password,
                                     presenter=presenter)

        # Assert
        storage.validate_username \
            .assert_called_once_with(username=username)
        storage.validate_password \
            .assert_called_once_with(username=username, password=password)
        presenter.raise_exception_for_invalid_password \
            .assert_called_once()

    @patch('common.oauth_user_auth_tokens_service.OAuthUserAuthTokensService.create_user_auth_tokens')
    def test_for_login_interactor(self, create_user_auth_tokens):
        # Arrange
        username = "monty"
        password = "monty"

        user_role_dto = UserRoleDto(
            user_id=1,
            user_role="USER"
        )

        user_access_token_dto = UserAuthTokensDTO(
            user_id=1,
            access_token="token",
            refresh_token="refresh_token",
            expires_in=100000
        )

        login_response = {
            "user_id": 1,
            "access_token": "token",
            "role": "USER"
        }

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        oauth2_storage = create_autospec(OAuth2SQLStorage)

        interactor = LoginInteractor(
            storage=storage,
            oauth2_storage=oauth2_storage
        )

        storage.validate_username.return_value = True
        storage.validate_password.return_value = True
        storage.get_user_role_dto.return_value = user_role_dto
        create_user_auth_tokens.return_value = user_access_token_dto
        presenter.get_response_for_login_interactor = login_response

        # Act
        response = interactor.login_wrapper(username=username,
                                            password=password,
                                            presenter=presenter)

        # Assert
        storage.validate_username \
            .assert_called_once_with(username=username)
        storage.validate_password \
            .assert_called_once_with(username=username, password=password)
        storage.get_user_role_dto \
            .assert_called_once_with(username=username, password=password)
