from abc import ABC, abstractmethod
from typing import List
from gyaan.interactors.storages.dtos \
    import (PostDto,
            PostTag,
            TagDto,
            PostComment,
            CommentDto,
            CommentReplyDto,
            ReplyDto)


class PostStorageInterface(ABC):

    @abstractmethod
    def get_user_following_domain_ids(self, user_id: int) \
            -> List[int]:
        pass

    @abstractmethod
    def get_approved_post_ids_in_user_domains(
            self, domain_ids: List[int]) \
            -> List[int]:
        pass

    @abstractmethod
    def validate_post_ids(self, post_ids: List[int]):
        pass

    @abstractmethod
    def get_basic_post_details(self, post_ids: List[int]) \
            -> List[PostDto]:
        pass

    @abstractmethod
    def get_post_tag_ids(self, post_ids: List[int]) \
            -> List[PostTag]:
        pass

    @abstractmethod
    def get_tag_dtos(self, tag_ids: List[int]) \
            -> List[TagDto]:
        pass

    @abstractmethod
    def get_post_comment_ids_sort_by_date(
            self, post_ids:List[int]) \
            -> List[PostComment]:
        pass

    @abstractmethod
    def get_comment_dtos(self, comment_ids: List[int]) \
            -> List[CommentDto]:
        pass

    @abstractmethod
    def get_comment_reply_ids_dtos(self, comment_ids: List[int]) \
            -> List[CommentReplyDto]:
        pass

    @abstractmethod
    def get_reply_dtos(self, reply_ids: List[int]) \
            -> List[ReplyDto]:
        pass