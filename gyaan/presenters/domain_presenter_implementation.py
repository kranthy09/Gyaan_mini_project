from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface
from gyaan.interactors.storages.dtos import UserDomainsDetails


class JsonPresenter(DomainPresenterInterface, HTTPResponseMixin):

    def get_response_for_user_domains(
            self,
            user_domains_details_dto: UserDomainsDetails):
        user_dto = user_domains_details_dto.user_details[0]
        user_details = {
            "user_id": user_dto.user_id,
            "name": user_dto.name,
            "profile_pic": user_dto.profile_pic,
            "username": user_dto.user_name,
            "role": user_dto.role
        }
        user_following_domains = []
        for domain_dto in user_domains_details_dto.user_following_domains:
            user_following_domains.append(
                {
                    "domain_id": domain_dto.domain_id,
                    "domain_name": domain_dto.domain_name
                }
            )
        suggested_domains = []
        for domain_dto in user_domains_details_dto.suggested_domains:
            suggested_domains.append(
                {
                    "domain_id": domain_dto.domain_id,
                    "domain_name": domain_dto.domain_name
                }
            )
        user_domains = []
        for domain_metric in user_domains_details_dto.user_domains_posts.domains:
            user_domains.append(
                {
                    "domain_id": domain_metric.domain_id,
                    "domain_name": domain_metric.domain_name,
                    "posts_count": domain_metric.posts_count
                }
            )
        user_domains_posts = {
            "total_posts": user_domains_details_dto.user_domains_posts.total_posts,
            "domains": user_domains
        }
        user_pending_domains = []
        for domain_metric in user_domains_details_dto.user_pending_domain_posts.domains:
            user_pending_domains.append(
                {
                    "domain_id": domain_metric.domain_id,
                    "domain_name": domain_metric.domain_name,
                    "posts_count": domain_metric.posts_count
                }
            )
        user_pending_domain_posts = {
            "total_pending_posts": user_domains_details_dto.user_pending_domain_posts.total_posts,
            "domains": user_pending_domains
        }
        domain_requests = []
        for domain_request in user_domains_details_dto.domain_requests:
            domain_requests.append(
                {
                    "user_id": domain_request.user_id,
                    "name": domain_request.name,
                    "profile_pic": domain_request.profile_pic,
                    "username": domain_request.user_name,
                    "role": domain_request.role
                }
            )
        domain_expert_pendings = []
        for expert_pending in user_domains_details_dto.domain_expert_pendings:
            domain_expert_pendings.append(
                {
                    "domain_id": expert_pending.domain_id,
                    "domain_name": expert_pending.domain_name
                }
            )
        response = {
            "user_details": user_details,
            "user_following_domains": user_following_domains,
            "suggested_domains": suggested_domains,
            "user_domains_posts": user_domains_posts,
            "user_pending_domain_posts": user_pending_domain_posts,
            "domain_requests": domain_requests,
            "domain_expert_pendings": domain_expert_pendings
        }
        return self.prepare_201_created_response(response_dict=response)
