"""
==========================================================
Prediction Metrics Component

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st

from config import (
    LOW_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
)


# ==========================================================
# Prediction Metrics
# ==========================================================

def render_prediction_metrics(
    probability: float,
) -> None:
    """
    Render detailed prediction metrics and business
    recommendations.

    Parameters
    ----------
    probability : float
        Predicted churn probability.
    """

    confidence = max(
        probability,
        1 - probability,
    )

    st.subheader("📈 Prediction Analysis")

    # ======================================================
    # Confidence
    # ======================================================

    st.metric(
        label="Model Confidence",
        value=f"{confidence:.2%}",
    )

    st.markdown("---")

    # ======================================================
    # Risk Interpretation
    # ======================================================

    if probability < LOW_RISK_THRESHOLD:

        st.success(
            "🟢 **Low Risk**\n\n"
            "The customer is unlikely to churn."
        )

        st.info(
            """
### Recommended Action

- Maintain customer relationship
- Offer premium banking services
- Continue regular engagement
"""
        )

    elif probability < MEDIUM_RISK_THRESHOLD:

        st.warning(
            "🟡 **Medium Risk**\n\n"
            "The customer has a moderate chance of churning."
        )

        st.warning(
            """
### Recommended Action

- Send personalized offers
- Encourage digital banking
- Provide loyalty rewards
- Monitor account activity
"""
        )

    else:

        st.error(
            "🔴 **High Risk**\n\n"
            "The customer is highly likely to churn."
        )

        st.error(
            """
### Recommended Action

- Immediate relationship manager follow-up
- Offer retention benefits
- Waive selected banking fees
- Provide exclusive banking offers
- Closely monitor customer activity
"""
        )

    st.markdown("---")

    # ======================================================
    # Probability Interpretation
    # ======================================================

    st.subheader("📊 Probability Interpretation")

    st.progress(float(probability))

    st.write(
        f"**Predicted Churn Probability:** "
        f"**{probability:.2%}**"
    )