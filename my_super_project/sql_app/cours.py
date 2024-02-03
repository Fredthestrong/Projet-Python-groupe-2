from fastapi import HTTPException, Depends, status ,APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models 
from . database import engine, SessionLocal
from . import schema

cours_app = APIRouter(
    prefix='/cours',
    tags=['cours']
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

# Au niveau de l'URL , mettre "/order"  sans le "/docs"
@cours_app.post("/cours/", status_code=status.HTTP_201_CREATED)
async def create_cours(cours: schema.CoursBase, db: Session = db_dependency):
    db_cours = models.Cours(**cours.dict())
    db.add(db_cours)
    db.commit()
    db.refresh(db_cours)
    
@cours_app.get("/cours/{cours_id}", status_code=status.HTTP_200_OK, response_model= schema.CoursResponse)
async def read_cours(cours_id: int, db: Session = db_dependency):
    cours = db.query(models.Cours).filter(models.Cours.id == cours_id).first()
    if cours is None:
        raise HTTPException(status_code=404, detail='Cours non trouvé')
    return cours

@cours_app.put("/cours/{cours_id}", status_code=status.HTTP_200_OK, response_model=schema.CoursResponse)
async def update_cours(cours_id: int, cours: schema.CoursBase, db: Session = db_dependency):
    db_cours = db.query(models.Cours).filter(models.Cours.id == cours_id).first()
    if db_cours is None:
        raise HTTPException(status_code=404, detail='Post not found')
    
    for key, value in cours.dict().items():
        setattr(db_cours, key, value)
    
    db.commit()
    db.refresh(db_cours)
    return db_cours

@cours_app.delete("/cours/{cours_id}", status_code=status.HTTP_200_OK)
async def delete_cours(cours_id: int, db: Session = db_dependency):
    db_cours = db.query(models.Cours).filter(models.Cours.id == cours_id).first()
    if db_cours is None:
        raise HTTPException(status_code=404, detail='Cours non trouvé')
    db.delete(db_cours)
    db.commit()