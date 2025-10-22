from http import HTTPStatus
from fastapi.testclient import TestClient
from fastapi_zero.app import app


def teste_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Executa a coisa (o SUT)
    - A: Assert - Garante que A é A
    """

    #  Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Asset
    assert response.json() == {'nessage': 'olá mundo'}
    assert response.status_code == HTTPStatus.OK
