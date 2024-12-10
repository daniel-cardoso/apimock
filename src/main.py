from fastapi import FastAPI
from repositories.viacep_repository import ViacepRepository
from services.viacep_service import ViacepService
from views.viacep_view import ViacepView

app = FastAPI(
        title="Viacep external api consumer", description="external calls to viacep api"
    )

viacep_repository = ViacepRepository()
viacep_service = ViacepService(viacep_repository)
viacep_view = ViacepView(viacep_service)

app.include_router(viacep_view.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to API ViaCEP!"}

if __name__ == "__main__":
   import uvicorn
   uvicorn.run("main:app", reload=True) 
