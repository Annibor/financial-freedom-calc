"""
Calclulations for the financial freedom Calculator.
"""
class CalcYearsToFinancialFreedom:
    """
    Calculates the number of years it takes to reach the finanicial freedom.
    """
    def __init__(self, initial_savings, monthly_savings, financial_goal, annual_interest, monthly_savings_percent):
        try:
            self.initial_savings = float(initial_savings)
            self.monthly_savings = float(monthly_savings)
            self.financial_goal = float(financial_goal)
            self.annual_interest = float(annual_interest)
            self.monthly_savings_percent = float(monthly_savings_percent)
        except ValueError as exc:
            raise ValueError('Invalid input.Answers must be numeric values. Please try again.\n') from exc


    def calc_years_to_financial_freedom(self):
        """
        Calculates the years it takes to reach the finanicial freedom.

        """
        years_to_target = 0
        current_savings = self.initial_savings
        while current_savings < self.financial_goal:
            monthly_interest = self.annual_interest / 12
            current_savings = current_savings + monthly_interest
            current_savings = current_savings * (1 + self.monthly_savings_percent)
            current_savings = current_savings + self.monthly_savings
            years_to_target += 1

        return years_to_target



class CalcRequiredMonthlySavings:
    """
    Calculates the required monthly savings to reazch a specific financial target.
    """
    def __init__(self, initial_savings_two, target_goal_two, monthly_savings_percent_two, annual_interest_two, target_years_to_freedom):
        try:
            self.initial_savings_two = float(initial_savings_two)
            self.target_goal_two = float(target_goal_two)
            self.monthly_savings_percent_two = float(monthly_savings_percent_two)
            self.annual_interest_two = float(annual_interest_two)
            self.target_years_to_freedom = float(target_years_to_freedom)
        except ValueError as exc:
            raise ValueError('Invalid input.Answers must be numeric values. Please try again.\n') from exc

    def calc_required_monthly_savings(self):
        """
        Calculates the required monthly savings to reazch a specifiv financial target.
        """
        monthly_savings_percent_two = self.monthly_savings_percent_two / 100 / 12
        periods = self.target_years_to_freedom * 12
        monthly_savings_required = (self.target_goal_two / ((1+ self.annual_interest_two / 12) ** periods - 1)) / monthly_savings_percent_two

        return monthly_savings_required
