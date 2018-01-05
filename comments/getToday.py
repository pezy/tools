#! python3

'''
getToday.py - Get current date to clipboard
'''

import pyperclip
import datetime

now = datetime.datetime.now()
pyperclip.copy(now.strftime('%Y-%m-%d'))
