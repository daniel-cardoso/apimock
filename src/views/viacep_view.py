from services.viacep_service import ViacepService
from typing import Dict
from fastapi import APIRouter, HTTPException


class ViacepView:
    def __init__(self, service: ViacepService):
        self.__viacep_service = service
        self.router = APIRouter()
        self.setup_routes()

    def setup_routes(self):
        @self.router.get("/cep/{cep}")
        def get_address_viacep(cep: str) -> Dict[str, str]:
            try:
                return self.__viacep_service.get_address_viacep_service(cep)
            except ValueError as error:
                raise HTTPException(status_code=400, detail=str(error))
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")
