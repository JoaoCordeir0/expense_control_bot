import locale
import io
import matplotlib.pyplot as plt
from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
from sqlalchemy import func
from .db import get_session
from .models import Expense, User
from .config import ADMIN_ID
from .hooks import *
from .texts import *
from dateutil.relativedelta import relativedelta
from api.gemini_api import GeminiApi

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

gemini_api = GeminiApi()

async def handle_start(update: Update, context):
    user = hook_register_user(update)
    message = START
    try:
        if user.active:
            message += START_ACTIVE
            keyboard_options = hook_get_keyboard_options('help')
        else:
            raise Exception
    except:
        message += START_INACTIVE
        keyboard_options = hook_get_keyboard_options('support')

    await update.message.reply_text(message, reply_markup=keyboard_options)

async def handle_support(update, context):
    await update.message.reply_text(SUPPORT, parse_mode='Markdown')

async def handle_help(update, context):
    message = gemini_api.create_response_with_help()
    await update.message.reply_text(message, parse_mode='Markdown')

async def handle_unknown_message(update: Update, context):
    try:
        message = gemini_api.create_response_with_user_message(update.message.text)
    except Exception as e:
        message = str(e)
    await update.message.reply_text(message)

async def handle_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(EDITED_MESSAGE)

async def handle_callback(update: Update, context):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id

    match query.data:
        case 'summary':
            await context.bot.send_message(chat_id=chat_id, text=CALLBACK_SUMMARY)
        case 'summary_chart':
            await context.bot.send_message(chat_id=chat_id, text=CALLBACK_SUMMARY_CHART)
        case 'add_expense':
            await context.bot.send_message(chat_id=chat_id, text=CALLBACK_ADD_EXPENSE)
        case 'calculate_salary':
            await context.bot.send_message(chat_id=chat_id, text=CALCULATE_INSTRUCTIONS)
        case 'help':
            await context.bot.send_message(chat_id=chat_id, text=gemini_api.create_response_with_help(), parse_mode='Markdown')

async def handle_active_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != ADMIN_ID:
        await update.message.reply_text(NOT_ACCESS)
        return

    if len(context.args) != 1:
        await update.message.reply_text(ACTIVE_INSTRUCTIONS)
        return

    session = get_session()
    user = session.query(User).filter_by(telegram_id=int(context.args[0])).first()
    if user:
        user.active = True
        user.updated_on = datetime.now()
        user.updated_by = f'{update.effective_user.name}-{str(update.effective_user.id)}'
        session.commit()
        await update.message.reply_text(USER_SUCCESS.format(name=user.name))
    else:
        await update.message.reply_text(USER_NOTFOUND)
    session.close()

async def handle_register_expense(update: Update, context):
    user, session = hook_get_user(update)
    if not user:
        session.close()
        await update.message.reply_text(USER_NOTREGISTRED)
        return
    if not user.active:
        session.close()
        await update.message.reply_text(USER_INACTIVE)
        return

    try:
        gemini = GeminiApi()
        gemini_response = gemini.extract_info_from_user_text(update.message.text)

        value = float(gemini_response.get('total_value'))
        description = str(gemini_response.get('description'))
        installments_bool = bool(gemini_response.get('is_installments', False))
        installments = int(gemini_response.get('quantity_installments', 0))
        
        if installments_bool:
            for i in range(0, installments):
                created_on = datetime.now() + relativedelta(months=i)
                expense = Expense(value=value/installments, description=description, user_id=user.id, created_on=created_on)
                session.add(expense)
                session.commit()
            await update.message.reply_text(EXPENSE_SUCCESS.format(name=user.name, value=value, description=f'{description} em ({installments}x)'))
        else:
            expense = Expense(value=value, description=description, user_id=user.id)
            session.add(expense)
            session.commit()
            await update.message.reply_text(EXPENSE_SUCCESS.format(name=user.name, value=value, description=description))
    except:
        await update.message.reply_text(EXPENSE_INSTRUCTIONS)
    finally:
        session.close()

async def handle_summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = get_session()
    try:
        telegram_id = update.effective_user.id

        user = session.query(User).filter_by(telegram_id=telegram_id).first()

        if not user:
            await update.message.reply_text(USER_NOTREGISTRED)
            session.close()
            return
        
        current_month, month_name = hook_get_month_str(context)

        expenses = session.query(Expense).filter(
            Expense.user_id == user.id,
            func.strftime("%Y-%m", Expense.created_on) == current_month
        ).all()

        if not expenses:
            await update.message.reply_text(EXPENSE_NONE.format(month=month_name))
            return

        response = f'📋 *Gastos detalhados do mês ({month_name}):*\n\n'
        total = 0
        for e in expenses:
            response += f"• {e.description.capitalize()}: R${e.value:.2f} - {e.created_on.strftime('%d/%m')}\n"
            total += e.value
        response += f'\n📊 *Total:* R${total:.2f}'

        await update.message.reply_text(response, parse_mode='Markdown')
    except Exception as e:
        print(e)
    finally:
        session.close()

async def handle_calculate_salary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = get_session()
    try:
        telegram_id = update.effective_user.id

        user = session.query(User).filter_by(telegram_id=telegram_id).first()

        if not user:
            await update.message.reply_text(USER_NOTREGISTRED)
            session.close()
            return

        current_month, month_name = hook_get_month_str(context)
        
        if len(context.args) == 0 or not context.args[0].isdigit():
            await update.message.reply_text(CALCULATE_INVALID)
            return
        
        user_salary = float(context.args[0])

        expenses = session.query(Expense).filter(
            Expense.user_id == user.id,
            func.strftime("%Y-%m", Expense.created_on) == current_month
        ).all()

        if not expenses:
            await update.message.reply_text(EXPENSE_NONE.format(month=month_name))
            return

        total = sum(e.value for e in expenses)
        remaining = user_salary - total

        message = REMAINING_SALARY_POSITIVE if remaining >= 0 else REMAINING_SALARY_NEGATIVE
        
        await update.message.reply_text(message.format(salary=user_salary, total=total, remaining=remaining, month=month_name))
    finally:
        session.close()

async def handle_summary_chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = get_session()
    try:
        telegram_id = update.effective_user.id

        month_and_year = datetime.now().strftime('%B/%Y')
        current_month, month_name = hook_get_month_str(context)

        user = session.query(User).filter_by(telegram_id=telegram_id).first()
        if not user:
            await update.message.reply_text(USER_NOTREGISTRED)
            session.close()
            return

        expenses = session.query(Expense).filter(
            Expense.user_id == user.id,
            func.strftime("%Y-%m", Expense.created_on) == current_month
        ).all()
        session.close()

        if not expenses:
            await update.message.reply_text(EXPENSE_NONE.format(month=month_name))
            return

        labels = [f"{e.description.capitalize()}-{e.created_on.strftime('%d/%m')}" for e in expenses]
        values = [e.value for e in expenses]
    
        chart_option = 'barra' if len(context.args) == 0 else context.args[0]

        match chart_option:
            case 'linha':
                fig, ax = plt.subplots(figsize=(8, 4))

                ax.plot(labels, values, color='#7e22ce', marker='o', linewidth=2)

                ax.set_title(f'Gastos de {month_and_year}')
                ax.set_ylabel('Valor (R$)')
                plt.xticks(rotation=45, ha='right')

                for i, value in enumerate(values):
                    ax.text(i, value + max(values)*0.02, f'R$ {value:.2f}', ha='center', va='bottom', fontsize=9)

                plt.tight_layout()
            
            case 'pizza':
                fig, ax = plt.subplots(figsize=(6, 6))
                
                ax.pie(
                    values,
                    labels=labels,
                    autopct='R$ %.2f',
                    startangle=90,
                )

                ax.set_title(f'Gastos de {month_and_year}')
                ax.axis('equal')

                plt.tight_layout()

            case 'barra-vertical':
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.bar(labels, values, color='#7e22ce')
                ax.set_title(f'Gastos de {month_and_year}')
                ax.set_ylabel('Valor (R$)')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()

            case _:
                fig, ax = plt.subplots(figsize=(8, 4))

                ax.barh(labels, values, color='#7e22ce')
                ax.set_title(f'Gastos de {month_and_year}')
                ax.set_xlabel('Valor (R$)')

                for i, v in enumerate(values):
                    ax.text(v + max(values)*0.01, i, f'R$ {v:.2f}', va='center')

                plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        await update.message.reply_photo(photo=buf)

        buf.close()
    finally:
        session.close()
