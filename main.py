from fastapi import FastAPI
from routes import taskR

app = FastAPI()

app.include_router(router = taskR.router)



#pip install -r requirements.txt --> dependecias de la api