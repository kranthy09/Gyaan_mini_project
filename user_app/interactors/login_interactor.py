from common.oauth2_storage import OAuth2SQLStorage
from user_app.exceptions.exceptions \
        import (InvalidUsername,
                InvalidPassword)
from user_app.interactors.storages.dtos import TokenDto
from user_app.interactors.storages.storage_interface \
    import StorageInterface
from user_app.interactors.presenters.presenter_interface \
    import PresenterInterface


class LoginInteractor:

    def __init__(self, storage: StorageInterface,
                    oauth2_storage: OAuth2SQLStorage):
        self.storage = storage
        self.oauth2_storage = oauth2_storage

    def login_wrapper(self, username: str, password: str,
                      presenter: PresenterInterface):
        try:
            token_dto = self.login(username=username, password=password)
        except InvalidUsername:
            return presenter.raise_exception_for_invalid_username()
        except InvalidPassword:
            return presenter.raise_exception_for_invalid_password()

        response = presenter.get_response_for_login(token_dto=token_dto)
        return response

    def login(self, username: str, password: str):

        self.storage.validate_username(username=username)
        self.storage.validate_password(username=username, password=password)
        user_role_dto = self.storage.get_user_role_dto(username=username, password=password)

        from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

        token_service = OAuthUserAuthTokensService(oauth2_storage=self.oauth2_storage)
        user_access_token_dto = token_service.create_user_auth_tokens(user_id=user_role_dto.user_id)

        token_dto = TokenDto(
            user_id=user_role_dto.user_id,
            access_token=user_access_token_dto.access_token,
            user_role=user_role_dto.user_role
        )
        return token_dto