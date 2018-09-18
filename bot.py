#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from uuid import uuid4

from telegram import InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import Updater, CommandHandler, InlineQueryHandler

# Sample functions
def start(bot, update):
    update.message.reply_text("Hello, world")

def inline_split_words(bot, update):
    reversed_sentence = update.inline_query.query.split(' ')[::-1]
    results = (
        InlineQueryResultArticle(id = uuid4(),
                                 description = word.lower(),
                                 title = word.upper(),
                                 input_message_content=InputTextMessageContent(word.lower()))
        for word in reversed_sentence
    )
    update.inline_query.answer(results)
    
def main():
    TOKEN = os.getenv('BOT_TELEGRAM_TOKEN')
    PORT = int(os.getenv('PORT', '8443'))

    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(InlineQueryHandler(inline_split_words))

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook(os.getenv('HEROKU_APP_URL') + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
