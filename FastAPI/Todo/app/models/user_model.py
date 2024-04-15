from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from datetime import datetime
from typing import Optional

class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hash_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[str] = None