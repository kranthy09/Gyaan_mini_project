import factory, factory.fuzzy
import datetime
from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.sequence(lambda n: "username %02d" % n)
    password = factory.sequence(lambda n: "password %02d" % n)
    user_role = factory.fuzzy.FuzzyChoice(User.ROLE_CHOICES, getter=lambda c: c[0])
    name = factory.sequence(lambda n: "name %02d" % n)
    profile_pic = factory.sequence(lambda n: "profilePic %02d" % n)
    date_joined = factory.LazyFunction(datetime.datetime.now)
