from unittest.mock import create_autospec, patch
from gyaan.adapters.dtos import UserDetailsDto
from gyaan.interactors.storages.dtos \
    import (DomainDto,
            DomainMetrics,
            DomainWithPostsCount)
from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface
from gyaan.interactors.get_user_domains_interactor \
    import GetUserDomainsInteractor


class TestGetUserDomainsInteractor:

    @patch('gyaan.adapters.userapp_adapter.UserAppAdapter.get_user_details_dto')
    def test_get_user_domains_interactor(self, get_user_details_dto):
        # Arrange
        user_id = 1
        user_details_dto = \
            UserDetailsDto(
                user_id=1,
                username="kranthi",
                name="skywalker",
                profile_pic="profile_pic.com",
                role="USER"
            )
        user_following_domain_ids = [1, 2]
        all_domains_dtos = [
            DomainDto(
                domain_id=1,
                domain_name="Python"
            ),
            DomainDto(
                domain_id=2,
                domain_name="React"
            ),
            DomainDto(
                domain_id=3,
                domain_name="GoLang"
            )
        ]
        user_domains_with_posts_count = [
            DomainWithPostsCount(
                domain_id=1,
                domain_name="Python",
                posts_count=2
            ),
            DomainWithPostsCount(
                domain_id=2,
                domain_name="React",
                posts_count=1
            )
        ]
        user_posts_with_domain = [
            DomainMetrics(
                total_posts=3,
                domain=user_domains_with_posts_count
            )
        ]
        user_domains_with_pending_posts_count = [
            DomainWithPostsCount(
                domain_id=2,
                domain_name="React",
                posts_count=1
            )
        ]
        user_pending_posts_with_domain = [
            DomainMetrics(
                total_posts=1,
                domain=user_domains_with_pending_posts_count
            )
        ]

        domain_storage = create_autospec(DomainStorageInterface)
        domain_presenter = create_autospec(DomainPresenterInterface)

        interactor = GetUserDomainsInteractor(
            domain_storage=domain_storage
        )

        get_user_details_dto.return_value = user_details_dto
        domain_storage.get_user_following_domain_ids \
            .return_value = user_following_domain_ids
        domain_storage.get_all_domains_dtos \
            .return_value = all_domains_dtos
        domain_storage.get_user_posts_with_domain \
            .return_value = user_posts_with_domain
        domain_storage.get_user_pending_posts_with_domain \
            .return_value = user_pending_posts_with_domain
        domain_storage.is_user_domain_expert \
            .return_value = False

        # Act
        interactor.get_user_domains_wrapper(
            user_id=user_id,
            domain_presenter=domain_presenter
        )

        # Assert
        domain_storage.get_user_following_domain_ids \
            .assert_called_once_with(user_id=user_id)
        domain_storage.get_all_domains_dtos \
            .assert_called_once()
        domain_storage.get_user_posts_with_domain \
            .assert_called_once_with(user_id=user_id)
        domain_storage.get_user_pending_posts_with_domain \
            .assert_called_once_with(user_id=user_id)
        domain_storage.is_user_domain_expert \
            .assert_called_once_with(user_id=user_id)

    @patch('gyaan.adapters.userapp_adapter.UserAppAdapter.get_user_details_dto')
    def test_get_user_domains_interactor_with_expert(self, get_user_details_dto):

        # Arrange
        user_id = 1
        user_details_dto = \
            UserDetailsDto(
                user_id=1,
                username="kranthi",
                name="skywalker",
                profile_pic="profile_pic.com",
                role="USER"
            )
        user_following_domain_ids = [1, 2]
        all_domains_dtos = [
            DomainDto(
                domain_id=1,
                domain_name="Python"
            ),
            DomainDto(
                domain_id=2,
                domain_name="React"
            ),
            DomainDto(
                domain_id=3,
                domain_name="GoLang"
            )
        ]
        user_domains_with_posts_count = [
            DomainWithPostsCount(
                domain_id=1,
                domain_name="Python",
                posts_count=2
            ),
            DomainWithPostsCount(
                domain_id=2,
                domain_name="React",
                posts_count=1
            )
        ]
        user_posts_with_domain = [
            DomainMetrics(
                total_posts=3,
                domain=user_domains_with_posts_count
            )
        ]
        user_domains_with_pending_posts_count = [
            DomainWithPostsCount(
                domain_id=2,
                domain_name="React",
                posts_count=1
            )
        ]
        user_pending_posts_with_domain = [
            DomainMetrics(
                total_posts=1,
                domain=user_domains_with_pending_posts_count
            )
        ]
        expert_domain_ids = [1, 2]
        domain_request_ids = [3, 4]
        expert_approval_posts_dtos = [
            DomainWithPostsCount(
                domain_id=1,
                domain_name="Python",
                posts_count=2
            )
        ]

        domain_storage = create_autospec(DomainStorageInterface)
        domain_presenter = create_autospec(DomainPresenterInterface)

        interactor = GetUserDomainsInteractor(
            domain_storage=domain_storage
        )

        get_user_details_dto.return_value = user_details_dto
        domain_storage.get_user_following_domain_ids \
            .return_value = user_following_domain_ids
        domain_storage.get_all_domains_dtos \
            .return_value = all_domains_dtos
        domain_storage.get_user_posts_with_domain \
            .return_value = user_posts_with_domain
        domain_storage.get_user_pending_posts_with_domain \
            .return_value = user_pending_posts_with_domain
        domain_storage.is_user_domain_expert \
            .return_value = True
        domain_storage.get_domain_expert_domain_ids \
            .return_value = expert_domain_ids
        domain_storage.get_domain_requests_ids \
            .return_value = domain_request_ids
        domain_storage.get_domain_expert_approval_posts \
            .return_value = expert_approval_posts_dtos


        # Act
        interactor.get_user_domains_wrapper(
            user_id=user_id,
            domain_presenter=domain_presenter
        )

        # Assert
        domain_storage.get_user_following_domain_ids \
            .assert_called_once_with(user_id=user_id)
        domain_storage.get_all_domains_dtos \
            .assert_called_once()
        domain_storage.get_user_posts_with_domain \
            .assert_called_once_with(user_id=user_id)
        domain_storage.get_user_pending_posts_with_domain \
            .assert_called_once_with(user_id=user_id)
        domain_storage.get_domain_expert_domain_ids \
            .assert_called_once_with(domain_expert_id=user_id)
        domain_storage.get_domain_requests_ids \
            .assert_called_once_with(domain_ids=expert_domain_ids)
        domain_storage.get_domain_expert_approval_posts \
            .assert_called_once_with(domain_expert_id=user_id)
