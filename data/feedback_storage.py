# Этот файл отвечает за хранение отзывов

# Список для хранения всех отзывов (в памяти)
feedback_list = []

def add_feedback(feedback):
    """Добавляет новый отзыв в хранилище"""
    feedback_list.append(feedback)
    print(f"✅ Отзыв сохранен. Всего отзывов: {len(feedback_list)}")

def get_all_feedbacks():
    """Возвращает все сохраненные отзывы"""
    return feedback_list

def get_feedbacks_count():
    """Возвращает количество отзывов"""
    return len(feedback_list)