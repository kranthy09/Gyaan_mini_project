from abc import ABC, abstractmethod
from user_app.interactors.storages.dtos \
        import (UserRoleDto,
                UserDetailsDto)
from typing import List


class StorageInterface(ABC):

    @abstractmethod
    def validate_username(self, username: str):
        pass

    @abstractmethod
    def validate_password(self, username: str, password: str):
        pass

    @abstractmethod
    def get_user_role_dto(self, username: str, password: str) \
            -> UserRoleDto:
        pass

    @abstractmethod
    def get_user_details(self, user_ids: List[int]) -> UserDetailsDto:
        pass