from fastapi import FastAPI, Query
from pydantic import BaseModel
import os
from models import UserAge, Feedback
from data.feedback_storage import add_feedback, get_all_feedbacks, get_feedbacks_count

app = FastAPI()

# ----- ЗАДАНИЕ 1: POST /user (проверка возраста) -----
@app.post("/user")
async def check_user_age(user_data: UserAge):
    return {
        "name": user_data.name,
        "age": user_data.age,
        "is_adult": user_data.age >= 18
    }

# ----- ЗАДАНИЯ 2 и 3: POST /feedback -----
@app.post("/feedback")
async def create_feedback(
    feedback: Feedback,
    is_premium: bool = Query(False)
):
    add_feedback(feedback)
    message = f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    if is_premium:
        message += " Ваш отзыв будет рассмотрен в приоритетном порядке."
    return {"message": message}

# ----- Просмотр всех отзывов -----
@app.get("/feedbacks")
async def get_all_feedbacks_route():
    return {
        "feedbacks": [
            {
                "name": fb.name,
                "message": fb.message,
                "contact": {
                    "email": fb.contact.email,
                    "phone": fb.contact.phone
                }
            }
            for fb in get_all_feedbacks()
        ],
        "total": get_feedbacks_count()
    }

# ----- ЗАПУСК -----
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        f"{os.path.basename(__file__)[:-3]}:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )