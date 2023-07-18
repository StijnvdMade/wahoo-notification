# Description: Read email from file and extract tracking link
# Author: Stijn van der Made
# Date: 17/07/2023

import re
import sys
import os

# Get the absolute path of the current script file
current_script_path = os.path.abspath(__file__)

# Get the directory of the script
script_directory = os.path.dirname(current_script_path)

# Your file name (replace 'your_file_name.txt' with your actual file name)
file_name = 'email.html'

# Construct the absolute path to your file
file_path = os.path.join(script_directory, file_name)

def read_email():
    # Read email from file
    with open(file_path, 'r') as f:
        email = f.read()
    return email

def get_email_body(email):
    # Get email body
    email_body = email.split('\n\n', 1)[1]
    return email_body

def filter_tracking_link(email_body):
    # Filter tracking link
    try:
        filter = re.compile(r'https://www.wahooligan.com/users/live/\w+-\w+')
        tracking_link = filter.search(email_body).group()
    except AttributeError:
        filter = re.compile(r'https://www.wahooligan.com/users/live/\w+')
        tracking_link = filter.search(email_body).group()
    return tracking_link

if __name__ == '__main__':
    email = read_email()
    tracking_link = filter_tracking_link(get_email_body(email))
    print(tracking_link)