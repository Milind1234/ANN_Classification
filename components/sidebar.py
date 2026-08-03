"""
==========================================================
Sidebar Component

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st

from config import (
    MODEL_NAME,
    MODEL_VERSION,
    AUTHOR,
    FRAMEWORK,
    ACCURACY,
    PRECISION,
    RECALL,
    F1_SCORE,
    ROC_AUC,
)

# ==========================================================
# Sidebar Component
# ==========================================================


def render_sidebar() -> None:
    """
    Render the application sidebar.
    """

    st.sidebar.title("🏦 Customer Churn Analytics")

    st.sidebar.markdown("---")

    # ======================================================
    # Model Information
    # ======================================================

    st.sidebar.subheader("🧠 Model Information")

    st.sidebar.info(
        f"""
**Model**

{MODEL_NAME}

**Version**

{MODEL_VERSION}

**Framework**

{FRAMEWORK}
"""
    )

    st.sidebar.markdown("---")

    # ======================================================
    # Performance
    # ======================================================

    st.sidebar.subheader("📊 Model Performance")

    st.sidebar.metric(
        "Accuracy",
        f"{ACCURACY:.2%}",
    )

    st.sidebar.metric(
        "Precision",
        f"{PRECISION:.2%}",
    )

    st.sidebar.metric(
        "Recall",
        f"{RECALL:.2%}",
    )

    st.sidebar.metric(
        "F1 Score",
        f"{F1_SCORE:.2%}",
    )

    st.sidebar.metric(
        "ROC-AUC",
        f"{ROC_AUC:.2%}",
    )

    st.sidebar.markdown("---")

    # ======================================================
    # Architecture
    # ======================================================

    st.sidebar.subheader("⚙ Model Configuration")

    st.sidebar.write("Learning Rate : **0.01**")

    st.sidebar.write("Batch Size : **16**")

    st.sidebar.write("Optimizer : **RMSprop**")

    st.sidebar.write("Activation : **ELU**")

    st.sidebar.write("Dropout : **0.40**")

    st.sidebar.write("Hidden Layers : **32 → 16 → 1**")

    st.sidebar.markdown("---")

    # ======================================================
    # Navigation
    # ======================================================

    st.sidebar.subheader("🧭 Navigation")

    st.sidebar.success(
        """
🏠 Home

📊 Dashboard

📈 Model Performance

📋 Batch Prediction

ℹ️ About
"""
    )

    st.sidebar.markdown("---")

    # ======================================================
    # Developer
    # ======================================================

    st.sidebar.subheader("👨‍💻 Developer")

    st.sidebar.write(AUTHOR)

    st.sidebar.caption("Customer Churn Analytics v2.0")