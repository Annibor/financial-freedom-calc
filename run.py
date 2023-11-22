#This code is based on two different sources:
# one by ismailmoufid47, available at GitHu(link in README.md )
# and one by Akash3121, available at GitHub (link in README.md).
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

def update_user_worksheet(user_data_list):
    """Update the user worksheet. Add new
    information to the worksheet from user input.
    """
    print('Update the user worksheet...\n')
    user_worksheet = SHEET.worksheet('user_sheet')
    user_worksheet.append_row(user_data_list)

def update_financial_worksheet():
     """Update the financial worksheet. Add new
    information to the worksheet from user input.
    """
    print('Update the financial worksheet...\n')
    financail_worksheet = SHEET.worksheet('financial_sheet')
    finanacial_worksheet.append_row(financial_data_list)

def user_data():
    """
    Get user data and welcome to the program.

    Returns:
         str: User's name.
    """
    print('Welcome to the financial freedom calculator!\n')
    name = input('Please enter your name: \n')
    check_if_exit(name)
    email = input('Please enter your email address: \n')
    check_if_exit(email)
    age = input('Please enter your age: \n')
    check_if_exit(age)

    user_data_list = [name, age, email]
    update_user_worksheet(user_data_list)
    print(f'Hello {name}!\n')

    # This gives user a introduction to the calculator.
    print('This program will calculate the number of years it takes'
          'to reach finanicial freedom, or how much you need to save'
          'each month to reach the finanicial freedom in a certain years.\n')
    return user_data_list


def choose_what_to_calc():
    """
    Choose what to calculate.

    Returns:
        Object: Instance of either CalcYearsTiFinancialFreedom
        or CalcRequiredMothlySavings.
    """
    print("""
Please choose what you want to calculate:\n
1. How many years it takes to reach the finanicial freedom\n
2. How much you need to save each month to reach the finanicial
freedom in a certain years\n
    """)
    choice = input('Enter your choice: \n')
    check_if_exit(choice)

    if choice == '1':
        try:
            # Get user inputs for the first calcualtion.
            initial_savings = (float(input(
                'Please enter your initial savings in euro: \n')))
            monthly_savings = (float(input(
                'Please enter your monthly savings in euro: \n')))
            financial_goal = (float(input(
                'Please enter your financial goal in euro: \n')))
            years_to_financial_freedom = (CalcYearsToFinancialFreedom(
                initial_savings, monthly_savings, financial_goal))
            return years_to_financial_freedom
        except ValueError:
            # Shows error message if user enters anything else than digits.
            print('Invalid input. Answers must be numeric values.'
                  'Please try again.\n')
            return choose_what_to_calc()
    elif choice == '2':
        try:
            # Get user inputs for the second calculation.
            initial_savings_two = (float(input(
                'Please enter your initial savings in euro: \n')))
            target_goal_two = (float(input(
                'Please enter your target goal in euro: \n')))
            taget_years_to_freedom = (float(input(
                'Please enter your taget years to freedom: \n')))
            required_monthly_savings = (CalcRequiredMonthlySavings(
                initial_savings_two, target_goal_two, taget_years_to_freedom))
            return required_monthly_savings
        except ValueError:
            # Shows error message if user enters anything else than digits.
            print('Invalid input. Answers must be numeric values.'
                  'Please try again.\n')
            return choose_what_to_calc()
    else:
        print('Invalid choice. Please try again.\n')
        choose_what_to_calc()


def run_calc():
    """
    Make the user select if they want to make another
    claculation or if they want to exit.
    """
    user_name = user_data()

    while True:
        calculation_choice = choose_what_to_calc()

        if isinstance(calculation_choice, CalcYearsToFinancialFreedom):
            # This will show the results of the first calculation
            # for the user, and the name the user added in
            # the beginning of the program will be shown.
            result = calculation_choice.calc_years_to_financial_freedom()
            print(f'{user_name}, it will take {result:.2f} years '
                  'to reach the finanicial freedom.\n')

        elif isinstance(calculation_choice, CalcRequiredMonthlySavings):
            # This will show the results of the second calculation
            # for the user, and the name the user added in
            # the beginning of the program will be shown.
            result = calculation_choice.calc_required_monthly_savings()
            print(f'{user_name}, you will need to save {result:.2f} euros '
                  'every month to reach your financial goal.\n')

        # This will give the user a choice if user wants
        # to make another calculation or not.
        repeat = (input('Do you want to make a new calculation?'
                        '(yes/no): ').lower())
        check_if_exit(repeat)

        if repeat != 'yes':
            print(f"""Thank you {user_name}, for using
the Financial Freedom Calculator.
See you next time! \n""")
            break


def main():
    """
    Main function that calls the run_calc function
    that will make the calculation available for the user.
    """
    run_calc()


if __name__ == '__main__':
    main()
