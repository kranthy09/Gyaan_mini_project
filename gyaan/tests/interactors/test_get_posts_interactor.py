import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions \
    import NotFound
from gyaan.exceptions.exceptions import InvalidPostId
from gyaan.interactors.get_posts_interactor import GetPost
from gyaan.interactors.storages.dtos \
    import (PostDto,
            PostTag,
            TagDto,
            PostComment,
            CommentDto,
            CommentReplyDto,
            ReplyDto,
            PostReactionDto,
            ReactionDto,
            PostAnswerDto)
from gyaan.adapters.dtos \
    import UserDetailsDto
from user_app.constants.enums \
    import UserRoles


class TestGetPostInteractor:

    @pytest.fixture
    def post_storage(self):
        from gyaan.interactors.storages.post_storage_interface \
            import PostStorageInterface
        return create_autospec(PostStorageInterface)

    @pytest.fixture
    def post_presenter(self):
        from gyaan.interactors.presenters.post_presenter_interface \
            import PostPresenterInterface
        return create_autospec(PostPresenterInterface)

    def test_get_posts_for_invalid_post_ids(self,
                                            post_storage,
                                            post_presenter):

        # Arrange
        post_ids = [-1, -2, -3]

        interactor = GetPost(
            post_storage=post_storage
        )

        post_storage.validate_post_ids.side_effect = InvalidPostId
        post_presenter.get_response_for_invalid_post_ids \
            .side_effect = NotFound


        # Act
        with pytest.raises(NotFound):
            interactor.get_posts_wrapper(
                post_ids=post_ids,
                post_presenter=post_presenter
            )

        # Assert
        post_storage.validate_post_ids \
            .assert_called_once_with(post_ids=post_ids)
        post_presenter.get_response_for_invalid_post_ids \
            .assert_called_once()

    def test_get_posts_interactor(self, post_storage, post_presenter):

        # Arrange
        user_id = 1
        user2 = UserDetailsDto(
            user_id=2,
            username='user2',
            name='kingkhan',
            profile_pic='king.khan',
            role=UserRoles.USER
        )
        post_ids = [1, 2]
        post_dtos = [
            PostDto(
                post_id=1,
                post_title="post_title_1",
                post_content="post_content_1",
                posted_at="2020-08-07",
                post_comments_count=2
            ),
            PostDto(
                post_id=1,
                post_title="post_title_2",
                post_content="post_content_2",
                posted_at="2020-08-04",
                post_comments_count=2
            )
        ]
        post_tag_ids_dtos = [
            PostTag(
                post_id=1,
                tag_id=1
            ),
            PostTag(
                post_id=1,
                tag_id=2
            ),
            PostTag(
                post_id=2,
                tag_id=3
            ),
            PostTag(
                post_id=2,
                tag_id=4
            )
        ]
        tag_ids = [post_tag.tag_id
                   for post_tag in post_tag_ids_dtos]
        tag_dtos = [
            TagDto(
                tag_id=1,
                tag_name='python'
            ),
            TagDto(
                tag_id=2,
                tag_name='django'
            ),
            TagDto(
                tag_id=3,
                tag_name='react'
            ),
            TagDto(
                tag_id=4,
                tag_name='javascript'
            )
        ]
        post_comment_ids_dtos = [
            PostComment(
                post_id=1,
                comment_id=1
            ),
            PostComment(
                post_id=2,
                comment_id=2
            )
        ]
        comment_ids = [post_comment.comment_id
                       for post_comment in post_comment_ids_dtos]
        comment_dtos = [
            CommentDto(
                comment_id=1,
                comment_content='comment_1',
                commented_at="25-08-2020",
                commented_by_id=3
            ),
            CommentDto(
                comment_id=2,
                comment_content='comment_2',
                commented_at="27-08-2020",
                commented_by_id=5
            )
        ]
        comment_reply_ids_dto = [
            CommentReplyDto(
                comment_id=1,
                reply_id=1
            ),
            CommentReplyDto(
                comment_id=2,
                reply_id=2
            )
        ]
        reply_ids = [comment_reply.reply_id
                     for comment_reply in comment_reply_ids_dto]
        reply_dtos = [
            ReplyDto(
                reply_id=1,
                replied_by_id=2,
                reply_content="reply_content",
                replied_at="29-07-2020"
            ),
            ReplyDto(
                reply_id=2,
                replied_by_id=2,
                reply_content="reply_content",
                replied_at="30-07-2020"
            )

        ]
        post_reactions_ids_dtos = [
            PostReactionDto(
                post_id=1,
                reaction_id=1
            ),
            PostReactionDto(
                post_id=1,
                reaction_id=2
            ),
            PostReactionDto(
                post_id=2,
                reaction_id=3
            ),
            PostReactionDto(
                post_id=2,
                reaction_id=4
            )
        ]
        reaction_ids = [
            post_reaction.reaction_id
            for post_reaction in post_reactions_ids_dtos
        ]
        reaction_dtos = [
            ReactionDto(
                reaction_id=1,
                reacted_by_id=4,
                reacted_at="01-08-2020"
            ),
            ReactionDto(
                reaction_id=2,
                reacted_by_id=5,
                reacted_at="01-08-2020"
            ),
            ReactionDto(
                reaction_id=3,
                reacted_by_id=6,
                reacted_at="01-08-2020"
            ),
            ReactionDto(
                reaction_id=1,
                reacted_by_id=7,
                reacted_at="01-08-2020"
            )
        ]
        post_answer_ids_dtos = [
            PostAnswerDto(
                post_id=1,
                answer_id=1
            ),
            PostAnswerDto(
                post_id=2,
                answer_id=2
            )
        ]

        interactor = GetPost(
            post_storage=post_storage
        )

        post_storage.validate_post_ids \
            .return_value = True
        post_storage.get_basic_post_details \
            .return_value = post_dtos
        post_storage.get_post_tag_ids \
            .return_value = post_tag_ids_dtos
        post_storage.get_tag_dtos \
            .return_value = tag_dtos
        post_storage.get_post_comment_ids_sort_by_date \
            .return_value = post_comment_ids_dtos
        post_storage.get_comment_dtos \
            .return_value = comment_dtos
        post_storage.get_comment_reply_ids_dtos \
            .return_value = comment_reply_ids_dto
        post_storage.get_reply_dtos \
            .return_value = reply_dtos
        post_storage.get_post_reactions_ids_dtos \
            .return_value = post_reactions_ids_dtos
        post_storage.get_reaction_dtos \
            .return_value = reaction_dtos
        post_storage.get_post_answer_ids_dtos \
            .return_value = post_answer_ids_dtos



        # Act
        response = interactor.get_posts_wrapper(
            post_ids=post_ids,
            post_presenter=post_presenter
        )


        # Assert
        post_storage.validate_post_ids \
            .assert_called_once_with(post_ids=post_ids)
        post_storage.get_basic_post_details \
            .assert_called_once_with(post_ids=post_ids)
        post_storage.get_post_tag_ids \
            .assert_called_once_with(post_ids=post_ids)
        post_storage.get_tag_dtos \
            .assert_called_once_with(tag_ids=tag_ids)
        post_storage.get_post_comment_ids_sort_by_date \
            .assert_called_once_with(post_ids=post_ids)
        post_storage.get_comment_dtos \
            .assert_called_once_with(comment_ids=comment_ids)
        post_storage.get_reply_dtos \
            .assert_called_once_with(reply_ids=reply_ids)
        post_storage.get_post_reactions_ids_dtos \
            .assert_called_once_with(post_ids=post_ids)
        post_storage.get_reaction_dtos \
            .assert_called_once_with(reaction_ids=reaction_ids)
        post_storage.get_post_answer_ids_dtos \
            .assert_called_once_with(post_ids=post_ids)