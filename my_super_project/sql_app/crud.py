from sqlalchemy.orm import Session

from . import models, schema

# CRUD operations for Cours
def create_cours(cours: schema.CoursBase, db: Session):
    db_cours = models.Cours(**cours.dict())
    db.add(db_cours)
    db.commit()
    db.refresh(db_cours)

def read_cours(cours_id: int, db: Session):
    cours = db.query(models.Cours).filter(models.Cours.id == cours_id).first()

def update_cours(cours_id: int, cours: schema.CoursBase, db: Session):
    db_cours = db.query(models.Cours).filter(models.Cours.id == cours_id).first()
       
    db.commit()
    db.refresh(db_cours)
    return db_cours

def delete_cours(cours_id: int, db: Session):
    db_cours = db.query(models.Cours).filter(models.Cours.id == cours_id).first()
    
    db.delete(db_cours)
    db.commit()
    
# CRUD operations for Module
def create_module(module: schema.ModuleBase, db: Session):
    db_module = models.Module(**module.dict())
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return schema.ModuleResponse(module_name=db_module.module_name)

def read_module(module_id: int, db: Session):
    module = db.query(models.Module).filter(models.Module.id == module_id).first()

def update_module(module_id: int, user: schema.ModuleBase, db: Session):
    db_module = db.query(models.Module).filter(models.Module.id == module_id).first()
        
    db.commit()
    db.refresh(db_module)
    return db_module

def delete_module(module_id: int, db: Session):
    db_module = db.query(models.User).filter(models.Module.id == module_id).first()
   
    db.delete(db_module)
    db.commit()

# CRUD operations for Etudiant
def create_etudiant(etudiant: schema.EtudiantBase, db: Session):
    db_etudiant = models.Etudiant(**etudiant.dict())
    db.add(db_etudiant)
    db.commit()
    db.refresh(db_etudiant)

def read_etudiant(etudiant_id: int, db: Session):
    etudiant = db.query(models.Etudiant).filter(models.Etudiant.id == etudiant_id).first()

def update_etudiant(etudiant_id: int, etudiant: schema.EtudiantBase, db: Session):
    db_etudiant = db.query(models.Etudiant).filter(models.Etudiant.id == etudiant_id).first()
       
    db.commit()
    db.refresh(db_etudiant)
    return db_etudiant

def delete_etudiant(etudiant_id: int, db: Session):
    db_etudiant = db.query(models.Etudiant).filter(models.Etudiant.id == etudiant_id).first()
    
    db.delete(db_etudiant)
    db.commit()    

# CRUD operations for Professeur
def create_professeur(professeur: schema.ProfesseurBase, db: Session):
    db_professeur = models.Professeur(**professeur.dict())
    db.add(db_professeur)
    db.commit()
    db.refresh(db_professeur)

def read_professeur(professeur_id: int, db: Session):
    professeur = db.query(models.Professeur).filter(models.Professeur.id == professeur_id).first()

def update_professeur(professeur_id: int, professeur: schema.ProfesseurBase, db: Session):
    db_professeur = db.query(models.Professeur).filter(models.Professeur.id == professeur_id).first()
       
    db.commit()
    db.refresh(db_professeur)
    return db_professeur

def delete_professeur(professeur_id: int, db: Session):
    db_professeur = db.query(models.Professeur).filter(models.Professeur.id == professeur_id).first()
    
    db.delete(db_professeur)
    db.commit()
