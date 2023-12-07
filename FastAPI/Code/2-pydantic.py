# user = {"nome": "Fulano", "idade": 25, "email": "fulano@gmail.com"}

# print(user)

from pydantic import BaseModel, field_validator


class User(BaseModel):
    name: str
    age: int
    email: str

    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("E-mail está inválido")
        return value


user1 = User(name="Fulano", age=23, email="fulano@gmail.com")

print(user1)
