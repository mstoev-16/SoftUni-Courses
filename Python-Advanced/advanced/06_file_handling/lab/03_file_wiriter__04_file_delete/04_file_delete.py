import os

try:
    os.remove('my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')


"""
Error handling is usually slower than a simple 
IF-statement, therefore, it is preferable to use
the latter if it involves something simpler and
far more likely to occur as an error (since the
deletion of a file is a common one).
"""
# if os.path.exists('my_first_file.txt'):
#     os.remove('my_first_file.txt')
# else:
#     print('File already deleted!')

