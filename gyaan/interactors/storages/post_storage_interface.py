from abc import ABC, abstractmethod
from typing import List


class PostStorageInterface(ABC):

    @abstractmethod
    def get_user_following_domain_ids(self, user_id: int):
        pass

    @abstractmethod
    def get_approved_post_ids_in_user_domains(
            self, domain_ids: List[int]) \
            -> List[int]:
        pass
