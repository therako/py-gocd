import pytest
import vcr

from gocd.server import Server


@pytest.fixture
def server():
    return Server('http://localhost:8153', user='ba', password='secret')


auth_test_cassettes = [
    'tests/fixtures/cassettes/server-basic-auth.yml',
    'tests/fixtures/cassettes/server-without-auth.yml',
]


@pytest.mark.parametrize("cassette_name", auth_test_cassettes)
def test_request_with_and_without_auth(server, cassette_name):
    with vcr.use_cassette(cassette_name) as cass:
        response = server.get('go/api/pipelines/Simple/history/0')

    assert response.code == 200
    assert response.headers.type == 'application/json'
