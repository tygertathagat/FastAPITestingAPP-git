from fastapi import FastAPI,BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import schemas
import crud
import models
from database import get_db, engine
import database


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/index")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], #Allows all origin
    allow_credentials=True,
    allow_methods=['*'], #Allows all methods
    allow_headers=['*'], #Allows all headers
)

@app.post('/translate', response_model=schemas.TaskResponse)
def translate(request:schemas.TranslationRequest):
    task =crud.create_translation_task(get_db.db,request.text, request.languages)
    BackgroundTasks.add_task(perform_translation, task.id, request.text, request.languages, get_db.db)
    