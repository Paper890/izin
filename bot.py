from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from github import Github
import base64

# Token dari bot Telegram dan token akses pribadi GitHub
TELEGRAM_TOKEN = '6857385915:AAGHGbdMRMQ1lsAL2Y8n6MOZIMzSicugwQw'
GITHUB_TOKEN = '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'

# Membuat instance Github
g = Github(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)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('WELCOME IP REGIST TO SKYTUNNEL')

def get_repos(update: Update, context: CallbackContext) -> None:
    user = g.get_user()
    repos = user.get_repos()
    for repo in repos:
        update.message.reply_text(repo.name)

def add_ip(update: Update, context: CallbackContext) -> None:
    repo = g.get_user().get_repo('san')
    file = repo.get_contents('izin.txt', ref='master')
    data = base64.b64decode(file.content).decode('utf-8') + '\n### ' + ' '.join(context.args)
    repo.update_file(file.path, 'Updated by telegram bot', data, file.sha, branch='master')
    update.message.reply_text('IP added successfully!')

def main() -> None:
    updater = Updater(token=6857385915:AAGHGbdMRMQ1lsAL2Y8n6MOZIMzSicugwQw)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("get_repos", get_repos))
    dispatcher.add_handler(CommandHandler("add_ip", add_ip))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
 