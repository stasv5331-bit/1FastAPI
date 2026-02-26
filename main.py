from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

<<<<<<< HEAD
# Импортируем модели
from models import User, Feedback
=======
# ----- НОВЫЙ ИМПОРТ -----
from models import User  # Импортируем модель User из файла models.py

# Создаем приложение
app = FastAPI()
>>>>>>> cabe61b76a35df286ca1cb96aa4bdc88f3a398dd

# Импортируем функции для работы с отзывами ИЗ ПАПКИ DATA
from data.feedback_storage import add_feedback, get_all_feedbacks, get_feedbacks_count

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# ----- СТАРЫЙ КОД (GET /) -----
@app.get("/")
async def read_root(request: Request):
    message = "Привет, это строка из FastAPI!"
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"data": message}
    )

<<<<<<< HEAD
# ----- СТАРЫЙ КОД (POST /calculate) -----
=======
# ----- СТАРЫЙ КОД (POST запрос) -----
>>>>>>> cabe61b76a35df286ca1cb96aa4bdc88f3a398dd
class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

<<<<<<< HEAD
# ----- СТАРЫЙ КОД (GET /users) -----
=======
# ----- НОВЫЙ КОД (GET /users) -----
# Создаем экземпляр (объект) пользователя
>>>>>>> cabe61b76a35df286ca1cb96aa4bdc88f3a398dd
user = User(name="John Doe", id=1)

@app.get("/users")
async def get_user():
<<<<<<< HEAD
    return user

# ----- НОВЫЙ КОД (POST /feedback) -----
@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    # Сохраняем отзыв через функцию из папки data
    add_feedback(feedback)
    
    # Отправляем ответ пользователю
    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }

# ----- НОВЫЙ КОД (GET /feedbacks) для просмотра всех отзывов -----
@app.get("/feedbacks")
async def get_all_feedbacks_route():
    all_feedbacks = get_all_feedbacks()
    return {
        "feedbacks": all_feedbacks,
        "total": get_feedbacks_count()
    }

# ----- КОД ДЛЯ ЗАПУСКА -----
=======
    # FastAPI автоматически преобразует объект User в JSON
    return user

# ----- КОД ДЛЯ ЗАПУСКА (остается без изменений) -----
>>>>>>> cabe61b76a35df286ca1cb96aa4bdc88f3a398dd
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