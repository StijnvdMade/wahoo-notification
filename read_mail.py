# Description: Read email from file and extract tracking link
# Author: Stijn van der Made
# Date: 17/07/2023

import re
import sys

def read_email():
    # print argv
    # print(sys.argv[1])
    # Read email from file
    with open('~/Wahoo_mails/email.html', 'r') as f:
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