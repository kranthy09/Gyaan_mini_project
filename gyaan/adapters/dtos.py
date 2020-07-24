from dataclasses import dataclass
from user_app.constants.enums \
    import UserRoles


@dataclass
class UserDetailsDto:
    user_id: int
    username: str
    name: str
    profile_pic: str
    role: UserRoles