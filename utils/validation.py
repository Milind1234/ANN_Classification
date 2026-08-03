"""
==========================================================
Validation Utility

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from prediction import CustomerData

from config import (
    MIN_AGE,
    MAX_AGE,
    MIN_CREDIT_SCORE,
    MAX_CREDIT_SCORE,
    MIN_BALANCE,
    MIN_SALARY,
    MIN_PRODUCTS,
    MAX_PRODUCTS,
    MIN_TENURE,
    MAX_TENURE,
)

# ==========================================================
# Validate Customer Input
# ==========================================================

def validate_customer_input(customer: CustomerData) -> list[str]:
    """
    Validate customer information.

    Parameters
    ----------
    customer : CustomerData

    Returns
    -------
    list[str]
        List of validation errors.
        Empty list indicates valid input.
    """

    errors = []

    # ------------------------------------------------------
    # Age
    # ------------------------------------------------------

    if not (MIN_AGE <= customer.age <= MAX_AGE):
        errors.append(
            f"Age must be between {MIN_AGE} and {MAX_AGE}."
        )

    # ------------------------------------------------------
    # Credit Score
    # ------------------------------------------------------

    if not (
        MIN_CREDIT_SCORE
        <= customer.credit_score
        <= MAX_CREDIT_SCORE
    ):
        errors.append(
            f"Credit Score must be between "
            f"{MIN_CREDIT_SCORE} and "
            f"{MAX_CREDIT_SCORE}."
        )

    # ------------------------------------------------------
    # Balance
    # ------------------------------------------------------

    if customer.balance < MIN_BALANCE:
        errors.append(
            "Balance cannot be negative."
        )

    # ------------------------------------------------------
    # Estimated Salary
    # ------------------------------------------------------

    if customer.estimated_salary < MIN_SALARY:
        errors.append(
            "Estimated Salary cannot be negative."
        )

    # ------------------------------------------------------
    # Products
    # ------------------------------------------------------

    if not (
        MIN_PRODUCTS
        <= customer.num_of_products
        <= MAX_PRODUCTS
    ):
        errors.append(
            f"Number of Products must be between "
            f"{MIN_PRODUCTS} and "
            f"{MAX_PRODUCTS}."
        )

    # ------------------------------------------------------
    # Tenure
    # ------------------------------------------------------

    if not (
        MIN_TENURE
        <= customer.tenure
        <= MAX_TENURE
    ):
        errors.append(
            f"Tenure must be between "
            f"{MIN_TENURE} and "
            f"{MAX_TENURE} years."
        )

    return errors