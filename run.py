"""
Import needed for the code
"""
from calculations import CalcYearsToFinancialFreedom
from calculations import CalcRequiredMonthlySavings
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
        initial_savings = float(input('Please enter your initial savings: \n'))
        monthly_savings = float(input('Please enter your monthly savings: \n'))
        financial_goal = float(input('Please enter your financial goal: \n'))
        annual_interest = float(input('Please enter your annual interest rate: \n'))
        monthly_savings_percent = float(input('Please enter your monthly savings percentage: \n'))
        years_to_financial_freedom = CalcYearsToFinancialFreedom(initial_savings, monthly_savings, financial_goal, annual_interest, monthly_savings_percent)

        return years_to_financial_freedom
    elif choice == '2':
        initial_savings_two = float(input('Please enter your initial savings: \n'))
        target_goal_two = float(input('Please enter your target goal: \n'))
        monthly_savings_percent_two = float(input('Please enter your monthly savings percentage: \n'))
        annual_interest_two = float(input('Please enter your annual interest rate: \n'))
        taget_years_to_freedom = float(input('Please enter your taget years to freedom: \n'))
        required_monthly_savings = CalcRequiredMonthlySavings(initial_savings_two, target_goal_two, monthly_savings_percent_two, annual_interest_two, taget_years_to_freedom)

        return required_monthly_savings
    else:
        print('Invalid choice. Please try again.\n')
        choose_what_to_calc()

    