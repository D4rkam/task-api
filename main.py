from fastapi import FastAPI

from routes import apiTaskRoutes

app = FastAPI()

app.include_router(router = apiTaskRoutes.router)



#pip install -r requirements.txt --> dependecias de la api




