import unittest
from mortgage.mortgage import Mortgage
from mortgage.payment_frequency import PaymentFrequency

class TestMortgageInit(unittest.TestCase):
    """Unit tests for the __init__ method of the Mortgage class."""

    def test_type_error_loan_amount_not_numeric(self):
        with self.assertRaises(TypeError):
            Mortgage("100000", 0.05, 25, PaymentFrequency.MONTHLY)

    def test_value_error_loan_amount_zero(self):
        with self.assertRaises(ValueError):
            Mortgage(0, 0.05, 25, PaymentFrequency.MONTHLY)

    def test_value_error_loan_amount_negative(self):
        with self.assertRaises(ValueError):
            Mortgage(-50000, 0.05, 25, PaymentFrequency.MONTHLY)

    def test_type_error_interest_rate_not_numeric(self):
        with self.assertRaises(TypeError):
            Mortgage(100000, "0.05", 25, PaymentFrequency.MONTHLY)

    def test_value_error_interest_rate_negative(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, -0.01, 25, PaymentFrequency.MONTHLY)

    def test_value_error_interest_rate_zero(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 0, 25, PaymentFrequency.MONTHLY)

    def test_value_error_interest_rate_above_one(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 1.5, 25, PaymentFrequency.MONTHLY)

    def test_value_error_invalid_amortization(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 0.05, 12, PaymentFrequency.MONTHLY)

    def test_value_error_invalid_frequency(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 0.05, 25, 999)

    def test_object_initializes_private_attributes(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage._Mortgage__loan_amount, 100000)
        self.assertEqual(mortgage._Mortgage__annual_interest_rate, 0.05)
        self.assertEqual(mortgage._Mortgage__amortization, 25)
        self.assertEqual(mortgage._Mortgage__frequency, PaymentFrequency.MONTHLY)

class TestMortgageLoanAmount(unittest.TestCase):
    """Unit tests for Mortgage class loan_amount property."""

    def test_loan_amount_setter_type_error(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        with self.assertRaises(TypeError):
            mortgage.loan_amount = "abc"

    def test_loan_amount_setter_value_error_zero(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        with self.assertRaises(ValueError):
            mortgage.loan_amount = 0

    def test_loan_amount_setter_value_error_negative(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        with self.assertRaises(ValueError):
            mortgage.loan_amount = -100

    def test_loan_amount_setter_updates_state(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        mortgage.loan_amount = 150000
        self.assertEqual(mortgage._Mortgage__loan_amount, 150000)

    def test_loan_amount_getter_returns_state(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.loan_amount, 100000)

class TestMortgageAnnualInterestRate(unittest.TestCase):
    """Unit tests for Mortgage class annual_interest_rate property."""

    def test_interest_rate_setter_type_error(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        with self.assertRaises(TypeError):
            mortgage.annual_interest_rate = "abc"

    def test_interest_rate_setter_value_error_negative(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        with self.assertRaises(ValueError):
            mortgage.annual_interest_rate = -0.05

    def test_interest_rate_setter_value_error_zero(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        with self.assertRaises(ValueError):
            mortgage.annual_interest_rate = 0

    def test_interest_rate_setter_value_error_above_one(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        with self.assertRaises(ValueError):
            mortgage.annual_interest_rate = 1.5

    def test_interest_rate_setter_updates_state(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        mortgage.annual_interest_rate = 0.045
        self.assertEqual(
            mortgage._Mortgage__annual_interest_rate, 0.045
        )

    def test_interest_rate_getter_returns_state(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.annual_interest_rate, 0.05)

class TestMortgageAmortization(unittest.TestCase):
    """Unit tests for Mortgage class amortization property."""

    def test_amortization_setter_value_error(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        with self.assertRaises(ValueError):
            mortgage.amortization = 12  # invalid amortization

    def test_amortization_setter_updates_state(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        mortgage.amortization = 20
        self.assertEqual(mortgage._Mortgage__amortization, 20)

    def test_amortization_getter_returns_state(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.amortization, 25)
