# This code is based on two different sources:
# one by ismailmoufid47, available at GitHu(link in README.md )
# and one by Akash3121, available at GitHub (link in README.md).
"""
Import needed for the code
"""
import re
import uuid
# googlesheets imports are adapted from Code Institutes
# Love Sandwiches (Link in README.md).
import gspread
from google.oauth2.service_account import Credentials
from calculations import check_if_exit
from calculations import CalcYearsToFinancialFreedom
from calculations import CalcRequiredMonthlySavings

# SCOPE are adapted from Code Institutes Love Sandwiches,
# (Link in README.md).
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# CREDS,SCOPED_CREDS, GSPREAD_CLIENT & SHEET are
# adapted from Code Institute Love Sandwiches (Link in README.md).
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('financial-freedom-calc')


def update_user_worksheet(user_id, user_data_list):
    """Update the user worksheet. Add new
    information to the worksheet from user input.
    """
    # The code for the googlesheet update with input information
    # are based on Code Institutes Love Sandwiches, (Link in README.md).
    print('Update the user worksheet...')
    user_worksheet = SHEET.worksheet('user_sheet')
    user_worksheet.append_row([user_id] + user_data_list)
    print('User worksheet updated\n')


def update_financial_worksheet_one(user_id, financial_data_list_one):
    """
    Update the financial worksheet one. Add new
    information to the worksheet from user inputs in choice one.
    """
    # The code for the googlesheet update with input information
    # are based on Code Institutes Love Sandwiches, (Link in README.md).
    print('Update the financial worksheet...')
    financial_worksheet = SHEET.worksheet('financial_sheet_one')
    financial_worksheet.append_row([user_id] + financial_data_list_one)
    print('Financial worksheet updated\n')


def update_financial_worksheet_two(user_id, financial_data_list_two):
    """
    Update the financial worksheet two. Add new
    information to the worksheet from user inputs in choice two.
    """
    # The code for the googlesheet update with input information
    # are based on Code Institutes Love Sandwiches, (Link in README.md).
    print('Update the financial worksheet...')
    financial_worksheet = SHEET.worksheet('financial_sheet_two')
    financial_worksheet.append_row([user_id] + financial_data_list_two)
    print('Financial worksheet updated\n')


def is_email_valid(email):
    """
    Validate email address using regular expression.
    """
    # This email validation is based on Max O'Didilys
    # youtube tutorial, link in README.md file.
    email_patterns = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(email_patterns, email) is not None


def user_data():
    """
    Get user data and welcome to the program.
    And update the google worksheet with user data.
    """
    print('Welcome to the financial freedom calculator!\n')
    name = input('Please enter your name: \n')
    check_if_exit(name)

    # This email validation is based on Max O'Didilys
    # youtube tutorial, link in README.md file.
    while True:
        email = input('Please enter your email address: \n')
        check_if_exit(email)

        if is_email_valid(email):
            break
        else:
            print('Invalid email address. Please enter valid email. \n')
    while True:
        age = input('Please enter your age: \n')
        check_if_exit(age)

        if age.isdigit():
            break
        else:
            print('Invalid age. Please enter valid age (numeric value). \n')

    user_id = str(uuid.uuid4())
    user_data_list = [name, age, email]
    update_user_worksheet(user_id, user_data_list)

    print(f"""
Hello {name}!\n
This program will calculate the number of years it takes
to reach financial freedom, or how much you need to save
each month to reach your financial freedom within a
certain amount of years.\n
    """)

    return user_id, user_data_list


def choose_what_to_calc(user_id):
    """
    Makes the user choose what type of calcualtion they
    want to do. Calcualation 1 or calculation 2.
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

            # Check if initial savings are equal or grater than
            # the financial target goal.
            if initial_savings >= financial_goal:
                print('Congratulations! You have already '
                      'reached you financial goal.')
                return None

            years_to_financial_freedom = (CalcYearsToFinancialFreedom(
                initial_savings, monthly_savings, financial_goal))
            financial_data_list_one = [initial_savings, monthly_savings,
                                       financial_goal]
            update_financial_worksheet_one(user_id, financial_data_list_one)

            return years_to_financial_freedom
        except ValueError:
            # Shows error message if user enters anything else than digits.
            print('Invalid input. Answers must be numeric values.'
                  'Please try again.\n')
            return choose_what_to_calc(user_id)
    elif choice == '2':
        try:
            # Get user inputs for the second calculation.
            initial_savings_two = (float(input(
                'Please enter your initial savings in euro: \n')))
            target_goal_two = (float(input(
                'Please enter your target goal in euro: \n')))

            # Check if initial savings are equal or grater
            # than the financial target goal.
            if initial_savings_two >= target_goal_two:
                print('Congratulations! You have already '
                      'reached you financial goal.')
                return None

            target_years_to_freedom = (float(input(
                'Please enter your taget years to freedom: \n')))
            required_monthly_savings = (CalcRequiredMonthlySavings(
                initial_savings_two, target_goal_two, target_years_to_freedom))
            financial_data_list_two = [initial_savings_two, target_goal_two,
                                       target_years_to_freedom]
            update_financial_worksheet_two(user_id, financial_data_list_two)

            return required_monthly_savings
        except ValueError:
            # Shows error message if user enters anything else than digits.
            print('Invalid input. Answers must be numeric values.'
                  'Please try again.\n')
            return choose_what_to_calc(user_id)
    else:
        print('Invalid choice. Please try again.\n')
        choose_what_to_calc(user_id)


def run_calc(user_id):
    """
    Make the user select if they want to make another
    claculation or if they want to exit.
    """
    # makes only users name show in the prints.
    # makes only users name show in the prints.
    user_sheet = SHEET.worksheet('user_sheet')
    user_name_cell = user_sheet.find(user_id)
    user_name = user_sheet.cell(user_name_cell.row, 2).value

    calculation1_complete = False
    calculation2_complete = False

    while True:
        calculation_choice = choose_what_to_calc(user_id)

        if isinstance(calculation_choice, CalcYearsToFinancialFreedom):
            # This will show the results of the first calculation
            # for the user, and the name the user added in
            # the beginning of the program will be shown.
            result = calculation_choice.calc_years_to_financial_freedom()
            print(f"""
{user_name}, it will take {result:.2f} years
to reach the finanicial freedom.\n
""")
            calculation1_complete = True

        elif isinstance(calculation_choice, CalcRequiredMonthlySavings):
            # This will show the results of the second calculation
            # for the user, and the name the user added in
            # the beginning of the program will be shown.
            result = calculation_choice.calc_required_monthly_savings()
            print(f"""
{user_name}, you will need to save
{result:.2f} euros every month to reach
your financial goal.\n""")
            calculation2_complete = True

        # This will give the user a choice if user wants
        # to make another calculation or not.
        repeat = (input('Do you want to make a new calculation? '
                        '(yes/no): \n').lower())
        check_if_exit(repeat)

        if repeat != 'yes':
            print(f"""
Thank you {user_name}, for using
the Financial Freedom Calculator.
See you next time! \n""")
            break

    if not calculation1_complete or not calculation2_complete:
        print("Adding placeholders for incomplete calculations...\n")
        if not calculation1_complete:
            update_financial_worksheet_one(user_id, ['Placeholder'] * 3)
        if not calculation2_complete:
            update_financial_worksheet_two(user_id, ['Placeholder'] * 3)


def main():
    """
    Main function that calls the run_calc function
    that will make the calculation available for the user.
    """
    user_id, *_ = user_data()
    run_calc(user_id)


if __name__ == '__main__':
    main()
