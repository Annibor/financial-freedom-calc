"""
Import needed for the code
"""
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
SHEET = GSPREAD_CLIENT.open('financial-freedom-calc')

def user_data():
    """
    Get user data and welcome to the program.
    """
    print('Welcome to the financial freedom calculator!\n')
    name = input('Please enter your name: \n')
    print(f'Hello {name}!\n')
    print('This program will calculate the number of years it takes'
          'to reach finanicial freedom, or how much you need to save'
          'each month to reach the finanicial freedom in a certain years.\n')

print(user_data())