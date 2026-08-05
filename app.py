"""
==========================================================
Customer Churn Analytics
Home Page

Author  : Milind Chavan
==========================================================
"""

import streamlit as st

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE,
    MODEL_NAME,
    MODEL_VERSION,
    FRAMEWORK,
    DEVELOPER,
    ACCURACY,
    PRECISION,
    RECALL,
    F1_SCORE,
    ROC_AUC,
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE,
)

# ==========================================================
# Load CSS
# ==========================================================

from pathlib import Path

css_path = Path(__file__).parent / "style.css"

if css_path.exists():

    with open(css_path, encoding="utf-8") as css:

        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )
# ==========================================================
# Header
# ==========================================================

st.title("🏦 Customer Churn Analytics")

st.caption(
    "Artificial Neural Network • TensorFlow • Streamlit"
)

st.divider()

# ==========================================================
# Project Overview
# ==========================================================

st.header("📌 Project Overview")

st.write(
    """
This application predicts whether a bank customer is likely
to churn using a **Hyperparameter Tuned Artificial Neural
Network (ANN)**.

The project demonstrates an end-to-end Machine Learning
workflow including:

- Data preprocessing
- Feature engineering
- Artificial Neural Networks
- Hyperparameter tuning
- Model evaluation
- Streamlit deployment
"""
)

# ==========================================================
# Model Performance
# ==========================================================

st.header("📊 Model Performance")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric(
        "Accuracy",
        f"{ACCURACY:.2%}"
    )

with c2:
    st.metric(
        "Precision",
        f"{PRECISION:.2%}"
    )

with c3:
    st.metric(
        "Recall",
        f"{RECALL:.2%}"
    )

with c4:
    st.metric(
        "F1 Score",
        f"{F1_SCORE:.2%}"
    )

with c5:
    st.metric(
        "ROC-AUC",
        f"{ROC_AUC:.2%}"
    )

st.divider()

# ==========================================================
# Model Information
# ==========================================================

st.header("🧠 Model Information")

info_col1, info_col2 = st.columns(2)

with info_col1:

    st.info(
        f"""
### 🤖 Model Details

**Model Name**

{MODEL_NAME}

**Version**

{MODEL_VERSION}
"""
    )

with info_col2:

    st.info(
        f"""
### ⚙️ Technical Information

**Framework**

{FRAMEWORK}

**Developer**

{DEVELOPER}
"""
    )

st.divider()
# ==========================================================
# Navigation
# ==========================================================

st.header("🚀 Navigate")

st.write(
    """
Use the navigation menu on the left to explore the application.

### Available Pages

- 📊 Dashboard
- 📈 Model Performance
- 📋 Batch Prediction
- ℹ️ About
"""
)

st.success(
    "Start by opening the 📊 Dashboard page."
)

st.divider()

# ==========================================================
# Footer
# ==========================================================

st.caption(
    "Customer Churn Analytics • Version 2.0"
)