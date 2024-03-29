import factory, factory.fuzzy
from .domain import (Domain,
                     DomainExperts,
                     DomainRequests,
                     DomainPost,
                     DomainTag)
from user_app.models.factory import UserFactory


class DomainFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Domain

    domain_name = factory.sequence(lambda n: "domain_name %02d" % n)
    domain_description = factory.sequence(lambda n: "domain_description %02d" % n)


class DomainExpertsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DomainExperts

    domain = factory.Iterator(Domain.objects.all())
    domain_expert_id = factory.Iterator([1,2,3])


class DomainRequestsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DomainRequests

    domain = factory.Iterator(Domain.objects.all())
    requested_by = factory.Iterator([4, 5, 6, 7, 8, 9])
    is_approved = factory.fuzzy.FuzzyChoice([True, False])


class DomainPostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DomainPost

    user_id = factory.Iterator([4, 5, 6, 7, 8, 9])
    post_id = factory.fuzzy.FuzzyInteger(1,10)
    domain = factory.Iterator(Domain.objects.all())
    is_approved = factory.fuzzy.FuzzyChoice([True, False])


class DomainTagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DomainTag

    domain = factory.Iterator(Domain.objects.all())
    tag_id = factory.fuzzy.FuzzyInteger(1, 100)