from dataclasses import dataclass
from gyaan.adapters.dtos \
    import UserDetailsDto
from typing import List


@dataclass
class DomainDto:
    domain_id: int
    domain_name: str


@dataclass
class DomainWithPostsCount:
    domain_id: int
    domain_name: str
    posts_count: int


@dataclass
class DomainMetrics:
    domains: List[DomainWithPostsCount]
    total_posts: int


@dataclass
class UserDomainsDetails:
    user_details: UserDetailsDto
    user_following_domains: List[DomainDto]
    suggested_domains: List[DomainDto]
    user_domains_posts: DomainMetrics
    user_pending_domain_posts: DomainMetrics
    domain_requests: List[UserDetailsDto]
    domain_expert_pendings: List[DomainDto]


@dataclass
class PostDto:
    post_id: int
    post_title: str
    post_content: str
    posted_at: str
    post_comments_count: int


@dataclass
class PostTag:
    post_id: int
    tag_id: int


@dataclass
class TagDto:
    tag_id: int
    tag_name: str


@dataclass
class PostComment:
    post_id: int
    comment_id: int


@dataclass
class CommentDto:
    comment_id: int
    comment_content: str
    commented_at: str
    commented_by_id: int


@dataclass
class ReplyDto:
    reply_id: int
    replied_by_id: int
    reply_content: str
    replied_at: str


@dataclass
class CommentReplyDto:
    comment_id: int
    reply_id: int


@dataclass
class PostReactionDto:
    post_id: int
    reaction_id: int


@dataclass
class ReactionDto:
    reaction_id: int
    reacted_by_id: int
    reacted_at: str


@dataclass
class PostReactionWithCountUser:
    reactions_count: int
    reacted_by: List[UserDetailsDto]


@dataclass
class PostAnswerDto:
    post_id: int
    answer_id: int


@dataclass
class AnswerDto:
    answer_id: int
    answer_content: str
    answered_at: str
    answered_by_id: int
    approved_by_id: int


@dataclass
class PostUserDto:
    post_id: int
    user_id: int