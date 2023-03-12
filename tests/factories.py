import factory
from django.contrib.auth.models import User

from resume.models import Resume


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = factory.Faker('password')

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class ResumeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Resume

    status = 1
    grade = '1'
    specialty = 'python'
    education = 'education'
    experience = 'experience'
    title = factory.Faker('sentence', nb_words=3)
    email = 'email'
    author = factory.SubFactory(UserFactory)
