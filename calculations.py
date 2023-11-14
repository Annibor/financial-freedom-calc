class CalcYearsToFinancialFreedom:
    def __init__(self, initial_savings, monthly_savings, financial_goal, annual_interest, monthly):
        try:
            self.initial_savings = float(initial_savings)
            self.monthly_savings = float(monthly_savings)
            self.financial_goal = float(financial_goal)
            self.annual_interest = float(annual_interest)
            self.monthly_savings_percent = float(monthly_savings_percent)
        except ValueError:
            raise ValueError('Invalid input.Answers must be numeric values. Please try again.\n')
        
    
    def calc_years_to_financial_freedom(self):
        """
        Calculates the years it takes to reach the finanicial freedom.

        """
      while initial_savings < self.financial_goal:
        
