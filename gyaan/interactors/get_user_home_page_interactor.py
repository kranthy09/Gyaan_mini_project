from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.exceptions.exceptions \
    import (InvalidOffset,
            InvalidLimit)


class UserHomePageInteractor:

    def __init__(self, post_storage: PostStorageInterface):
        self.post_storage = post_storage

    def get_user_home_page_wrapper(self, offset: int, limit: int, user_id: int,
                                   post_presenter: PostPresenterInterface):
        try:
            self.get_user_home_page(user_id=user_id,
                                    offset=offset, limit=limit)
        except InvalidOffset:
            post_presenter.get_response_for_invalid_offset()
        except InvalidLimit:
            post_presenter.get_response_for_invalid_limit()

    def get_user_home_page(self, user_id: int,
                           offset: int, limit: int):
        self.validate_offset(offset=offset)
        self.validate_limit(limit=limit)

    @staticmethod
    def validate_offset(offset: int):

        if offset < 0:
            raise InvalidOffset
        else:
            return True

    @staticmethod
    def validate_limit(limit: int):

        if limit < 0:
            raise InvalidLimit
        else:
            return True
