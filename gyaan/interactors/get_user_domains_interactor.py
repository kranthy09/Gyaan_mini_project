from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface
from gyaan.interactors.storages.dtos \
    import (DomainDto,
            DomainMetrics,
            DomainWithPostsCount,
            UserDomainsDetails)
from gyaan.adapters.dtos import UserDetailsDto
from typing import List, Tuple


class GetUserDomainsInteractor:

    def __init__(self, domain_storage: DomainStorageInterface):
        self.domain_storage = domain_storage

    def get_user_domains_wrapper(self, user_id: int,
                                 domain_presenter: DomainPresenterInterface):
        user_domains_details_dto = self.get_user_domains(user_id=user_id)

        response = domain_presenter.get_response_for_user_domains(user_domains_details_dto=user_domains_details_dto)

    def get_user_domains(self, user_id: int):

        from gyaan.adapters.userapp_adapter \
            import UserAppAdapter

        user_adapter = UserAppAdapter()
        user_ids = [user_id]
        user_details_dto = user_adapter.get_user_details_dto(user_ids=user_ids)
        user_following_domain_ids = \
            self.domain_storage.get_user_following_domain_ids(user_id=user_id)
        all_domains_dtos = \
            self.domain_storage.get_all_domains_dtos()
        user_following_domain_dtos, user_suggested_domain_dtos = \
            self._get_user_following_and_suggested_domains(
                domain_ids=user_following_domain_ids,
                domain_dtos=all_domains_dtos
            )
        user_posts_with_domain, user_pending_posts_with_domain = \
            self._get_user_approved_pending_posts_with_domains(
                user_id=user_id
            )
        is_user_domain_expert = self.domain_storage.is_user_domain_expert(
            user_id=user_id
        )
        if is_user_domain_expert:
            domain_requests_details, expert_approval_posts_with_domains = \
                self._get_domain_requests_approval_posts(
                    domain_expert_id=user_id
                )
        else:
            domain_requests_details = []
            expert_approval_posts_with_domains = []
        user_domains_details_dto = \
            UserDomainsDetails(
                user_details=user_details_dto,
                user_following_domains=user_following_domain_dtos,
                suggested_domains=user_suggested_domain_dtos,
                user_domains_posts=user_posts_with_domain,
                user_pending_domain_posts=user_pending_posts_with_domain,
                domain_requests=domain_requests_details,
                domain_expert_pendings=expert_approval_posts_with_domains
            )
        return user_domains_details_dto

    def _get_user_following_and_suggested_domains(
            self,
            domain_ids: List[int],
            domain_dtos: List[DomainDto]
    ) -> Tuple[List[DomainDto], List[DomainDto]]:

        user_following_domains_dtos = []
        user_suggested_domains_dtos = []
        for domain_dto in domain_dtos:
            is_user_follows_domain = domain_dto.domain_id in domain_ids
            if is_user_follows_domain:
                user_following_domains_dtos.append(domain_dto)
            else:
                user_suggested_domains_dtos.append(domain_dto)
        return user_following_domains_dtos, user_suggested_domains_dtos

    def _get_user_approved_pending_posts_with_domains(self, user_id: int) \
            -> Tuple[DomainMetrics, DomainMetrics]:

        user_posts_with_domain = \
            self.domain_storage.get_user_posts_with_domain(
                user_id=user_id
            )
        user_pending_posts_with_domain = \
            self.domain_storage.get_user_pending_posts_with_domain(
                user_id=user_id
            )
        return user_posts_with_domain, user_pending_posts_with_domain

    def _get_domain_requests_approval_posts(self, domain_expert_id: int) \
            -> Tuple[List[UserDetailsDto], List[DomainWithPostsCount]]:

        expert_domain_ids = \
            self.domain_storage.get_domain_expert_domain_ids(
                domain_expert_id=domain_expert_id
            )
        domain_requests_ids = self.domain_storage.get_domain_requests_ids(
            domain_ids=expert_domain_ids
        )

        from gyaan.adapters.userapp_adapter \
            import UserAppAdapter

        user_adapter = UserAppAdapter()
        domain_requests_details = \
            user_adapter.get_user_details_dto(user_ids=domain_requests_ids)

        expert_approval_posts_dtos = \
            self.domain_storage.get_domain_expert_approval_posts(
                domain_expert_id=domain_expert_id
            )
        return domain_requests_details, expert_approval_posts_dtos
