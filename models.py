from pydantic import BaseModel

<<<<<<< HEAD
class User(BaseModel):
    name: str
    id: int

# Новая модель для отзывов
class Feedback(BaseModel):
    name: str      # Имя пользователя
    message: str   # Текст отзыва
=======
# Создаем модель User (Пользователь)
class User(BaseModel):
    name: str  # Имя пользователя (строка)
    id: int    # ID пользователя (целое число)
>>>>>>> cabe61b76a35df286ca1cb96aa4bdc88f3a398dd
