from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from gyaan.storages.domain_storage_implementation \
    import DomainStorageImplementation
from gyaan.presenters.domain_presenter_implementation \
    import JsonPresenter
from gyaan.interactors.get_user_domains_interactor \
    import GetUserDomainsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_id = kwargs['user_dto'].user_id

    domain_storage = DomainStorageImplementation()
    domain_presenter = JsonPresenter()

    interactor = GetUserDomainsInteractor(domain_storage=domain_storage)

    response = interactor.get_user_domains_wrapper(user_id=user_id,
                                                   domain_presenter=domain_presenter)
    return response
