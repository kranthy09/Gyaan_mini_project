from abc import ABC, abstractmethod
from gyaan.interactors.storages.dtos \
    import UserDomainsDetails


class DomainPresenterInterface(ABC):

    @abstractmethod
    def get_response_for_user_domains(
            self,
            user_domains_details_dto: UserDomainsDetails):
        pass