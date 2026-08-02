"""
==========================================================
Formatting Utility

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from datetime import datetime

from config import (
    LOW_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
)


# ==========================================================
# Percentage Formatting
# ==========================================================

def format_percentage(value: float) -> str:
    """
    Format decimal value as percentage.

    Example
    -------
    0.856 -> 85.60%
    """

    return f"{value:.2%}"


# ==========================================================
# Currency Formatting
# ==========================================================

def format_currency(value: float) -> str:
    """
    Format value as Indian currency.
    """

    return f"₹ {value:,.2f}"


# ==========================================================
# Boolean Formatting
# ==========================================================

def format_boolean(value: bool) -> str:
    """
    Convert boolean to Yes / No.
    """

    return "Yes" if value else "No"


# ==========================================================
# Prediction Label
# ==========================================================

def format_prediction(probability: float) -> str:
    """
    Convert probability to prediction label.
    """

    if probability >= 0.50:
        return "Likely to Churn"

    return "Not Likely to Churn"


# ==========================================================
# Risk Level
# ==========================================================

def format_risk(probability: float) -> str:
    """
    Convert probability to risk label.
    """

    if probability < LOW_RISK_THRESHOLD:
        return "🟢 Low Risk"

    if probability < MEDIUM_RISK_THRESHOLD:
        return "🟡 Medium Risk"

    return "🔴 High Risk"


# ==========================================================
# Confidence
# ==========================================================

def format_confidence(probability: float) -> float:
    """
    Calculate model confidence.
    """

    return max(probability, 1 - probability)


# ==========================================================
# Date and Time
# ==========================================================

def format_datetime() -> str:
    """
    Return current date and time.
    """

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )