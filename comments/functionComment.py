#! python3

'''
AddComments.py - generate doxygen documentation for functions.
'''

import pyperclip

comments = r'''
/** @brief

@param
@param

@sa
*/
'''

pyperclip.copy(comments)
