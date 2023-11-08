import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.OPEN('financial-freedom-calc')


def get_user_data():
    """
    Collect user data like name, email and address.
    """
    name = input('Enter your name: ')
    while True:
        try:
            email = input('Enter your email: ')
            if "@" in email and "." in email and email.find("@") < email.rfind('.'):
                break
        except:
            print('Invalid email address, please try again!')

get_user_data()
    