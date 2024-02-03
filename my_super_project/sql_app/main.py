from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models 
from . database import engine, SessionLocal
from . import schema


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

# ------------ Cours -------------
@app.post("/cours/", status_code=status.HTTP_201_CREATED)
async def create_cours(cours: schema.CoursBase, db: Session = db_dependency):
    db_cours = models.Cours(**cours.dict())
    db.add(db_cours)
    db.commit()
    db.refresh(db_cours)
    
@app.get("/cours/{cours_id}", status_code=status.HTTP_200_OK, response_model= schema.CoursResponse)
async def read_cours(cours_id: int, db: Session = db_dependency):
    cours = db.query(models.Cours).filter(models.Cours.id == cours_id).first()
    if cours is None:
        raise HTTPException(status_code=404, detail='Cours non trouvé')
    return cours

@app.put("/cours/{cours_id}", status_code=status.HTTP_200_OK, response_model=schema.CoursResponse)
async def update_cours(cours_id: int, cours: schema.CoursBase, db: Session = db_dependency):
    db_cours = db.query(models.Cours).filter(models.Cours.id == cours_id).first()
    if db_cours is None:
        raise HTTPException(status_code=404, detail='Post not found')
    
    for key, value in cours.dict().items():
        setattr(db_cours, key, value)
    
    db.commit()
    db.refresh(db_cours)
    return db_cours

@app.delete("/cours/{cours_id}", status_code=status.HTTP_200_OK)
async def delete_cours(cours_id: int, db: Session = db_dependency):
    db_cours = db.query(models.Cours).filter(models.Cours.id == cours_id).first()
    if db_cours is None:
        raise HTTPException(status_code=404, detail='Cours non trouvé')
    db.delete(db_cours)
    db.commit()
    
# ------------ Module -------------
@app.post("/module/", status_code=status.HTTP_201_CREATED, response_model=schema.ModuleResponse)
async def create_module(module: schema.ModuleBase, db: Session= db_dependency):
    db_module = models.Module(**module.dict())
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    # return schema.ModuleResponse(module_name=db_module.module_name)

@app.get("/module/{module_id}", status_code=status.HTTP_200_OK, response_model=schema.ModuleResponse)
async def read_module(module_id: int, db: Session= db_dependency):
    module = db.query(models.Module).filter(models.Module.id == module_id).first()
    if module is None:
        raise HTTPException(status_code=404, detail='Module not found')
    return schema.ModuleResponse(module_name=module.module_name)

@app.put("/module/{module_id}", status_code=status.HTTP_200_OK, response_model=schema.ModuleResponse)
async def update_module(module_id: int, module: schema.ModuleBase, db: Session= db_dependency):
    db_module = db.query(models.Module).filter(models.Module.id == module_id).first()
    if db_module is None:
        raise HTTPException(status_code=404, detail='Module not found')
    
    for key, value in module.dict().items():
        setattr(db_module, key, value)        
    db.commit()
    db.refresh(db_module)
    return db_module

@app.delete("/module/{module_id}", status_code=status.HTTP_200_OK)
async def delete_module(module_id: int, db: Session= db_dependency):
    db_module = db.query(models.User).filter(models.Module.id == module_id).first()
    if db_module is None:
        raise HTTPException(status_code=404, detail='Module not found')
    db.delete(db_module)
    db.commit()
    db.delete(db_module)
    db.commit()
    
# ------------------- Etudiant --------------------

@app.post("/etudiant/", status_code=status.HTTP_201_CREATED)
async def create_etudiant(etudiant: schema.EtudiantBase, db: Session = db_dependency):
    db_etudiant = models.Etudiant(**etudiant.dict())
    db.add(db_etudiant)
    db.commit()
    db.refresh(db_etudiant)
    
@app.get("/etudiant/{etudiant_id}", status_code=status.HTTP_200_OK, response_model= schema.EtudiantBase)
async def read_etudiant(etudiant_id: int, db: Session = db_dependency):
    cours = db.query(models.Etudiant).filter(models.Etudiant.id == etudiant_id).first()
    if cours is None:
        raise HTTPException(status_code=404, detail='Etudiant non trouvé')
    return cours

@app.put("/etudiant/{etudiant_id}", status_code=status.HTTP_200_OK, response_model=schema.EtudiantBase)
async def update_etudiant(etudiant_id: int, etudiant: schema.EtudiantBase, db: Session = db_dependency):
    db_etudiant = db.query(models.Etudiant).filter(models.Etudiant.id == etudiant_id).first()
    if db_etudiant is None:
        raise HTTPException(status_code=404, detail='Etudiant not found')
    
    for key, value in etudiant.dict().items():
        setattr(db_etudiant, key, value)
    
    db.commit()
    db.refresh(db_etudiant)
    return db_etudiant

@app.delete("/etudiant/{etudiant_id}", status_code=status.HTTP_200_OK)
async def delete_etudiant(etudiant_id: int, db: Session = db_dependency):
    db_etudiant = db.query(models.Etudiant).filter(models.Etudiant.id == etudiant_id).first()
    if db_etudiant is None:
        raise HTTPException(status_code=404, detail='Etudiant non trouvé')
    db.delete(db_etudiant)
    db.commit()
    
# ------------------- Professeurs --------------------

@app.post("/professeur/", status_code=status.HTTP_201_CREATED)
async def create_professeur(professeur: schema.ProfesseurBase, db: Session = db_dependency):
    db_professeur = models.Professeur(**professeur.dict())
    db.add(db_professeur)
    db.commit()
    db.refresh(db_professeur)
    
@app.get("/professeur/{professeur_id}", status_code=status.HTTP_200_OK, response_model= schema.ProfesseurBase)
async def read_professeur(professeur_id: int, db: Session = db_dependency):
    professeur = db.query(models.Professeur).filter(models.Professeur.id == professeur_id).first()
    if professeur is None:
        raise HTTPException(status_code=404, detail='professeur non trouvé')
    return professeur

@app.put("/professeur/{professeur_id}", status_code=status.HTTP_200_OK, response_model=schema.ProfesseurBase)
async def update_professeur(professeur_id: int, professeur: schema.ProfesseurBase, db: Session = db_dependency):
    db_professeur = db.query(models.Professeur).filter(models.Professeur.id == professeur_id).first()
    if db_professeur is None:
        raise HTTPException(status_code=404, detail='professeur not found')
    
    for key, value in professeur.dict().items():
        setattr(db_professeur, key, value)
    
    db.commit()
    db.refresh(db_professeur)
    return db_professeur

@app.delete("/professeur/{professeur_id}", status_code=status.HTTP_200_OK)
async def delete_professeur(professeur_id: int, db: Session = db_dependency):
    db_professeur = db.query(models.Professeur).filter(models.Professeur.id == professeur_id).first()
    if db_professeur is None:
        raise HTTPException(status_code=404, detail='professeur non trouvé')
    db.delete(db_professeur)
    db.commit()