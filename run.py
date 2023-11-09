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


def get_user_data():
    """
    Collect user data like name, email, and address.
    """
    print('Welcome to the financial freedom calculator!')
    print('This program will help you calculate the number of years \
          it takes to reach financial freedom, or how much you need to \
          save every month to reach financial freedom.')

    name = input('Enter your name: ')
    while True:
        email = input('Enter your email: ')
        if "@" in email and "." in email and email.find("@") < email.rfind('.'):
            break
        else:
            print('Invalid email address, please try again!')

    while True:
        age = input('Enter your age here: ')
        if age.isdigit():
            break
        else:
            print('Invalid data: age must be in digits, please try again!')

      user_data = {
        'name': name,
        'email': email,
        'age': age
    }

    user_data_sheet = SHEET.sheet1
    user_data_sheet.append_row([user_data['name'], user_data['email'], user_data['age']])

    return user_data

def update_google_sheet(data, worksheet):
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row([data['name'], data['email'], data['age']])
    print('Data successfully updated!')


def calculate_years_to_financial_freedom(initial_savings,
        monthly_savings, target_goal, annual_interest_rate, monthly_savings_percentage):
    """
    Calculate the years it takes to reach financial freedom.

    Args: initial_savings (float): The initial savings amount in euros.
    Args: monthly_savings (float): The monthly savings amount in euros.
    Args: target_goal (float): The target saving goal in euros.
    Args: annual_interest_rate (float): The annual interest rate as a percentage.
    Args: monthly_savings_percentage (float): The monthly savings percentage.
    
    Returns: years_to_financial_freedom (int): The number of years it 
    takes to reach financial freedom.
    """

    years_to_financial_freedom = 0
    initial_savings = float(initial_savings)
    monthly_savings = float(monthly_savings)
    target_goal = float(target_goal)
    annual_interest_rate = float(annual_interest_rate)
    monthly_savings_percentage = float(monthly_savings_percentage)
    annual_interest_rate = annual_interest_rate / 100
    monthly_savings_percentage = monthly_savings_percentage / 100

    while initial_savings < target_goal:
        initial_savings = initial_savings + (initial_savings * monthly_savings_percentage)
        years_to_financial_freedom = years_to_financial_freedom + 1

    return years_to_financial_freedom


def choose_what_to_calculate ():
    """
    Make user choose what to calculate.
    """
    print('1. Would you like to calculate the number of years it \
          takes to reach financial freedom, or 2. how much you need \
          to save every month to reach financial freedom? "')
    choice = input('Enter 1 or 2: \n')
    while choice!= '1' and choice!= '2':
        print('Please enter 1 or 2')
        choice = input('Enter 1 or 2: \n')

        if choice == '1':

            initial_savings = input('Enter the initial savings amount in euros: ')
            monthly_savings = input('Enter the monthly savings amount in euros: ')
            target_goal = input('Enter the target saving goal in euros: ')
            annual_interest_rate = input('Enter the annual interest rate as a percentage: ')
            monthly_savings_percentage = input('Enter the monthly savings percentage: ')
            years_to_financial_freedom = calculate_years_to_financial_freedom(initial_savings,
                monthly_savings, target_goal, annual_interest_rate, monthly_savings_percentage)
            print(f'Hi these {name}! The number of years it takes \
                  to reach financial freedom is: {years_to_financial_freedom}')

        elif choice == '2':

            initial_savings = input('Enter the initial savings amount in euros: ')
            target_goal = input('Enter the target goal in euros: ')
            annual_interest_rate = input('Enter the annual interest rate as a percentage: ')
            monthly_savings_percentage = input('Enter the monthly savings percentage: ')

            required_monthly_savings = calculate_required_monthly_savings()
            print(f'Hi these {name}! The amount you need to save every \
                  month to reach financial freedom is: {required_monthly_savings}')
