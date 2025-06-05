from pydantic import BaseModel

class ActorBase(BaseModel):
    first_name: str
    last_name: str

class ActorCreate(ActorBase):
    pass

class ActorRead(ActorBase):
    actor_id: int

class ActorUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    
    class Config:
        orm_mode = True