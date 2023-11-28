import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Token bot Telegram Anda
TELEGRAM_BOT_TOKEN = '6857385915:AAGHGbdMRMQ1lsAL2Y8n6MOZIMzSicugwQw'

# ID chat grup atau user di Telegram
TELEGRAM_CHAT_ID = '576495165'

# URL untuk mengupload file ke GitHub
GITHUB_UPLOAD_URL = 'https://api.github.com/Paper890/izin//main/IP'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot is running!')

def process_text(update: Update, context: CallbackContext) -> None:
    # Mendapatkan teks dari pesan
    text = update.message.text

    # Mengekstrak informasi dari teks
    parts = text.split()
    username = parts[0].replace('#', '')
    date = parts[1]
    ip_address = parts[2]
    status = parts[3]

    # Format teks untuk diisi ke dalam file
    file_content = f'{username} {date} {ip_address} {status}\n'

    # Menyimpan ke file
    with open('log.txt', 'a') as file:
        file.write(file_content)

    # Mengirim file ke GitHub
    upload_to_github()

def upload_to_github():
    # Mengganti nilai-nilai ini sesuai dengan informasi GitHub Anda
    github_username = 'Paper890'
    github_repository = 'izin'
    github_path = 'izin/IP'
    github_file_name = 'IP.txt'

    # Membaca token GitHub dari variabel lingkungan
    github_token = os.environ.get('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')

    # Membaca isi file
    with open(github_file_name, 'r') as file:
        file_content = file.read()

    # Membuat payload untuk request
    payload = {
        'message': 'Update log file',
        'content': file_content
    }

    # Menentukan header untuk autentikasi
    headers = {
        'Authorization': f'token {github_token}'
    }

    # Melakukan request untuk mengupdate file di GitHub
    response = requests.put(
        GITHUB_UPLOAD_URL.replace('Paper890', github_username)
                        .replace('izin', github_repository)
                        .replace('izin/IP', github_path)
                        .replace('IP.txt', github_file_name),
        headers=headers,
        json=payload
    )

    # Memeriksa status response
    if response.status_code == 200:
        print('File successfully uploaded to GitHub')
    else:
        print(f'Failed to upload file to GitHub. Status code: {response.status_code}')

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Menambahkan handler untuk command /start
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Menambahkan handler untuk mengolah pesan teks
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_text))

    # Memulai polling untuk mendapatkan pembaruan dari Telegram
    updater.start_polling()

    # Menjalankan bot hingga disetop manual
    updater.idle()

if __name__ == '__main__':
    main()
