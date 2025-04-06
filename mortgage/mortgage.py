from .payment_frequency import PaymentFrequency

class Mortgage:
    """Represents a mortgage loan used to purchase real estate."""

    __amortization_years = [5, 10, 15, 20, 25, 30]

    def __init__(self, loan_amount: float, annual_interest_rate: float,
                 amortization: int, frequency: PaymentFrequency):
        """
        Initializes a Mortgage object with loan details.

        Args:
            loan_amount (float): The mortgage loan amount.
            annual_interest_rate (float): The interest rate (0 < rate <= 1).
            amortization (int): Years to repay the loan.
            frequency (PaymentFrequency): Payments per year.

        Raises:
            TypeError: If loan amount or interest rate is not numeric.
            ValueError: If values are outside accepted ranges.
        """
        # Validate loan_amount
        if not isinstance(loan_amount, (int, float)):
            raise TypeError("Loan amount must be a value of a numeric type.")
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be a value greater than zero.")

        # Validate annual_interest_rate
        if not isinstance(annual_interest_rate, (int, float)):
            raise TypeError("Annual interest rate must be a value of a numeric type.")
        if annual_interest_rate <= 0 or annual_interest_rate > 1:
            raise ValueError("Annual interest rate must be a value greater than zero "
                             "and less than or equal to 1.")

        # Validate amortization
        if amortization not in Mortgage.__amortization_years:
            raise ValueError("Amortization must be a value in [5, 10, 15, 20, 25, 30].")

        # Validate frequency
        if frequency not in PaymentFrequency:
            raise ValueError("Frequency must be a value of PaymentFrequency type.")

        self.__loan_amount = loan_amount
        self.__annual_interest_rate = annual_interest_rate
        self.__amortization = amortization
        self.__frequency = frequency
