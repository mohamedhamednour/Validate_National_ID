import factory
from faker import Faker
from .models import NationalID

faker = Faker()

class NationalIDFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NationalID

    number = factory.LazyAttribute(lambda _: faker.unique.random_number(digits=14, fix_len=True))
    birth_date = factory.Faker('date_of_birth')
    location = factory.Faker('city')
