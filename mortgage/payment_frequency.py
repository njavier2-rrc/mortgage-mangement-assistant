from enum import Enum

class PaymentFrequency(Enum):
    """Represents the payment frequencies of a mortgage."""
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52
