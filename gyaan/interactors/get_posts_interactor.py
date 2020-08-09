from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.exceptions.exceptions import InvalidPostId
from typing import List
from gyaan.interactors.storages.dtos \
    import (CommentDto,
            PostReactionDto,
            ReactionDto,
            PostReactionWithCountUser)



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
        post_dtos = self.post_storage \
            .get_basic_post_details(post_ids=post_ids)
        post_tag_ids_dtos = self.post_storage \
            .get_post_tag_ids(post_ids=post_ids)
        tag_ids = [post_tag.tag_id for post_tag in post_tag_ids_dtos]
        tag_dtos = self.post_storage \
            .get_tag_dtos(tag_ids=tag_ids)
        post_comment_ids_dtos = self.post_storage \
            .get_post_comment_ids_sort_by_date(post_ids=post_ids)
        comment_ids = [post_comment.comment_id
                       for post_comment in post_comment_ids_dtos]
        comment_dtos = self.get_latest_comments(comment_ids=comment_ids)
        comment_reply_ids_dto = self.post_storage \
            .get_comment_reply_ids_dtos(comment_ids=comment_ids)
        reply_ids = [comment_reply.reply_id
                     for comment_reply in comment_reply_ids_dto]
        reply_dtos = self.post_storage \
            .get_reply_dtos(reply_ids=reply_ids)
        post_reaction_ids_dtos = self.post_storage \
            .get_post_reactions_ids_dtos(post_ids=post_ids)
        reaction_ids = [post_reaction.reaction_id
                        for post_reaction in post_reaction_ids_dtos]
        reaction_dtos = self.post_storage \
            .get_reaction_dtos(reaction_ids=reaction_ids)
        post_reactions_with_count_user_details = \
            self._call_for_post_reactions_count_user_details(
                post_reaction_ids_dtos=post_reaction_ids_dtos,
                reaction_dtos=reaction_dtos
            )


    def get_latest_comments(self, comment_ids: List[int]) \
            -> List[CommentDto]:

        number_of_comments = len(comment_ids)
        if number_of_comments > 2:
            comment_ids = comment_ids[:2]
        comment_dtos = self.post_storage \
            .get_comment_dtos(comment_ids=comment_ids)
        return comment_dtos

    def _call_for_post_reactions_count_user_details(
            self,
            reaction_dtos: List[ReactionDto],
            post_reaction_ids_dtos: List[PostReactionDto]) \
            -> PostReactionWithCountUser:
        pass
