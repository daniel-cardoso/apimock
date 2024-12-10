from dataclasses import dataclass

@dataclass
class Address:
    cep : str
    logradouro : str
    complemento : str
    unidade : str
    bairro : str
    localidade : str
    uf : str
    estado : str
    regiao : str
    ibge : str
    gia : str
    ddd : str
    siafi : str
    
