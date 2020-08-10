from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.exceptions.exceptions import InvalidPostId
from typing import List
from gyaan.adapters.dtos \
    import UserDetailsDto
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
        post_answer_ids_dtos = self.post_storage \
            .get_post_answer_ids_dtos(
            post_ids=post_ids
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
            -> List[PostReactionWithCountUser]:

        post_reactions_with_count_user_details = []
        for post_reaction in post_reaction_ids_dtos:
            reacted_by_list = []
            for reaction_dto in reaction_dtos:
                if post_reaction.reaction_id == reaction_dto.reaction_id:
                    user_details_dto = self._call_for_reacted_by(
                        reacted_by_id=reaction_dto.reacted_by_id
                    )
                    reacted_by_list.append(
                        user_details_dto
                    )
            post_reactions_with_count_user_details.append(
                PostReactionWithCountUser(
                    reactions_count=len(reacted_by_list),
                    reacted_by=reacted_by_list
                )
            )
        return post_reactions_with_count_user_details

    @staticmethod
    def _call_for_reacted_by(reacted_by_id: int) \
            -> UserDetailsDto:

        # user_ids = [reacted_by_id]
        # from gyaan.adapters.userapp_adapter \
        #     import UserAppAdapter
        #
        # user_adapter = UserAppAdapter()
        # user_details_dtos = \
        #     user_adapter.get_user_details_dto(
        #         user_ids=user_ids
        #     )
        # return user_details_dtos[0]
        pass
