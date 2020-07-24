import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from common.oauth2_storage import OAuth2SQLStorage
from user_app.storages.storage_implementation \
        import StorageImplementation
from user_app.presenters.presenter_implementation \
        import PresenterImplementation
from user_app.interactors.login_interactor \
        import LoginInteractor



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    username = kwargs['request_data']['username']
    password = kwargs['request_data']['password']

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()

    interactor = LoginInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage
    )

    response = interactor.login_wrapper(username=username,
                                    password=password,
                                    presenter=presenter)
    return response