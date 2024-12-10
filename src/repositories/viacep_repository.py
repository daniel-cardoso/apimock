# from models.address import Address
from typing import Dict
import requests


class ViacepRepository:
    BASE_URL = "https://viacep.com.br/ws"

    def get_address_viacep_repository(self, cep: str) -> Dict[str, str]:
        response = requests.get(f"{self.BASE_URL}/{cep}/json")
        response.raise_for_status()  # para caso de alguma falha no http

        return response.json()
