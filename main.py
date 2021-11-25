from login import *


user_filename = 'data/users.csv'
remove_all_empty_lines(user_filename)
login(user_filename)
remove_all_empty_lines(user_filename)