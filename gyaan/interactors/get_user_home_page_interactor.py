from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.exceptions.exceptions \
    import (InvalidOffset,
            InvalidLimit)
from typing import List


class UserHomePageInteractor:

    def __init__(self, post_storage: PostStorageInterface):
        self.post_storage = post_storage

    def get_user_home_page_wrapper(self, offset: int, limit: int, user_id: int,
                                   post_presenter: PostPresenterInterface):
        try:
            post_details_dto_with_count \
                = self.get_user_home_page(user_id=user_id,
                                    offset=offset, limit=limit)
        except InvalidOffset:
            return post_presenter.get_response_for_invalid_offset()
        except InvalidLimit:
            return post_presenter.get_response_for_invalid_limit()
        return post_details_dto_with_count

    def get_user_home_page(self, user_id: int,
                           offset: int, limit: int):
        self.validate_offset(offset=offset)
        self.validate_limit(limit=limit)
        user_following_domain_ids = \
            self.post_storage.get_user_following_domain_ids(user_id=user_id)
        approved_post_ids = \
            self.post_storage.get_approved_post_ids_in_user_domains(
                domain_ids=user_following_domain_ids
            )
        post_details_dto_with_count = \
            self._call_get_posts_interactor(post_ids=approved_post_ids)
        return post_details_dto_with_count

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

    def _call_get_posts_interactor(self, post_ids: List[int]):
        from gyaan.interactors.get_posts_interactor import GetPost

        post_interactor = GetPost(
            post_storage=self.post_storage
        )
        post_details_dtos_with_count = post_interactor.get_posts(post_ids=post_ids)
        return post_details_dtos_with_count
