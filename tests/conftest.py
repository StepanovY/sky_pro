from pytest_factoryboy import register

from tests.factories import UserFactory, ResumeFactory

pytest_plugins = 'tests.fixtures'

register(UserFactory)
register(ResumeFactory)
