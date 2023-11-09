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
    print('This program will help you calculate the number of years it takes to reach financial freedom, or how much you need to save every month to reach financial freedom.')

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

get_user_data()

def calcualte_years_to_financial_freedom(initial_savings,
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
    print('1. Would you like to calculate the number of years it takes to reach financial freedom, or 2. how much you need to save every month to reach financial freedom? ')
    choice = input('Enter 1 or 2: \n')
    while choice!= '1' and choice!= '2':
        print('Please enter 1 or 2')
        choice = input('Enter 1 or 2: \n')
        
        if choice == '1':
        
      
          