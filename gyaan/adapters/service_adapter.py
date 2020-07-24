from ib_common.service_adapter_utils.base_adapter_class import BaseAdapterClass


class ServiceAdapter(BaseAdapterClass):
    def __init__(self, *args, **kwargs):
        from django.conf import settings
        source = settings.IB_MINIPROJECTS_BACKEND_SOURCE
        kwargs['source'] = source
        super(ServiceAdapter, self).__init__(*args, **kwargs)
