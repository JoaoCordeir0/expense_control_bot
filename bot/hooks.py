import re
from .db import get_session
from .models import Expense, User
from .texts import STATIC_RESPONSES
from datetime import datetime
from unidecode import unidecode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def hook_get_user(update) -> tuple:
    session = get_session()
    telegram_id = update.effective_user.id
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    return user, session

def hook_register_user(update) -> User:
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

def hook_format_text(description) -> str:
    words = ['com a ', 'com o ', 'na ', 'no ', 'com ', 'em ']
    for word in words:
        description = description.replace(word, '')
    return description.strip().capitalize()

def hook_get_month_str(context) -> str:
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
    try:
        for arg in context.args:
            month = arg.strip().lower()
            if month in months.keys():
                month_number = months[month]
    finally:
        if month_number != 0:
            date = datetime(datetime.now().year, month_number, 1)
            return date.strftime('%Y-%m'), date.strftime('%B').capitalize()
        
        now = datetime.now()
        return now.strftime('%Y-%m'), now.strftime('%B').capitalize()

def hook_create_response_with_user_message(original_message) -> str:
    standardized_message = re.sub(r'[^\w\s]', '', unidecode(original_message).strip().lower())
    try:
        for key in STATIC_RESPONSES:
            if standardized_message in key:
                return STATIC_RESPONSES[key], False
        raise KeyError
    except KeyError:
        now_hour = datetime.now().hour
        if 5 <= now_hour < 12:
            return STATIC_RESPONSES['bom dia'], True
        elif 12 <= now_hour < 18:
            return STATIC_RESPONSES['boa tarde'], True
        else:
            return STATIC_RESPONSES['boa noite'], True
        
def hook_get_keyboard_options(type):
    keyboard = []
    match type:
        case 'help':
            keyboard = [
                [InlineKeyboardButton('🗒️ Ver resumos', callback_data='summary')],
                [InlineKeyboardButton('📊 Ver resumos em gráfico', callback_data='summary_chart')],
                [InlineKeyboardButton('📝 Adicionar gasto', callback_data='add_expense')],
                [InlineKeyboardButton('💰 Calcular salário', callback_data='calculate_salary')],
                [InlineKeyboardButton('🧠 Solicitar ajuda', callback_data='help')],
            ]

        case 'support':
            keyboard = [
                [InlineKeyboardButton('💬 Acionar o suporte', url='https://t.me/Cordeirovsk')],
            ]
            
    return InlineKeyboardMarkup(keyboard)
    
def hook_is_installments(text):
    for value in ['2x', '3x', '4x', '5x', '6x', '7x', '8x', '9x', '10x', '11x', '12x']:
        if value in text:
            new_text = text.replace(value, '').strip() + f' em {value}'
            return new_text, int(value.replace('x', '')), True
    return text.strip(), 0, False