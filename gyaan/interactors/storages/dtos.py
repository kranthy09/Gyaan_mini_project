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