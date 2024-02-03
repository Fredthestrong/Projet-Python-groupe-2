from pydantic import BaseModel

class CoursBase(BaseModel):
    title: str
    content: str
    module_id: int
    
class CoursResponse(BaseModel):
    title: str
    content: str
    module_id: int

class ModuleBase(BaseModel):
    module_name: str

class ModuleResponse(BaseModel):
    module_name: str

class EtudiantBase(BaseModel):
    name_etud: str
    first_name_etud :str
    email_etud : str
    password_etud: str
    
class EtudiantResponse(BaseModel):
    name_etud: str
    first_name_etud :str
    email_etud : str
    password_etud: str
    
class ProfesseurBase(BaseModel):
    name_prof : str
    first_name_prof: str
    email_prof : str
    password_prof: str
    speciality: str
    
class ProfesseurResponse(BaseModel):
    name_prof : str
    first_name_prof: str
    email_prof : str
    password_prof: str
    speciality: str