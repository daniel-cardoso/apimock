from views.viacep_view import get_address_viacep
import pytest

@pytest.fixture
def data_test():
    return{
        "cep_valid":"04812060",
        "cep_invalid":"00",
        "cep_notfound_or_non_existent":"12345678"
    }

def test_get_viacep_success(data_test):
    #arrange
    cep=data_test['cep_valid']

    #act
    result = get_address_viacep(cep)

    #assert
    assert result['logradouro'] == "Rua Félix Caetano"


def test_get_viacep_not_found(cep:str):
    # 200 mas nao localizado
    pass

def test_get_viacep_invalid(cep:str):
    # cep fora de estrutura
    pass
