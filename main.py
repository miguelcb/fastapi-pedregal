from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app import crud, models, schema
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/persons/", response_model=List[schema.Person])
def read_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    persons = crud.get_persons(db, skip=skip, limit=limit)
    return persons


@app.get("/persons/{person_id}", response_model=schema.Person)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


@app.post("/persons/", response_model=schema.Person)
def create_person(person: schema.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person.document_id)
    if db_person:
        raise HTTPException(status_code=400, detail="Document already registered")
    return crud.create_person(db, person)


@app.put("/persons/{person_id}", response_model=schema.Person)
async def update_person(person_id: int, person: schema.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=400, detail="Person not found")
    return crud.update_person(db, person)


@app.delete("/persons/{person_id}/",)
async def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return crud.delete_person(db, person_id)