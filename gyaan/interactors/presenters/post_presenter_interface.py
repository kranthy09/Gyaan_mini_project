from abc import ABC, abstractmethod


class PostPresenterInterface(ABC):

    @abstractmethod
    def get_response_for_invalid_offset(self):
        pass

    @abstractmethod
    def get_response_for_invalid_limit(self):
        pass