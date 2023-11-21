"""
Import needed for the code
"""
from calculations import check_if_exit
from calculations import CalcYearsToFinancialFreedom
from calculations import CalcRequiredMonthlySavings


def user_data():
    """
    Get user data and welcome to the program.

    Returns:
         str: User's name.
    """
    print('Welcome to the financial freedom calculator!\n')
    name = input('Please enter your name: \n')
    print(f'Hello {name}!\n')
    check_if_exit(name)

    # This gives user a introduction to the calculator.
    print('This program will calculate the number of years it takes'
          'to reach finanicial freedom, or how much you need to save'
          'each month to reach the finanicial freedom in a certain years.\n')
    return name


def choose_what_to_calc():
    """
    Choose what to calculate.

    Returns:
        Object: Instance of either CalcYearsTiFinancialFreedom
        or CalcRequiredMothlySavings.
    """
    print('Please choose what you want to calculate:\n')
    print('1. How many years it takes to reach the finanicial freedom\n')
    print('2. How much you need to save each month to reach the finanicial'
          'freedom in a certain years\n')
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
            print(f'Thank you {user_name}, for using'
                  'the Financial Freedom Calculator.'
                  'See you next time! \n')
            break


def main():
    """
    Main function that calls the run_calc function
    that will make the calculation available for the user.
    """
    run_calc()


if __name__ == '__main__':
    main()
