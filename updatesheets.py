"""
Making googlesheet update with inputs information from the user, and the results from calculations
"""
#The imports are adapted form Love Sandwiches
# by Code institute. Link in README.md
import gspread
from google.oauth2.service_account import Credentials
#The scope is adapted form Love Sandwiches
# by Code institute. Link in README.md
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
#The creds, scoped creds, gspread clients and sheets are
# adapted form Love Sandwiches, by Code institute. Link in README.md
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('financial-freedom-calc')

# All the following codes are based on
# Code Institutes Love Sandwiches. Link in README.md
def update_user_worksheet(user_data_list):
    """Update the user worksheet. Add new
    information to the worksheet from user input.
    """
    print('Update the user worksheet...\n')
    user_worksheet = SHEET.worksheet('user_sheet')
    user_worksheet.append_row(user_data_list)
    print('User worksheet updated')

def update_financial_worksheet_one(financial_data_list_one):
    """
    Update the financial worksheet one. Add new
    information to the worksheet from user inputs in choice one.
    """
    print('Update the financial worksheet...\n')
    financial_worksheet = SHEET.worksheet('financial_sheet_one')
    financial_worksheet.append_row(financial_data_list_one)
    print('Financial worksheet updated')

def update_financial_worksheet_two(financial_data_list_two):
    """
    Update the financial worksheet two. Add new
    information to the worksheet from user inputs in choice two.
    """
    print('Update the financial worksheet...\n')
    financial_worksheet = SHEET.worksheet('financial_sheet_two')
    financial_worksheet.append_row(financial_data_list_two)
    print('Financial worksheet updated')

def update_answers_calculations(answers_data_list):
    """
    Update the answers whorksheet. Add new
    information to the worksheet from claculations made form the users inputs.
    """
    print('Update the answers worksheet...\n')
    financial_worksheet = SHEET.worksheet('Answer_calculations')
    financial_worksheet.append_row(answers_data_list)
    print('Answers worksheet updated')
