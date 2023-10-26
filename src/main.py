from datetime import datetime, timedelta  
from pathlib import Path
import os
import re
from collections import OrderedDict
from pprint import pprint
import tempfile
import sys
# import urllib, requests
import logging
from logging.handlers import RotatingFileHandler
from telegram_handler.handlers import TelegramHandler
from telegram_handler.formatters import HtmlFormatter

TELEGRAM_NOTIFICATION_BOT_TOKEN="6400828497:AAFlJ_rrNnV2mjt8M_rNh8aSk7WzXUZkwpQ"
TELEGRAM_NOTIFICATION_CHAT_ID="-1001927109642"
REPLY_TO_MESSAGE_ID="2"


"""
Configure logger: 
https://docs.python.org/3/howto/logging.html#configuring-logging
"""


log = logging.getLogger('main')

def init_logger(telegram_chat_token, telegram_chat_id, telegram_reply_to_message):

    log.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)s: %(message)s')

    stream_handler.setFormatter(formatter)

    log.addHandler(stream_handler)

    # file_handler = RotatingFileHandler(filename, mode='a', maxBytes=1024*1024*10, backupCount=3, encoding="utf8")
    # file_handler.setLevel(logging.INFO)

    # formatter = logging.Formatter('%(levelname)s\t: %(asctime)s - %(message)s')
    # file_handler.setFormatter(formatter)

    # log.addHandler(file_handler)
    telegram_handler = TelegramHandler(level=logging.WARNING, token=telegram_chat_token, reply_to_message_id=telegram_reply_to_message, chat_id=telegram_chat_id)
    telegram_handler.setLevel(logging.WARNING)

    formatter = HtmlFormatter()
    telegram_handler.setFormatter(formatter)

    log.addHandler(telegram_handler)





def main():
    init_logger(
        os.getenv("TELEGRAM_NOTIFICATION_BOT_TOKEN"),
        os.getenv("TELEGRAM_NOTIFICATION_CHAT_ID"),
        os.getenv("REPLY_TO_MESSAGE_ID"),
        )
    log.info(f"this message level: info")
    log.warning(f"this message level: info")
    


if __name__ == "__main__":
    main()
