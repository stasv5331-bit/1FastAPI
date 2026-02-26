from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

# Импортируем модели
from models import User, Feedback

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

# ----- СТАРЫЙ КОД (POST /calculate) -----
class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

# ----- СТАРЫЙ КОД (GET /users) -----
user = User(name="John Doe", id=1)

@app.get("/users")
async def get_user():
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