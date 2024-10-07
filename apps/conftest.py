import pytest
from graphene.test import Client

from apps.core.schema import schema


@pytest.fixture
def graphql_client():
    return Client(schema)
