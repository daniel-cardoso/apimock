from repositories.viacep_repository import ViacepRepository
from typing import Dict

class ViacepService:

    def __init__(self, repo:ViacepRepository):
        self.__viacep_repo = repo
    
    def get_address_viacep_service(self,cep:str) -> Dict[str,str]:
        if len(cep) != 8 or not cep.isdigit():
            raise ValueError("CEP must contain 8 numeric digits.")

        address:Dict[str,str] = self.__viacep_repo.get_address_viacep_repository(cep)

        if "erro" in address:
            raise ValueError("CEP not found or doesn't exist.")

        return address