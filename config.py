"""
==========================================================
Configuration File
Customer Churn Analytics Dashboard
==========================================================

Author  : Milind Chavan
Project : Customer Churn Prediction using ANN
Model   : Hyperparameter Tuned Artificial Neural Network
"""

from pathlib import Path

# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

ASSETS_DIR = PROJECT_ROOT / "assets"

DATA_DIR = PROJECT_ROOT / "data"

LOGS_DIR = PROJECT_ROOT / "logs"

EXPORTS_DIR = PROJECT_ROOT / "exports"

# ==========================================================
# MODEL ARTIFACTS
# ==========================================================

MODEL_PATH = ARTIFACTS_DIR / "customer_churn_final_optimized.keras"

SCALER_PATH = ARTIFACTS_DIR / "scaler.pkl"

LABEL_ENCODER_PATH = ARTIFACTS_DIR / "label_encoder_gender.pkl"

GEO_ENCODER_PATH = ARTIFACTS_DIR / "geography_ohe.pkl"

BEST_PARAMETERS_PATH = ARTIFACTS_DIR / "best_hyperparameters.json"

# ==========================================================
# STREAMLIT CONFIGURATION
# ==========================================================

PAGE_TITLE: str = "Customer Churn Analytics Dashboard"

PAGE_ICON: str = "🏦"

LAYOUT: str = "wide"

SIDEBAR_STATE: str = "expanded"

# ==========================================================
# MODEL INFORMATION
# ==========================================================

MODEL_NAME = "Artificial Neural Network (ANN)"

MODEL_VERSION = "2.0.0"

FRAMEWORK = "TensorFlow 2.19.1 • Keras"

DEVELOPER = "Milind Chavan"

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

ACCURACY = 0.8560
PRECISION = 0.7692
RECALL = 0.3817
F1_SCORE = 0.5102
ROC_AUC = 0.8595

MODEL_METRICS = {
    "Accuracy": ACCURACY,
    "Precision": PRECISION,
    "Recall": RECALL,
    "F1 Score": F1_SCORE,
    "ROC-AUC": ROC_AUC,
}

# ==========================================================
# BEST HYPERPARAMETERS
# ==========================================================

LEARNING_RATE = 0.01

BATCH_SIZE = 16

OPTIMIZER = "RMSprop"

ACTIVATION = "ELU"

DROPOUT = 0.40

HIDDEN_LAYERS = (32, 16)

OUTPUT_NEURONS = 1

BEST_HYPERPARAMETERS = {

    "Learning Rate": LEARNING_RATE,

    "Batch Size": BATCH_SIZE,

    "Optimizer": OPTIMIZER,

    "Activation": ACTIVATION,

    "Dropout": DROPOUT,

    "Hidden Layers": HIDDEN_LAYERS,

}

# ==========================================================
# PREDICTION THRESHOLDS
# ==========================================================

CHURN_THRESHOLD: float = 0.50

LOW_RISK_THRESHOLD: float = 0.30

MEDIUM_RISK_THRESHOLD: float = 0.60

# ==========================================================
# INPUT RANGES
# ==========================================================

MIN_AGE = 18

MAX_AGE = 92

MIN_CREDIT_SCORE = 300

MAX_CREDIT_SCORE = 900

MIN_BALANCE = 0.0

MIN_SALARY = 0.0

MIN_PRODUCTS = 1

MAX_PRODUCTS = 4

MIN_TENURE = 0

MAX_TENURE = 10

# ==========================================================
# INPUT RANGES
# ==========================================================

MIN_AGE = 18

MAX_AGE = 92

MIN_CREDIT_SCORE = 300

MAX_CREDIT_SCORE = 900

MIN_BALANCE = 0.0

MIN_SALARY = 0.0

MIN_PRODUCTS = 1

MAX_PRODUCTS = 4

MIN_TENURE = 0

MAX_TENURE = 10

# ==========================================================
# INPUT FEATURES
# ==========================================================

INPUT_FEATURES = (
    "CreditScore",
    "Gender",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "HasCrCard",
    "IsActiveMember",
    "EstimatedSalary",
    "Geography",
)

# ==========================================================
# UI COLORS
# ==========================================================

PRIMARY_COLOR = "#2563EB"

SECONDARY_COLOR = "#1E40AF"

SUCCESS_COLOR = "#16A34A"

WARNING_COLOR = "#F59E0B"

DANGER_COLOR = "#DC2626"

BACKGROUND_COLOR = "#F8FAFC"

CARD_COLOR = "#FFFFFF"

TEXT_COLOR = "#0F172A"

SECONDARY_TEXT = "#475569"

BORDER_COLOR = "#CBD5E1"

# ==========================================================
# FILE EXPORTS
# ==========================================================

CSV_REPORT_NAME = "customer_churn_prediction_report.csv"

PDF_REPORT_NAME = "customer_churn_prediction_report.pdf"

# ==========================================================
# RANDOM SEED
# ==========================================================

RANDOM_STATE = 42

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

PROJECT_NAME = "Customer Churn Analytics"

PROJECT_VERSION = "2.0.0"

PROJECT_DESCRIPTION = (
    "Customer Churn Prediction using "
    "Artificial Neural Networks"
)

# ==========================================================
# APP SETTINGS
# ==========================================================

ENABLE_DEBUG = False

ENABLE_LOGGING = True

SHOW_PROCESSED_FEATURES = True

SHOW_CONFIDENCE_SCORE = True

LOG_FILE = LOGS_DIR / "application.log"