"""
==========================================================
Charts Utility

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import plotly.graph_objects as go

from config import (
    LOW_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
)


# ==========================================================
# Probability Gauge
# ==========================================================

def create_probability_gauge(
    probability: float,
) -> go.Figure:
    """
    Create a Plotly gauge chart showing
    customer churn probability.

    Parameters
    ----------
    probability : float
        Predicted churn probability.

    Returns
    -------
    plotly.graph_objects.Figure
    """

    figure = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=probability * 100,

            number={

                "suffix": "%",

                "font": {

                    "size": 42

                }

            },

            title={

                "text": "Churn Probability",

                "font": {

                    "size": 24

                }

            },

            gauge={

                "axis": {

                    "range": [0, 100]

                },

                "bar": {

                    "color": "#2563EB"

                },

                "steps": [

                    {
                        "range": [0, LOW_RISK_THRESHOLD * 100],
                        "color": "#22C55E",
                    },

                    {
                        "range": [
                            LOW_RISK_THRESHOLD * 100,
                            MEDIUM_RISK_THRESHOLD * 100,
                        ],
                        "color": "#FACC15",
                    },

                    {
                        "range": [
                            MEDIUM_RISK_THRESHOLD * 100,
                            100,
                        ],
                        "color": "#EF4444",
                    },

                ],

                "threshold": {

                    "line": {

                        "color": "black",

                        "width": 5

                    },

                    "value": probability * 100,

                },

            },

        )

    )

    figure.update_layout(

        height=420,

        margin=dict(

            l=20,
            r=20,
            t=60,
            b=20,

        ),

    )

    return figure