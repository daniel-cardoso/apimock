import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from fixtures import create_view
from typing import Dict


teste=create_view()

@pytest.fixture
def client(create_view):
    app = create_view.app
    return TestClient(app)

@pytest.fixture
def data_test():
    return{
        "cep_valid":"04812060",
        "cep_invalid":"00",
        "cep_notfound_or_non_existent":"12345678"
    }



def test_get_viacep_success(client, data_test):
    # Arrange: Definindo um CEP válido
    cep = data_test['cep_valid']
    
    # Act: Fazendo a requisição GET
    response = client.get(f"/cep/{cep}")
    
    # Assert: Verificando se o retorno é o esperado
    assert response.status_code == 200
    assert response.json() == {
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
    }


