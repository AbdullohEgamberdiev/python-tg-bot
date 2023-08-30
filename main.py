from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6459872018:AAEgwibi-Q1t8ns2FKoGXAf5xPTksuNp4-Q'
BOT_USERNAME: Final = '@MrAbdullokhBot'

async def start_command(update: Update, contest: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salom, mening ismim Abdulloh va mening shaxsiy botimga tashrif buyurganingiz uchun tashakkur.')

async def help_command(update: Update, contest: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bu bot orqali siz... websayt zakaz qilishingiz va ingliz tili kursimga yozilishingiz mumkin!')

async def websayt_command(update: Update, contest: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Siz har xil turdagi vebsayt zakaz qilishingiz mumkin. MASALAN: 1 varoqli, 2 varoqli, 3 varoqli, 4 varoqli, 5 varoqli, 6-10 varoqli, 10-15 varoqli. 15-20 varoqli...')

async def english_command(update: Update, contest: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Siz har xil bosqichdagi guruhlarga qo`shilishingiz mumkin. MASALAN: starter, beginner, elementary, pre-intermediate ')


# Responses
def handle_response (text: str) -> str:
    processed: str = text.lower()

    if 'Salom' in processed:
        return 'Salom!'

    if '1 varoqli' in processed:
        return '1 Varoqli sayt narxi +domen, +hosting: 💵 70$ - 130$. [1 hafta ichida tayyor bo`ladi, sababi hosting va domen registratsiyasi 👨🏻‍💻]'

    if '2 varoqli' in processed:
        return '2 Varoqli sayt narxi +domen, +hosting: 140$ - 200$. [1 hafta ichida tayyor bo`ladi, sababi hosting va domen registratsiyasi 👨🏻‍💻]'

    if '3 varoqli' in processed:
        return '3 Varoqli sayt narxi +domen, +hosting: 210$ - 270$. [1-1.5 hafta ichida tayyor bo`ladi, sababi hosting va domen registratsiyasi 👨🏻‍💻]'

    if '4 varoqli' in processed:
        return '4 Varoqli sayt narxi +domen, +hosting: 280$ - 340$. [1-1.5 hafta ichida tayyor bo`ladi, sababi hosting va domen registratsiyasi 👨🏻‍💻]'

    if '5 varoqli' in processed:
        return '5 Varoqli sayt narxi +domen, +hosting: 350$ - 410$. [1-1.5 hafta ichida tayyor bo`ladi, sababi hosting va domen registratsiyasi 👨🏻‍💻]'

    if '6-10 varoqli' in processed:
        return '6-10 Varoqli sayt narxi +domen, +hosting: 500$ - 900$. [2.5-3 hafta ichida tayyor bo`ladi, sababi hosting va domen registratsiyasi 👨🏻‍💻]'

    if '10-15 varoqli' in processed:
        return '10-15 Varoqli sayt narxi +domen, +hosting: 1000$ - 1400$. [3.5-4 hafta ichida tayyor bo`ladi, sababi hosting va domen registratsiyasi 👨🏻‍💻]'

    if '15-20 varoqli' in processed:
        return '15-20 Varoqli sayt narxi +domen, +hosting: 1500$ - 2100$. [6-7 hafta ichida tayyor bo`ladi, sababi hosting va domen registratsiyasi 👨🏻‍💻]'

    if 'starter' in processed:
        return 'starter guruhga qo`shilish uchun ism, familiyangiz va telefon raqamingizni yozib qoldiring! MISOL UCHUN: Eshmatov Toshmat +998(99)000-00-00'

    if 'beginner' in processed:
        return 'beginner guruhga qo`shilish uchun ism, familiyangiz va telefon raqamingizni yozib qoldiring! MISOL UCHUN: Eshmatov Toshmat +998(99)000-00-00'

    if 'elementary' in processed:
        return 'elementary guruhga qo`shilish uchun ism, familiyangiz va telefon raqamingizni yozib qoldiring! MISOL UCHUN: Eshmatov Toshmat +998(99)000-00-00'

    if 'pre-intermediate' in processed:
        return 'pre-intermediate guruhga qo`shilish uchun ism, familiyangiz va telefon raqamingizni yozib qoldiring! MISOL UCHUN: Eshmatov Toshmat +998(99)000-00-00'

    return 'Xatolik bor ❌...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type} : "{text}"')


    response: str = handle_response(text)

    print('Bot:', response )
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if  __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('websayt', websayt_command))
    app.add_handler(CommandHandler('english', english_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)






    python
import requests
import json

# Telegram bot token
TOKEN = 'MrAbdullokhBot'

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()

def process_message(message):
    chat_id = message['chat']['id']
    text = message['text']

    # Process the received message and generate a response
    response_text = f"You said: {text}"

    # Send the response
    send_message(chat_id, response_text)

def main():
    # Set up a webhook to receive updates
    url = f'https://api.telegram.org/bot{TOKEN}/setWebhook'
    payload = {'url': 'YOUR_WEBHOOK_URL'}
    response = requests.post(url, json=payload)

    # Start listening for updates
    while True:
        # Get updates from Telegram
        updates_url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
        response = requests.get(updates_url)
        updates = response.json()

        # Process each update
        for update in updates['result']:
            process_message(update['message'])

        # Remove processed updates
        if updates['result']:
            last_update_id = updates['result'][-1]['update_id']
            url = f'https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_update_id + 1}'
            requests.get(url)

if __name__ == '__main__':
    main()
