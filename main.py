from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
class FormData(BaseModel):
          currentGroupName: str
          newGroupName : str

@app.post("/submit-form")
async def submit_form(form_data: FormData):
    print("dingggggggggggggggggg")
    print(form_data)
    return {"message": "Form submitted successfully"}
