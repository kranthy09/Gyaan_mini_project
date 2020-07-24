from django.db.models import Count
from gyaan.interactors.storages.dtos \
    import (DomainDto,
            DomainMetrics,
            DomainWithPostsCount)
from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from typing import List, Dict
from gyaan.models.domain import (Domain,
                                 DomainPost,
                                 DomainRequests,
                                 DomainExperts)


class DomainStorageImplementation(DomainStorageInterface):

    def get_user_following_domain_ids(self, user_id: int) \
            -> List[int]:
        user_following_domain_ids = \
            DomainRequests.objects.filter(
                requested_by=user_id,
                is_approved=True).values_list('id', flat=True)
        return user_following_domain_ids

    def get_all_domains_dtos(self) -> List[DomainDto]:
        domains = Domain.objects.all()
        all_domains_dtos = []
        for domain in domains:
            all_domains_dtos.append(
                DomainDto(
                    domain_id=domain.id,
                    domain_name=domain.domain_name
                )
            )
        return all_domains_dtos

    def get_user_posts_with_domain(self, user_id: int) \
            -> DomainMetrics:
        domains = DomainPost.objects.filter(is_approved=True, user_id=user_id) \
                    .values('domain_id', 'domain__domain_name') \
                    .annotate(count=Count('post_id'))
        user_posts_with_domain_dtos = self._convert_to_domain_metrics_dto(domains)
        return user_posts_with_domain_dtos

    def get_user_pending_posts_with_domain(self, user_id: int) \
            -> DomainMetrics:

        domains = list(DomainPost.objects.filter(is_approved=False, user_id=user_id) \
            .values('domain_id', 'domain__domain_name') \
            .annotate(count=Count('post_id')))
        user_posts_with_pending_domain_dtos = self._convert_to_domain_metrics_dto(domains)
        return user_posts_with_pending_domain_dtos

    def is_user_domain_expert(self, user_id: int) -> bool:

        is_domain_expert = \
            DomainExperts.objects.filter(user_id=user_id).exists()
        return is_domain_expert

    def get_domain_expert_domain_ids(self, domain_expert_id: int) \
            -> List[int]:
        pass

    def get_domain_requests_ids(self, domain_ids: List[int]) \
            -> List[int]:
        pass

    def get_domain_expert_approval_posts(self, domain_expert_id: int) \
            -> List[DomainDto]:
        pass

    @staticmethod
    def _convert_to_domain_metrics_dto(domains: List[Dict[int, str, int]]) \
            -> DomainMetrics:

        user_posts_with_domain_dtos = []
        total_posts = 0
        for domain in domains:
            user_posts_with_domain_dtos.append(
                DomainWithPostsCount(
                    domain_id=domain['domain_id'],
                    domain_name=domain['domain_name'],
                    posts_count=domain['count']
                )
            )
            total_posts += domain['count']
        domain_metrics = DomainMetrics(
            domains=user_posts_with_domain_dtos,
            total_posts=total_posts
        )
        return domain_metrics
