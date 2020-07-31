import json
from django.http import HttpResponse, response
from user_app.interactors.presenters.presenter_interface \
        import PresenterInterface
from user_app.constants.custom_messages \
    import (invalid_username,
            invalid_password)
from user_app.interactors.storages.dtos \
    import TokenDto


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_username(self) \
            -> HttpResponse:
        response_msg = invalid_username[1]
        status_code = 404
        res_status = invalid_username[0]

        data = json.dumps(
            {
                "response": response_msg,
                "http_response_code": status_code,
                "res_status": res_status
            }
        )
        response_data = response.HttpResponse(data, status=404)

        return response_data

    def raise_exception_for_invalid_password(self) \
            -> HttpResponse:
        response_msg = invalid_password[1]
        status_code = 404
        res_status = invalid_password[0]

        data = json.dumps(
            {
                "response": response_msg,
                "http_response_code": status_code,
                "res_status": res_status
            }
        )
        response_data = response.HttpResponse(data, status=404)

        return response_data

    def get_response_for_login(self, token_dto: TokenDto) \
            -> HttpResponse:

        data = json.dumps(
            {
                "user_id": token_dto.user_id,
                "access_token": token_dto.access_token,
                "user_role": token_dto.user_role
            }
        )

        response_data = response.HttpResponse(data, status=201)
        return response_data
