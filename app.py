import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Custom CSS
# ==========================================================

st.markdown("""
<style>

/* ==========================================================
   HIDE STREAMLIT DEFAULT UI
========================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ==========================================================
   APP BACKGROUND
========================================================== */

.stApp {
    background: #F4F7FC;
}

/* ==========================================================
   TITLES
========================================================== */

.title {

    font-size:42px;

    font-weight:700;

    color:#0A3D62;

    text-align:center;

}

.subtitle{

    text-align:center;

    font-size:18px;

    color:#5A6B7B;

    margin-bottom:30px;

}

/* ==========================================================
   CARD
========================================================== */

.card{

    background:white;

    padding:25px;

    border-radius:18px;

    box-shadow:0px 6px 18px rgba(0,0,0,0.12);

    margin-bottom:20px;

}

/* ==========================================================
   SIDEBAR
========================================================== */

[data-testid="stSidebar"]{

    background:#1E293B;

}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3{

    color:white;

}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label{

    color:white;

}

/* ==========================================================
   BUTTON
========================================================== */

.stButton > button{

    background:#0A3D62;

    color:white;

    border:none;

    border-radius:10px;

    height:55px;

    font-size:18px;

    font-weight:600;

    transition:0.3s;

}

.stButton > button:hover{

    background:#145DA0;

    color:white;

}

.stButton > button:focus{

    background:#145DA0;

    color:white;

}

/* ==========================================================
   LABELS
========================================================== */

label{

    color:#1E293B !important;

    font-weight:600;

}

.stSlider label,
.stRadio label,
.stSelectbox label,
.stNumberInput label{

    color:#1E293B !important;

    font-weight:600;

}

/* ==========================================================
   INPUT BOXES
========================================================== */

input{

    color:#1E293B !important;

}

textarea{

    color:#1E293B !important;

}

/* ==========================================================
   SELECTBOX
========================================================== */

[data-baseweb="select"]{

    color:#1E293B;

}

/* ==========================================================
   METRICS
========================================================== */

[data-testid="stMetric"]{

    background:white;

    border-radius:12px;

    padding:20px;

    box-shadow:0px 5px 12px rgba(0,0,0,0.08);

}

[data-testid="stMetricLabel"]{

    color:#1E293B !important;

    font-size:15px;

}

[data-testid="stMetricValue"]{

    color:#0A3D62 !important;

    font-size:34px;

    font-weight:700;

}

/* ==========================================================
   DATAFRAME
========================================================== */

[data-testid="stDataFrame"]{

    border-radius:12px;

}

/* ==========================================================
   EXPANDER
========================================================== */

.streamlit-expanderHeader{

    font-size:18px;

    font-weight:bold;

    color:#0A3D62;

}

/* ==========================================================
   SUCCESS
========================================================== */

[data-testid="stAlert"]{

    border-radius:12px;

}

/* ==========================================================
   PROGRESS BAR
========================================================== */

.stProgress > div > div{

    background:#0A3D62;

}

/* ==========================================================
   DOWNLOAD BUTTON
========================================================== */

.stDownloadButton > button{

    background:#0A3D62;

    color:white;

    border-radius:10px;

    border:none;

}

.stDownloadButton > button:hover{

    background:#145DA0;

    color:white;

}

/* ==========================================================
   HEADINGS
========================================================== */

h1{

    color:#0A3D62;

}

h2{

    color:#0A3D62;

}

h3{

    color:#0A3D62;

}

h4{

    color:#0A3D62;

}

/* ==========================================================
   TABLE
========================================================== */

table{

    color:#1E293B;

}

/* ==========================================================
   RADIO / TOGGLE
========================================================== */

[data-testid="stRadio"]{

    color:#1E293B;

}

[data-testid="stToggle"]{

    color:#1E293B;

}

/* ==========================================================
   MARKDOWN
========================================================== */

p{

    color:#1E293B;

}

li{

    color:#1E293B;

}

/* ==========================================================
   FOOTER
========================================================== */

.footer{

    text-align:center;

    color:#0A3D62;

    font-size:16px;

    margin-top:40px;

    margin-bottom:20px;

}

</style>
""",
unsafe_allow_html=True)

# ==========================================================
# Load Model
# ==========================================================

@st.cache_resource

def load_model():

    return tf.keras.models.load_model(
        "customer_churn_final_optimized.keras"
    )


# ==========================================================
# Load Preprocessing Objects
# ==========================================================

@st.cache_resource

def load_preprocessing():

    with open("label_encoder_gender.pkl","rb") as f:
        gender_encoder=pickle.load(f)

    with open("geography_ohe.pkl","rb") as f:
        geo_encoder=pickle.load(f)

    with open("scaler.pkl","rb") as f:
        scaler=pickle.load(f)

    return gender_encoder,geo_encoder,scaler


model=load_model()

label_encoder_gender,\
onehot_encoder_geo,\
scaler=load_preprocessing()

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("🏦 Bank Dashboard")

st.sidebar.markdown("---")

st.sidebar.subheader("Model Information")

st.sidebar.info("""
Artificial Neural Network

TensorFlow + Keras

Hyperparameter Tuned
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Performance")

st.sidebar.metric("Accuracy","85.60%")

st.sidebar.metric("Precision","76.92%")

st.sidebar.metric("Recall","38.17%")

st.sidebar.metric("F1 Score","51.02%")

st.sidebar.metric("ROC-AUC","85.95%")

st.sidebar.markdown("---")

st.sidebar.subheader("Architecture")

st.sidebar.write("Learning Rate : 0.01")

st.sidebar.write("Batch Size : 16")

st.sidebar.write("Optimizer : RMSprop")

st.sidebar.write("Activation : ELU")

st.sidebar.write("Dropout : 0.4")

st.sidebar.write("Neurons : 32 → 16 → 1")

# ==========================================================
# Header
# ==========================================================

st.markdown(
"""
<div class='title'>
🏦 Customer Churn Prediction Dashboard
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='subtitle'>

Predict whether a customer is likely to leave the bank using a
Hyperparameter Tuned Artificial Neural Network.

</div>
""",
unsafe_allow_html=True
)

st.markdown("---")

# ==========================================================
# Customer Information
# ==========================================================

st.markdown(
"""
<div class="card">

<h2 style="color:#0A3D62;">
👤 Customer Information
</h2>

<p>
Enter the customer details below to predict whether the customer
is likely to churn.
</p>

</div>
""",
unsafe_allow_html=True
)

left_col, right_col = st.columns(2)

# ==========================================================
# Left Column
# ==========================================================

with left_col:

    st.subheader("📋 Personal Details")

    geography = st.selectbox(
        "🌍 Geography",
        onehot_encoder_geo.categories_[0]
    )

    gender = st.selectbox(
        "👤 Gender",
        label_encoder_gender.classes_
    )

    age = st.slider(
        "🎂 Age",
        min_value=18,
        max_value=92,
        value=35
    )

    credit_score = st.number_input(
        "💳 Credit Score",
        min_value=300,
        max_value=900,
        value=650
    )

    tenure = st.slider(
        "📅 Tenure (Years)",
        min_value=0,
        max_value=10,
        value=5
    )

# ==========================================================
# Right Column
# ==========================================================

with right_col:

    st.subheader("🏦 Banking Details")

    balance = st.number_input(
        "💰 Account Balance",
        min_value=0.0,
        value=50000.0,
        step=1000.0,
        format="%.2f"
    )

    estimated_salary = st.number_input(
        "💼 Estimated Salary",
        min_value=0.0,
        value=50000.0,
        step=1000.0,
        format="%.2f"
    )

    num_of_products = st.slider(
        "📦 Number of Products",
        min_value=1,
        max_value=4,
        value=2
    )

    has_cr_card = st.toggle(
        "💳 Has Credit Card",
        value=True
    )

    is_active_member = st.toggle(
        "🟢 Active Member",
        value=True
    )
# ==========================================================
# Convert Yes / No to 1 / 0
# ==========================================================

has_cr_card = int(has_cr_card)
is_active_member = int(is_active_member)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# Predict Button
# ==========================================================

predict_button = st.button(
    "🔍 Predict Customer Churn",
    use_container_width=True
)

# ==========================================================
# Prediction Engine
# ==========================================================

if predict_button:

    with st.spinner("Analyzing customer data..."):

        try:

            # ---------------------------------------------
            # Create Input DataFrame
            # ---------------------------------------------

            input_df = pd.DataFrame({

                "CreditScore": [credit_score],

                "Gender": [
                    label_encoder_gender.transform([gender])[0]
                ],

                "Age": [age],

                "Tenure": [tenure],

                "Balance": [balance],

                "NumOfProducts": [num_of_products],

                "HasCrCard": [has_cr_card],

                "IsActiveMember": [is_active_member],

                "EstimatedSalary": [estimated_salary]

            })

            # ---------------------------------------------
            # One Hot Encode Geography
            # ---------------------------------------------

            geo_encoded = onehot_encoder_geo.transform(
                [[geography]]
            )

            try:

                geo_encoded = geo_encoded.toarray()

            except AttributeError:

                pass

            geo_df = pd.DataFrame(

                geo_encoded,

                columns=onehot_encoder_geo.get_feature_names_out(
                    ["Geography"]
                )

            )

            # ---------------------------------------------
            # Merge Features
            # ---------------------------------------------

            input_df = pd.concat(
                [
                    input_df.reset_index(drop=True),
                    geo_df.reset_index(drop=True)
                ],
                axis=1
            )

            # ---------------------------------------------
            # Scale Features
            # ---------------------------------------------

            input_scaled = scaler.transform(input_df)

            # ---------------------------------------------
            # Prediction
            # ---------------------------------------------

            prediction = model.predict(
                input_scaled,
                verbose=0
            )

            probability = float(prediction[0][0])

            prediction_class = (
                "Likely to Churn"
                if probability >= 0.5
                else "Not Likely to Churn"
            )

            # ==========================================================
            # Results Dashboard
            # ==========================================================

            st.markdown("---")

            st.header("📊 Prediction Results")

            metric_col1, metric_col2, metric_col3 = st.columns(3)

            with metric_col1:

                st.metric(
                    "Churn Probability",
                    f"{probability:.2%}"
                )

            with metric_col2:

                st.metric(
                    "Prediction",
                    prediction_class
                )

            with metric_col3:

                confidence = max(
                    probability,
                    1 - probability
                )

                st.metric(
                    "Confidence",
                    f"{confidence:.2%}"
                )

            st.markdown("### 📈 Churn Probability")

            st.progress(float(probability))

            # ==========================================================
            # Risk Level
            # ==========================================================

            if probability < 0.30:

                risk = "🟢 LOW RISK"

                st.success(
                    "Customer has a LOW probability of churning."
                )

            elif probability < 0.60:

                risk = "🟡 MEDIUM RISK"

                st.warning(
                    "Customer has a MEDIUM probability of churning."
                )

            else:

                risk = "🔴 HIGH RISK"

                st.error(
                    "Customer has a HIGH probability of churning."
                )

            st.markdown(f"## {risk}")

            # ==========================================================
            # Customer Summary
            # ==========================================================

            st.markdown("---")

            st.subheader("👤 Customer Summary")

            summary = pd.DataFrame({

                "Feature":[
                    "Geography",
                    "Gender",
                    "Age",
                    "Credit Score",
                    "Balance",
                    "Products",
                    "Credit Card",
                    "Active Member",
                    "Estimated Salary"
                ],

                "Value":[
                    geography,
                    gender,
                    age,
                    credit_score,
                    f"₹ {balance:,.2f}",
                    num_of_products,
                    "Yes" if has_cr_card else "No",
                    "Yes" if is_active_member else "No",
                    f"₹ {estimated_salary:,.2f}"
                ]

            })

            st.dataframe(
                summary,
                use_container_width=True,
                hide_index=True
            )

            # ==========================================================
            # Recommendation Engine
            # ==========================================================

            st.markdown("---")

            st.subheader("💡 Recommended Business Action")

            if probability >= 0.60:

                st.error("""
            ### Immediate Retention Recommended

            - 📞 Contact customer personally
            - 💳 Offer premium banking benefits
            - 🎁 Provide loyalty rewards
            - 💰 Offer cashback or fee waiver
            - 📈 Monitor customer activity closely
                """)

            elif probability >= 0.30:

                st.warning("""
            ### Customer Needs Attention

            - 📧 Send promotional email
            - 💵 Offer personalized loan rates
            - 🎯 Recommend suitable banking products
            - ⭐ Encourage digital banking usage
                """)

            else:

                st.success("""
            ### Customer Appears Stable

            - ✅ Continue regular services
            - 😊 Maintain customer satisfaction
            - 🎉 Offer optional premium services
                """)

            # ==========================================================
            # Processed Features
            # ==========================================================

            with st.expander("⚙ View Processed Features"):

                st.dataframe(
                    input_df,
                    use_container_width=True
                )

            # ==========================================================
            # Probability Interpretation
            # ==========================================================

            st.markdown("---")

            st.subheader("📉 Probability Interpretation")

            if probability < 0.30:

                st.info("""
### 🟢 Low Risk

The customer shows strong signs of remaining with the bank.

**Recommended Strategy**

- Maintain current relationship
- Continue excellent customer service
- Offer premium banking products if appropriate
                """)

            elif probability < 0.60:

                st.warning("""
### 🟡 Medium Risk

The customer has moderate chances of churning.

**Recommended Strategy**

- Personalized offers
- Promotional Emails
- Cashback Rewards
- Monitor account activity
                """)

            else:

                st.error("""
### 🔴 High Risk

The customer is highly likely to churn.

**Recommended Strategy**

- Contact Relationship Manager
- Retention Campaign
- Exclusive Banking Benefits
- Fee Waiver / Cashback
- Immediate Follow-up
                """)

            # ==========================================================
            # Download Prediction Report
            # ==========================================================

            st.markdown("---")

            st.subheader("📄 Prediction Report")

            report = pd.DataFrame({

                "Prediction":[prediction_class],

                "Probability":[round(probability*100,2)],

                "Risk":[risk],

                "Credit Score":[credit_score],

                "Age":[age],

                "Balance":[balance],

                "Estimated Salary":[estimated_salary],

                "Products":[num_of_products],

                "Active Member":[
                    "Yes" if is_active_member else "No"
                ]

            })

            csv = report.to_csv(index=False)

            st.download_button(

                "⬇ Download Prediction Report",

                csv,

                file_name="prediction_report.csv",

                mime="text/csv"

            )

            # ==========================================================
            # Dashboard Summary
            # ==========================================================

            st.markdown("---")

            st.subheader("📊 Dashboard Summary")

            c1,c2,c3 = st.columns(3)

            with c1:

                st.metric(
                    "Risk Level",
                    risk
                )

            with c2:

                st.metric(
                    "Customer Age",
                    age
                )

            with c3:

                st.metric(
                    "Credit Score",
                    credit_score
                )

            # ==========================================================
            # Footer
            # ==========================================================

            st.markdown("---")

            st.markdown("""
            <div class="footer">
            
            <h2>🏦 Customer Churn Prediction Dashboard</h2>

            <p><b>Developed by Milind Chavan</b></p>

            <p>
            Artificial Neural Network • TensorFlow • Keras • Streamlit
            </p>

            </div>
            """, unsafe_allow_html=True)

        except Exception as e:

            st.error(e)

            st.stop()


