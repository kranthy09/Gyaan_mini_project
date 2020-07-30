from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface
from gyaan.interactors.storages.dtos import UserDomainsDetails


class JsonPresenter(DomainPresenterInterface, HTTPResponseMixin):

    def get_response_for_user_domains(
            self,
            user_domains_details_dto: UserDomainsDetails):
        response = {
            "user_details": user_domains_details_dto.user_details,
            "user_following_domains": user_domains_details_dto.user_following_domains,
            "suggested_domains": user_domains_details_dto.suggested_domains,
            "user_domains_posts": user_domains_details_dto.user_domains_posts,
            "user_pending_domain_posts": user_domains_details_dto.user_pending_domain_posts,
            "domain_requests": user_domains_details_dto.domain_requests,
            "domain_expert_pendings": user_domains_details_dto.domain_expert_pendings
        }
        return self.prepare_201_created_response(response_dict=response)
