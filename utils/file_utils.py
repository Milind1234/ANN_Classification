"""
==========================================================
File Utilities

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path

import pandas as pd

from config import EXPORTS_DIR


# ==========================================================
# Ensure Export Directory Exists
# ==========================================================

def ensure_export_directory() -> None:
    """
    Create the exports directory if it does not exist.
    """

    EXPORTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )


# ==========================================================
# Check File Exists
# ==========================================================

def file_exists(
    file_path: Path,
) -> bool:
    """
    Check whether a file exists.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    bool
    """

    return file_path.exists()


# ==========================================================
# Save DataFrame as CSV
# ==========================================================

def save_csv(
    dataframe: pd.DataFrame,
    filename: str,
) -> Path:
    """
    Save DataFrame as CSV.

    Parameters
    ----------
    dataframe : pd.DataFrame

    filename : str

    Returns
    -------
    Path
        Saved file path.
    """

    ensure_export_directory()

    output_path = EXPORTS_DIR / filename

    dataframe.to_csv(
        output_path,
        index=False,
    )

    return output_path


# ==========================================================
# Load CSV
# ==========================================================

def load_csv(
    file_path: Path,
) -> pd.DataFrame:
    """
    Load CSV file.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    pd.DataFrame
    """

    return pd.read_csv(file_path)


# ==========================================================
# Get File Size
# ==========================================================

def get_file_size(
    file_path: Path,
) -> float:
    """
    Return file size in KB.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    float
    """

    size = file_path.stat().st_size

    return round(
        size / 1024,
        2,
    )


# ==========================================================
# Get File Name
# ==========================================================

def get_filename(
    file_path: Path,
) -> str:
    """
    Return filename.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    str
    """

    return file_path.name


# ==========================================================
# Delete File
# ==========================================================

def delete_file(
    file_path: Path,
) -> bool:
    """
    Delete a file.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    bool
    """

    if file_path.exists():

        file_path.unlink()

        return True

    return False