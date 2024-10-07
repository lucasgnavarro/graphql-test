import factory

from apps.admission.models import AdmissionProcess


class AdmissionProcessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AdmissionProcess

    id = factory.Sequence(lambda n: f"AP{n}")
    name = factory.Faker('company')
    subtitle = factory.Faker('catch_phrase')
    short_name_admin = factory.Faker('word')
    short_name_display = factory.Faker('word')
    application_target_type = factory.Iterator(['SCHOOL', 'PROGRAM'])
    display_in_public_school_directory = factory.Faker('boolean')


__all__ = ('AdmissionProcessFactory', )
