from pydantic import BaseModel

# Создаем модель User (Пользователь)
class User(BaseModel):
    name: str  # Имя пользователя (строка)
    id: int    # ID пользователя (целое число)