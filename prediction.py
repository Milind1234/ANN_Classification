"""
==========================================================
Prediction Pipeline
==========================================================

Responsible for:

1. Data Validation
2. Feature Encoding
3. Feature Scaling
4. ANN Prediction
5. Risk Classification

Author  : Milind Chavan
Project : Customer Churn Analytics Dashboard
"""

from dataclasses import dataclass
from typing import Dict

import pandas as pd

from config import (
    CHURN_THRESHOLD,
    LOW_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
)


# ==========================================================
# Customer Data Model
# ==========================================================

@dataclass
class CustomerData:
    """
    Represents a single customer's information.
    """

    geography: str
    gender: str
    age: int
    credit_score: int
    tenure: int
    balance: float
    num_of_products: int
    has_credit_card: int
    is_active_member: int
    estimated_salary: float


# ==========================================================
# Validate Customer Data
# ==========================================================

def validate_customer(customer: CustomerData) -> None:
    """
    Validate customer information.

    Raises
    ------
    ValueError
        If any value is invalid.
    """

    if customer.age < 18:
        raise ValueError("Age must be at least 18.")

    if customer.credit_score < 300:
        raise ValueError("Credit Score must be >= 300.")

    if customer.balance < 0:
        raise ValueError("Balance cannot be negative.")

    if customer.estimated_salary < 0:
        raise ValueError("Salary cannot be negative.")

    if customer.num_of_products not in [1, 2, 3, 4]:
        raise ValueError("Products must be between 1 and 4.")


# ==========================================================
# Risk Level
# ==========================================================

def get_risk_level(probability: float) -> str:
    """
    Return customer risk category.
    """

    if probability < LOW_RISK_THRESHOLD:
        return "Low Risk"

    elif probability < MEDIUM_RISK_THRESHOLD:
        return "Medium Risk"

    else:
        return "High Risk"


# ==========================================================
# Prediction Function
# ==========================================================

def predict_customer(
    customer: CustomerData,
    model,
    scaler,
    gender_encoder,
    geography_encoder,
) -> Dict:
    """
    Predict customer churn.

    Returns
    -------
    dict
        Prediction results.
    """

    validate_customer(customer)

    input_df = pd.DataFrame(
        {
            "CreditScore": [customer.credit_score],
            "Gender": [
                gender_encoder.transform(
                    [customer.gender]
                )[0]
            ],
            "Age": [customer.age],
            "Tenure": [customer.tenure],
            "Balance": [customer.balance],
            "NumOfProducts": [
                customer.num_of_products
            ],
            "HasCrCard": [
                customer.has_credit_card
            ],
            "IsActiveMember": [
                customer.is_active_member
            ],
            "EstimatedSalary": [
                customer.estimated_salary
            ],
        }
    )

    geo_encoded = geography_encoder.transform(
        [[customer.geography]]
    )

    try:

        geo_encoded = geo_encoded.toarray()

    except AttributeError:

        pass

    geo_df = pd.DataFrame(

        geo_encoded,

        columns=geography_encoder.get_feature_names_out(
            ["Geography"]
        ),

    )

    input_df = pd.concat(

        [

            input_df.reset_index(drop=True),

            geo_df.reset_index(drop=True),

        ],

        axis=1,

    )

    input_scaled = scaler.transform(input_df)

    probability = float(

        model.predict(
            input_scaled,
            verbose=0,
        )[0][0]

    )

    prediction = (

        "Likely to Churn"

        if probability >= CHURN_THRESHOLD

        else "Not Likely to Churn"

    )

    risk = get_risk_level(probability)

    confidence = max(
        probability,
        1 - probability
    )

    return {

        "prediction": prediction,

        "probability": probability,

        "confidence": confidence,

        "risk": risk,

        "processed_features": input_df,

    }