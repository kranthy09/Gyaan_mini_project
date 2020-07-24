from typing import List
from user_app.storages.storage_implementation \
    import StorageImplementation
from user_app.interactors.get_user_details_interactor \
    import UserDetailsInteractor


class ServiceInterface:

    @staticmethod
    def get_user_details_dtos(user_ids: List[int]):
        storage = StorageImplementation()
        interactor = UserDetailsInteractor(storage=storage)
        user_details_dtos = interactor.get_user_details_dtos(user_ids=user_ids)
        return user_details_dtos
