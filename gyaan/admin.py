# your django admin
from django.contrib import admin
from gyaan.models.domain \
    import (Domain,
            DomainRequests,
            DomainTag,
            DomainPost,
            DomainExperts)

admin.site.register(Domain)
admin.site.register(DomainRequests)
admin.site.register(DomainTag)
admin.site.register(DomainPost)
admin.site.register(DomainExperts)