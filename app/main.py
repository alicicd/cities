from fastapi import FastAPI, HTTPException
from elasticsearch import Elasticsearch
import os

app = FastAPI()

ES_HOST = os.getenv("ES_HOST", "http://localhost:9200")
es = Elasticsearch(ES_HOST)
INDEX_NAME = "cities"



@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/city")
def upsert_city(name: str, population: int):
    doc = {"name": name.lower(), "population": population}
    res = es.index(index=INDEX_NAME, id=name.lower(), document=doc)
    return {"result": res['result'], "city": name}

@app.get("/city/{name}")
def get_city(name: str):
    try:
        res = es.get(index=INDEX_NAME, id=name.lower())
        return res['_source']
    except:
        raise HTTPException(status_code=404, detail="City not found")
@app.get("/cities")
def get_all_cities():
    try:
        res = es.search(index=INDEX_NAME, query={"match_all": {}}, size=100)
        return [hit["_source"] for hit in res["hits"]["hits"]]
    except Exception as e:
        return []


