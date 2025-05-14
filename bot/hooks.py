import re
from .db import get_session
from .models import Expense, User
from .texts import STATIC_RESPONSES
from datetime import datetime
from unidecode import unidecode

def get_user(update) -> tuple:
    session = get_session()
    telegram_id = update.effective_user.id
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    return user, session

def register_user(update) -> User:
    session = get_session()
    telegram_id = update.effective_user.id
    user = session.query(User).filter_by(telegram_id=telegram_id).first()

    if not user:
        user = User(
            telegram_id=telegram_id,
            name=update.effective_user.first_name,
            username=update.effective_user.username,
            active=False # ou True para testes
        )
        session.add(user)
        session.commit()
    session.close()

    return user

def format_description(description) -> str:
    words = ['na ', 'no ', 'com ', 'em ']
    for word in words:
        description = description.replace(word, '')
    return description.capitalize()

def get_month_str(args) -> str:
    months = {
        'janeiro': 1,
        'fevereiro': 2,
        'março': 3,
        'abril': 4,
        'maio': 5,
        'junho': 6,
        'julho': 7,
        'agosto': 8,
        'setembro': 9,
        'outubro': 10,
        'novembro': 11,
        'dezembro': 12,
        'january': 1,
        'february': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october': 10,
        'november': 11,
        'december': 12
    }

    month_number = 0
    for arg in args:
        month = arg.strip().lower()
        if month in months.keys():
            month_number = months[month]

    if month_number != 0:
        date = datetime(datetime.now().year, month_number, 1)
        return date.strftime('%Y-%m'), date.strftime('%B').capitalize()
    
    now = datetime.now()
    return now.strftime('%Y-%m'), now.strftime('%B').capitalize()

def create_response_with_user_message(original_message) -> str:
    standardized_message = re.sub(r'[^\w\s]', '', unidecode(original_message).strip().lower())
    try:
        for key in STATIC_RESPONSES:
            if standardized_message in key:
                return STATIC_RESPONSES[key]
        raise KeyError
    except KeyError:
        now_hour = datetime.now().hour
        if 5 <= now_hour < 12:
            return STATIC_RESPONSES['bom dia']
        elif 12 <= now_hour < 18:
            return STATIC_RESPONSES['boa tarde']
        else:
            return STATIC_RESPONSES['boa noite']