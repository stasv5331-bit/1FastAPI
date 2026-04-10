from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, ClassVar  # ← Добавь ClassVar
import re

# Для задания 1 (проверка возраста)
class UserAge(BaseModel):
    name: str
    age: int

# Для задания 3 (вложенная модель Contact)
class Contact(BaseModel):
    email: EmailStr
    phone: Optional[str] = Field(None, pattern=r'^\d{7,15}$')

# Для заданий 2 и 3 (Feedback с валидацией)
class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    contact: Contact
    
    FORBIDDEN_WORDS: ClassVar[list] = ['редиска', 'бяка', 'коязвка']  # ← Добавлено ClassVar
    
    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str):
        v_lower = v.lower()
        for word in cls.FORBIDDEN_WORDS:
            if word in v_lower:
                raise ValueError(f'Использование недопустимых слов: "{word}"')
        return v