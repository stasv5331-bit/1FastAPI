feedback_list = []

def add_feedback(feedback):
    feedback_list.append(feedback)
    print(f"✅ Отзыв сохранен. Всего отзывов: {len(feedback_list)}")

def get_all_feedbacks():
    return feedback_list

def get_feedbacks_count():
    return len(feedback_list)