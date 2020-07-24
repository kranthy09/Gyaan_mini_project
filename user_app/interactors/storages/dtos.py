from dataclasses import dataclass
from user_app.constants.enums import UserRoles
from typing import List


@dataclass
class UserRoleDto:
    user_id: int
    user_role: UserRoles

@dataclass
class TokenDto:
    user_id: int
    access_token: str
    user_role: UserRoles

@dataclass
class UserDetailsDto:
    user_id: int
    user_name: str
    name: str
    profile_pic: str
    role: UserRoles

@dataclass
class UserDetailsDtoList:
    user_details_dtos: List[UserDetailsDto]