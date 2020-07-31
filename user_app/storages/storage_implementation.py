from user_app.exceptions.exceptions \
        import (InvalidUsername,
                InvalidPassword)
from user_app.interactors.storages.dtos \
        import (UserRoleDto,
                UserDetailsDto)
from user_app.interactors.storages.storage_interface \
        import StorageInterface
from user_app.models.models import User
from typing import List


class StorageImplementation(StorageInterface):

    def validate_username(self, username: str):

        is_username_does_not_exists = not User.objects.filter(username=username)
        if is_username_does_not_exists:
            raise InvalidUsername
        return True

    def validate_password(self, username: str, password: str):

        user = User.objects.get(username=username)

        is_not_valid_password = not user.check_password(raw_password=password)

        if is_not_valid_password:
            raise InvalidPassword
        return True

    def get_user_role_dto(self, username: str, password: str) \
            -> UserRoleDto:

        user = User.objects.get(username=username, password=password)

        return UserRoleDto(
            user_id=user.id,
            user_role=user.user_role
        )

    def get_user_details(self, user_ids: List[int]) -> List[UserDetailsDto]:

        users = User.objects.filter(id__in=user_ids)
        user_details_dto_list = []
        for user in users:
            user_details_dto = UserDetailsDto(
                user_id=user.id,
                user_name=user.username,
                name=user.name,
                profile_pic=user.profile_pic,
                role=user.user_role
            )
            user_details_dto_list.append(user_details_dto)

        return user_details_dto_list
