"""
Import needed for the code
"""
import gspread
from google.oauth2.service_account import Credentials
from calculations import check_if_exit
from calculations import CalcYearsToFinancialFreedom
from calculations import CalcRequiredMonthlySavings


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
    check_if_exit(name)

    print('This program will calculate the number of years it takes'
          'to reach finanicial freedom, or how much you need to save'
          'each month to reach the finanicial freedom in a certain years.\n')
    return name

def choose_what_to_calc():
    """
    Choose what to calculate.
    """
    print('Please choose what you want to calculate:\n')
    print('1. How many years it takes to reach the finanicial freedom\n')
    print('2. How much you need to save each month to reach the finanicial'
          'freedom in a certain years\n')
    choice = input('Enter your choice: \n')
    check_if_exit(choice)

    if choice == '1':
        initial_savings = float(input('Please enter your initial savings in euro: \n'))
        monthly_savings = float(input('Please enter your monthly savings in euro: \n'))
        financial_goal = float(input('Please enter your financial goal in euro: \n'))
        annual_interest = float(input('Please enter your annual interest rate: \n'))
        monthly_savings_percent = float(input('Please enter your monthly savings percentage: \n'))
        years_to_financial_freedom = CalcYearsToFinancialFreedom(initial_savings, monthly_savings, financial_goal, annual_interest, monthly_savings_percent)

        return years_to_financial_freedom
    elif choice == '2':
        initial_savings_two = float(input('Please enter your initial savings in euro: \n'))
        target_goal_two = float(input('Please enter your target goal in euro: \n'))
        taget_years_to_freedom = float(input('Please enter your taget years to freedom: \n'))
        required_monthly_savings = CalcRequiredMonthlySavings(initial_savings_two, target_goal_two, taget_years_to_freedom)

        return required_monthly_savings
    else:
        print('Invalid choice. Please try again.\n')
        choose_what_to_calc()

def run_calc():
    user_name = user_data()
    
    while True:
        calculation_choice = choose_what_to_calc()

        if isinstance(calculation_choice, CalcYearsToFinancialFreedom):
            result = calculation_choice.calc_years_to_financial_freedom()
            print(f'{user_name}, it will take {result} years to reach the finanicial freedom.\n')

        elif isinstance(calculation_choice, CalcRequiredMonthlySavings):
            result = calculation_choice.calc_required_monthly_savings()
            print(f'{user_name}, you will need to save {result:.2f} euros every month to reach your financial goal.\n')

        repeat = input('Do you want to make a new calculation? (yes/no): ').lower()
        check_if_exit(repeat)

        if repeat != 'yes':
            print(f'Thank you {user_name}, for using the Financial Freedom Calculator. See you next time! \n')
            break

run_calc()



