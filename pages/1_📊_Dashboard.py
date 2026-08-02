"""
==========================================================
Customer Churn Analytics Dashboard

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

import streamlit as st

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE,
)
from utils.formatting import (
    format_percentage,
)

from model_utils import load_artifacts

from components.sidebar import render_sidebar
from components.forms import render_customer_form
from components.cards import render_prediction_cards
from components.metrics import render_prediction_metrics

from prediction import predict_customer

from utils.validation import validate_customer_input
from utils.charts import create_probability_gauge
from utils.report import (
    create_prediction_report,
    report_to_csv,
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
# Load Global CSS
# ==========================================================

css_file = (
    Path(__file__).resolve().parent.parent
    / "style.css"
)

if css_file.exists():

    with open(css_file, encoding="utf-8") as file:

        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True,
        )

# ==========================================================
# Load Model Artifacts
# ==========================================================

try:

    (
        model,
        gender_encoder,
        geography_encoder,
        scaler,
    ) = load_artifacts()

except Exception as error:

    st.error("❌ Unable to load application artifacts.")

    st.exception(error)

    st.stop()

# ==========================================================
# Session State
# ==========================================================

if "prediction_result" not in st.session_state:

    st.session_state.prediction_result = None

# ==========================================================
# Sidebar
# ==========================================================

render_sidebar()

# ==========================================================
# Dashboard Header
# ==========================================================

st.title("🏦 Customer Churn Analytics Dashboard")

st.caption(
    "Artificial Neural Network • TensorFlow 2.19.1 • Hyperparameter Tuned"
)

st.divider()

# ==========================================================
# Introduction
# ==========================================================

st.info(
    """
Welcome to the **Customer Churn Analytics Dashboard**.

This application uses a **Hyperparameter Tuned Artificial Neural Network (ANN)** to predict whether a customer is likely to leave the bank.

### Workflow

1. Enter customer information
2. Validate the inputs
3. Generate churn prediction
4. Analyze probability and risk
5. Download prediction report
"""
)

# ==========================================================
# Customer Input Form
# ==========================================================

customer, predict_button = render_customer_form(
    geography_encoder=geography_encoder,
    gender_encoder=gender_encoder,
)

# ==========================================================
# Prediction Pipeline
# ==========================================================

if predict_button:

    with st.spinner("Analyzing customer information..."):

        try:

            # --------------------------------------------------
            # Validate Customer Input
            # --------------------------------------------------

            validation_errors = validate_customer_input(customer)

            if validation_errors:

                for error in validation_errors:

                    st.error(error)

                st.stop()

            # --------------------------------------------------
            # ANN Prediction
            # --------------------------------------------------

            prediction_result = predict_customer(

                customer=customer,

                model=model,

                scaler=scaler,

                gender_encoder=gender_encoder,

                geography_encoder=geography_encoder,

            )

            # --------------------------------------------------
            # Save Result in Session
            # --------------------------------------------------

            st.session_state.prediction_result = {

                "customer": customer,

                **prediction_result,

            }

        except Exception as error:

            st.error("Prediction failed.")

            st.exception(error)

            st.stop()

# ==========================================================
# Retrieve Prediction Result
# ==========================================================

result = st.session_state.prediction_result

if result is None:

    st.stop()

# ==========================================================
# Extract Prediction Values
# ==========================================================

customer = result["customer"]

prediction = result["prediction"]

probability = result["probability"]

confidence = result["confidence"]

risk = result["risk"]

processed_features = result["processed_features"]

# ==========================================================
# Prediction Results
# ==========================================================

st.divider()

st.header("📊 Prediction Results")

# ==========================================================
# KPI Cards
# ==========================================================

render_prediction_cards(
    probability=probability,
)

# ==========================================================
# Probability Gauge
# ==========================================================

st.markdown("---")

st.subheader("📈 Churn Probability Gauge")

gauge = create_probability_gauge(
    probability=probability,
)

st.plotly_chart(
    gauge,
    use_container_width=True,
)

# ==========================================================
# Prediction Analysis
# ==========================================================

st.markdown("---")

render_prediction_metrics(
    probability=probability,
)

# ==========================================================
# Customer Profile
# ==========================================================

st.markdown("---")

st.subheader("👤 Customer Profile")

profile_df = create_prediction_report(
    customer=customer,
    probability=probability,
    prediction=prediction,
    confidence=confidence,
    risk_level=risk,
)

display_profile = profile_df.drop(
    columns=[
        "Prediction Time",
        "Prediction",
        "Probability (%)",
        "Confidence (%)",
        "Risk Level",
    ]
).T.reset_index()

display_profile.columns = [
    "Customer Profile",
    "Value",
]

st.dataframe(
    display_profile,
    use_container_width=True,
    hide_index=True,
)

# ==========================================================
# Export Prediction Report
# ==========================================================

st.markdown("---")

st.subheader("📄 Export Prediction Report")

csv_data = report_to_csv(profile_df)

st.download_button(
    label="⬇ Download Prediction Report",
    data=csv_data,
    file_name="customer_churn_prediction_report.csv",
    mime="text/csv",
    use_container_width=True,
)

# ==========================================================
# Processed Features
# ==========================================================

st.markdown("---")

with st.expander(
    "⚙ View Processed Features",
    expanded=False,
):

    st.dataframe(
        processed_features,
        use_container_width=True,
        hide_index=True,
    )

# ==========================================================
# Prediction Information
# ==========================================================

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.info(
        f"""
### 🧠 Prediction

**{prediction}**
"""
    )

with col2:

    st.info(
        f"""
### 🎯 Risk Category

**{risk}**
"""
    )

# ==========================================================
# Footer
# ==========================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:20px;">

<h3>🏦 Customer Churn Analytics Dashboard</h3>

<p>
Version <b>2.0.0</b>
</p>

<p>
Developed by <b>Milind Chavan</b>
</p>

<p>
TensorFlow • Keras • Streamlit • Plotly
</p>

</div>
""",
unsafe_allow_html=True,
)