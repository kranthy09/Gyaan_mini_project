from unittest.mock import create_autospec
from user_app.constants.enums import UserRoles
from user_app.interactors.storages.storage_interface \
    import StorageInterface
from user_app.interactors.presenters.presenter_interface \
    import PresenterInterface
from user_app.interactors.get_user_details_interactor \
    import UserDetailsInteractor
from user_app.interactors.storages.dtos \
    import (UserDetailsDto,
            UserDetailsDtoList)


class TestUserDetailsInteractor:

    def test_user_details_interactor(self):

        # Arrange
        user_ids = [1, 2]
        user_details_dtos = [
                UserDetailsDto(
                    user_id=1,
                    user_name="monty",
                    name="shubham monty",
                    profile_pic="my_pic.com",
                    role=UserRoles.USER
            ),
            UserDetailsDto(
                user_id=2,
                user_name="jasper",
                name="Siddarth kumar",
                profile_pic="my_pic_2.com",
                role=UserRoles.DOMAIN_EXPERT
            )
        ]
        test_user_details_dtos_list = UserDetailsDtoList(
            user_details_dtos=user_details_dtos
        )


        storage = create_autospec(StorageInterface)
        # presenter = create_autospec(PresenterInterface)

        interactor = UserDetailsInteractor(storage=storage)

        storage.get_user_details.return_value = test_user_details_dtos_list

        # Act
        user_details_dto_list = interactor.get_user_details_dtos(user_ids=user_ids)

        # Assert
        storage.get_user_details \
            .assert_called_once_with(user_ids=user_ids)
        assert user_details_dto_list == test_user_details_dtos_list