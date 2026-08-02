"""
==========================================================
Model Utilities
==========================================================

Loads:
1. Trained ANN Model
2. Standard Scaler
3. Label Encoder
4. One-Hot Encoder

Author  : Milind Chavan
Project : Customer Churn Analytics Dashboard
"""

from pathlib import Path
import pickle

import streamlit as st
import tensorflow as tf

from config import (
    MODEL_PATH,
    SCALER_PATH,
    LABEL_ENCODER_PATH,
    GEO_ENCODER_PATH,
)


# ==========================================================
# File Validation
# ==========================================================

def validate_artifacts() -> None:
    """
    Validate that all required model artifacts exist.

    Raises
    ------
    FileNotFoundError
        If any required artifact is missing.
    """

    artifact_paths = [
        MODEL_PATH,
        SCALER_PATH,
        LABEL_ENCODER_PATH,
        GEO_ENCODER_PATH,
    ]

    missing_files = [path for path in artifact_paths if not Path(path).exists()]

    if missing_files:

        message = "\n".join(str(file) for file in missing_files)

        raise FileNotFoundError(
            f"The following artifact(s) were not found:\n\n{message}"
        )


# ==========================================================
# Load ANN Model
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_model():
    """
    Load the trained ANN model.

    Returns
    -------
    tensorflow.keras.Model
        Loaded Keras model.
    """

    validate_artifacts()

    return tf.keras.models.load_model(MODEL_PATH)


# ==========================================================
# Load Preprocessing Objects
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_preprocessing():
    """
    Load preprocessing artifacts.

    Returns
    -------
    tuple
        (
            label_encoder_gender,
            onehot_encoder_geography,
            scaler
        )
    """

    validate_artifacts()

    with open(LABEL_ENCODER_PATH, "rb") as file:
        label_encoder_gender = pickle.load(file)

    with open(GEO_ENCODER_PATH, "rb") as file:
        onehot_encoder_geography = pickle.load(file)

    with open(SCALER_PATH, "rb") as file:
        scaler = pickle.load(file)

    return (
        label_encoder_gender,
        onehot_encoder_geography,
        scaler,
    )


# ==========================================================
# Load Everything
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_artifacts():
    """
    Load all model artifacts.

    Returns
    -------
    tuple
        (
            model,
            label_encoder_gender,
            onehot_encoder_geography,
            scaler
        )
    """

    model = load_model()

    (
        label_encoder_gender,
        onehot_encoder_geography,
        scaler,
    ) = load_preprocessing()

    return (
        model,
        label_encoder_gender,
        onehot_encoder_geography,
        scaler,
    )