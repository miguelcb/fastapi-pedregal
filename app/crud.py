from sqlalchemy.orm import Session
from . import models, schema


def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.document_id == person_id).first()


def get_persons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person: schema.PersonCreate):
    db_person = models.Person(document_id=person.document_id, first_name=person.first_name, last_name=person.last_name, birthdate=person.birthdate)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def update_person(db: Session, person_id: int, person: schema.PersonUpdate):
    db_person = get_person(db, person_id=person_id)
    if db_person is not None:
        db_person.first_name = person.first_name
        db_person.last_name = person.last_name
        db_person.birthdate = person.birthdate
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
    return db_person

def delete_person(db: Session, person_id: int):
    db_person = get_person(db, person_id=person_id)
    if db_person is not None:
        db.delete(db_person)
        db.commit()
        db.refresh(db_person)
    return db_person