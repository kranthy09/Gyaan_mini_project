from abc import ABC, abstractmethod
from user_app.interactors.storages.dtos \
        import TokenDto


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def get_response_for_login(self, token_dto: TokenDto):
        pass