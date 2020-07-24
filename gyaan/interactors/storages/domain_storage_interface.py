from abc import ABC, abstractmethod
from typing import List
from gyaan.interactors.storages.dtos \
    import (DomainDto,
            DomainMetrics)


class DomainStorageInterface(ABC):

    @abstractmethod
    def get_user_following_domain_ids(self, user_id: int) \
        -> List[int]:
        pass

    @abstractmethod
    def get_all_domains_dtos(self)-> List[DomainDto]:
        pass

    @abstractmethod
    def get_user_posts_with_domain(self, user_id: int) \
        -> DomainMetrics:
        pass

    @abstractmethod
    def get_user_pending_posts_with_domain(self, user_id: int) \
        -> DomainMetrics:
        pass

    @abstractmethod
    def is_user_domain_expert(self, user_id: int)-> bool:
        pass

    @abstractmethod
    def get_domain_expert_domain_ids(self, domain_expert_id: int) \
        -> List[int]:
        pass

    @abstractmethod
    def get_domain_requests_ids(self, domain_ids: List[int]) \
        -> List[int]:
        pass

    @abstractmethod
    def get_domain_expert_approval_posts(self, domain_expert_id: int) \
        -> List[DomainDto]:
        pass