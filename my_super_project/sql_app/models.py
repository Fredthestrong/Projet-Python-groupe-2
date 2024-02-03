from sqlalchemy import Text, Column, Integer, String, ForeignKey
from . database import Base
from sqlalchemy.orm import relationship


class Module(Base):
    __tablename__ = 'modules'
    
    id = Column(Integer, primary_key=True)
    module_name = Column(String(50), unique=True)
    cours = relationship("Cours", back_populates="modules")
    
class Cours(Base):
    __tablename__ = 'cours'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(String(100))
    module_id = Column(Integer, ForeignKey("modules.id"))
    
    module = relationship("Module", back_populates="cours")
    
class Etudiant(Base):
    __tablename__ = 'etudiants'
    
    id = Column(Integer, primary_key=True)
    name_etud = Column(String(50))
    first_name_etud = Column(String(100))
    email_etud = Column(String(150))
    password_etud = Column(String(50))
    
class Professeur(Base):
    __tablename__ = 'professeurs'
    
    id = Column(Integer, primary_key=True, index=True)
    name_prof = Column(String(50))
    first_name_prof = Column(String(100))
    email_prof = Column(String(150))
    password_prof = Column(String(50))
    speciality = Column(String(50))
    
# class University(Base):
#     __tablename__ = 'universities'
    
#     id = Column(Integer)

    