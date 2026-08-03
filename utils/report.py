"""
==========================================================
Report Utility

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from datetime import datetime

import pandas as pd


# ==========================================================
# Prediction Report
# ==========================================================

def create_prediction_report(
    customer,
    probability: float,
    prediction: str,
    confidence: float,
    risk_level: str,
) -> pd.DataFrame:
    """
    Create a prediction report DataFrame.

    Parameters
    ----------
    customer : CustomerData
        Customer information.

    probability : float
        Predicted churn probability.

    prediction : str
        Prediction label.

    confidence : float
        Model confidence.

    risk_level : str
        Risk category.

    Returns
    -------
    pandas.DataFrame
        Report dataframe.
    """

    report = pd.DataFrame({

        "Prediction Time": [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ],

        "Prediction": [
            prediction
        ],

        "Probability (%)": [
            round(probability * 100, 2)
        ],

        "Confidence (%)": [
            round(confidence * 100, 2)
        ],

        "Risk Level": [
            risk_level
        ],

        "Geography": [
            customer.geography
        ],

        "Gender": [
            customer.gender
        ],

        "Age": [
            customer.age
        ],

        "Credit Score": [
            customer.credit_score
        ],

        "Tenure": [
            customer.tenure
        ],

        "Balance": [
            customer.balance
        ],

        "Products": [
            customer.num_of_products
        ],

        "Credit Card": [
            "Yes" if customer.has_credit_card else "No"
        ],

        "Active Member": [
            "Yes" if customer.is_active_member else "No"
        ],

        "Estimated Salary": [
            customer.estimated_salary
        ],

    })

    return report


# ==========================================================
# Convert Report to CSV
# ==========================================================

def report_to_csv(
    report: pd.DataFrame,
) -> bytes:
    """
    Convert report DataFrame to CSV.

    Parameters
    ----------
    report : pandas.DataFrame

    Returns
    -------
    bytes
    """

    return report.to_csv(
        index=False,
    ).encode("utf-8")