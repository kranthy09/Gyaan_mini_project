from user_app.interactors.storages.storage_interface \
    import StorageInterface
from typing import List


class UserDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_details_dtos(self, user_ids: List[int]):
        user_details_dto_list = \
                self.storage.get_user_details(user_ids=user_ids)
        return user_details_dto_list
