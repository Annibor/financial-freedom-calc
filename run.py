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

def choose_what_to_calc():
    """
    Choose what to calculate.
    """
    print('Please choose what you want to calculate:\n')
    print('1. How many years it takes to reach the finanicial freedom\n')
    print('2. How much you need to save each month to reach the finanicial'
          'freedom in a certain years\n')
    choice = input('Enter your choice: \n')
    if choice == '1':
        how_many_years()
    elif choice == '2':
        how_much_to_save_each_month()
    else:
        print('Invalid choice. Please try again.\n')
        choose_what_to_calc()