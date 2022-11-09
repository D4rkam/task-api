from fastapi import FastAPI
from routes import taskRoutes

app = FastAPI()

app.include_router(router = taskRoutes.router)



#pip install -r requirements.txt --> dependecias de la api




