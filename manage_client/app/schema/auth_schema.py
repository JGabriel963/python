from pydantic import BaseModel

class TokenSchema(BaseModel):
    acess_token: str

class TokenPayload(BaseModel):
    sub: int = None
    exp: int = None