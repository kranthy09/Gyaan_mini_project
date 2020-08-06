from abc import ABC, abstractmethod
from typing import List


class PostPresenterInterface(ABC):

    @abstractmethod
    def get_response_for_invalid_offset(self):
        pass

    @abstractmethod
    def get_response_for_invalid_limit(self):
        pass

    @abstractmethod
    def get_response_for_invalid_post_ids(
            self,
            post_ids: List[int]):
        pass

    @abstractmethod
    def get_response_for_home_page(
            self, post_details_dto_with_count):
        pass
