from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

# ----- НОВЫЙ ИМПОРТ -----
from models import User  # Импортируем модель User из файла models.py

# Создаем приложение
app = FastAPI()

# Указываем папку с шаблонами
templates = Jinja2Templates(directory="templates")

# ----- СТАРЫЙ КОД (GET запрос) -----
@app.get("/")
async def read_root(request: Request):
    message = "Привет, это строка из FastAPI!"
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"data": message}
    )

# ----- СТАРЫЙ КОД (POST запрос) -----
class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

# ----- НОВЫЙ КОД (GET /users) -----
# Создаем экземпляр (объект) пользователя
user = User(name="John Doe", id=1)

@app.get("/users")
async def get_user():
    # FastAPI автоматически преобразует объект User в JSON
    return user

# ----- КОД ДЛЯ ЗАПУСКА (остается без изменений) -----
if __name__ == "__main__":
    import uvicorn
    file_name = os.path.basename(__file__)
    module_name = file_name[:-3]
    uvicorn.run(
        f"{module_name}:app",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True
    )