from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import os

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

# ----- НОВЫЙ КОД (POST запрос) -----
from pydantic import BaseModel  # Добавь этот импорт в начало файла!

# Создаем модель данных для двух чисел
class Numbers(BaseModel):
    num1: float
    num2: float

# Создаем маршрут для POST запроса
@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

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