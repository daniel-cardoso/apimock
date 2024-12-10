import pytest
from unittest.mock import MagicMock
from repositories.viacep_repository import ViacepRepository
from services.viacep_service import ViacepService
from views.viacep_view import ViacepView
from typing import Dict


@pytest.fixture
def mock_viacep_repository() -> MagicMock:
    mock_repository:MagicMock = MagicMock(spec=ViacepRepository)
    '''mock_repository..return_values = {
        "cep": "04812-060",
        "logradouro": "Rua Félix Caetano",
        "complemento": "",
        "unidade": "",
        "bairro": "Jardim Ana Lúcia",
        "localidade": "São Paulo",
        "uf": "SP",
        "estado": "São Paulo",
        "regiao": "Sudeste",
        "ibge": "3550308",
        "gia": "1004",
        "ddd": "11",
        "siafi": "7107",
    }'''
    return mock_repository


@pytest.fixture
def mock_viacep_service(mock_viacep_repository:MagicMock)-> MagicMock:
    mock_service:MagicMock = MagicMock(spec=ViacepService)
    mock_service.get_address_viacep_service.return_value = mock_viacep_repository
    return mock_service


@pytest.fixture
def create_view(mock_viacep_service:MagicMock)-> ViacepView:
    mock_view:ViacepView = ViacepView(mock_viacep_service)
    return mock_view
