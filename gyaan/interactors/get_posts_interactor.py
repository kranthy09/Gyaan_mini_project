from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.exceptions.exceptions import InvalidPostId
from typing import List


class GetPost:
    def __init__(self, post_storage: PostStorageInterface):
        self.post_storage = post_storage

    def get_posts_wrapper(self, post_ids: List[int],
                          post_presenter: PostPresenterInterface):
        try:
            self.get_posts(post_ids=post_ids)
        except InvalidPostId:
            post_presenter.get_response_for_invalid_post_ids(post_ids)

    def get_posts(self, post_ids: List[int]):

        self.post_storage.validate_post_ids(post_ids=post_ids)
