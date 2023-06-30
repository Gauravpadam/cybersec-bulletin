from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import json

# Configure CORS
origins = [
    "http://localhost:3000",  # Replace with the URL of your React app
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/1")
async def read_item1():
    with open("JsonData.json", "r") as file:
        articledata = json.load(file)
        return articledata[:6]

@app.get("/2")
async def read_item2():
    with open("JsonData.json", "r") as file:
        articledata = json.load(file)

        return articledata[6:12]

@app.get("/3")
async def read_item3():
    with open("JsonData.json", "r") as file:
        articledata = json.load(file)
        return articledata[12:15]
