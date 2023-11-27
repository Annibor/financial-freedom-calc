"""
Calculations for the Financial Freedom Calculator.
"""


def check_if_exit(input_value):
    """
    Check if the input value is 'exit' and exit the calculator if true.
    """
    if input_value == 'exit':
        print('Exiting calculator, see you next time!')
        exit()


class CalcYearsToFinancialFreedom:
    """
    Calculates the number of years it takes to reach the finanicial freedom.
    """
    def __init__(self, initial_savings, monthly_savings, financial_goal):
        self.initial_savings = float(initial_savings)
        self.monthly_savings = float(monthly_savings)
        self.financial_goal = float(financial_goal)

    def calc_years_to_financial_freedom(self):
        """
        Calculates the years it takes to reach the finanicial freedom.

        """
        if self.monthly_savings >= self.financial_goal:
            return 0

        years_to_target = ((self.financial_goal - self.initial_savings)
                           / (self.monthly_savings * 12))

        return years_to_target


class CalcRequiredMonthlySavings:
    """
    Calculates the required monthly savings to
    reach a specific financial target.
    """
    def __init__(self, initial_savings_two, target_goal_two,
                 target_years_to_freedom):
        self.initial_savings_two = float(initial_savings_two)
        self.target_goal_two = float(target_goal_two)
        self.target_years_to_freedom = float(target_years_to_freedom)

    def calc_required_monthly_savings(self):
        """
        Calculates the required monthly savings to reazch
        a specifiv financial target.
        """
        periods = self.target_years_to_freedom * 12
        monthly_savings_required = ((self.target_goal_two -
                                     self.initial_savings_two)
                                    / periods)

        return monthly_savings_required
