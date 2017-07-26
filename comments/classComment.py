#! python3

'''
classComment.py - generate doxygen documentation for class.
'''

import pyperclip
from datetime import datetime

comments = r'''
/**
@class provided in the file
@brief The class provides
@author pezy
@date {}
@sa
*/
'''.format(datetime.now().strftime('%Y-%m-%d'))

pyperclip.copy(comments)
