from typing import List


class UserAppAdapter:

    @property
    def service_interface(self):
        from user_app.interfaces.service_interface \
            import ServiceInterface
        return ServiceInterface()

    def get_user_details_dto(self, user_ids: List[int]):
        from user_app.interfaces.service_interface \
            import ServiceInterface
        service_interface = ServiceInterface()
        user_details_dtos = \
            service_interface.get_user_details_dtos(user_ids=user_ids)
        return user_details_dtos
