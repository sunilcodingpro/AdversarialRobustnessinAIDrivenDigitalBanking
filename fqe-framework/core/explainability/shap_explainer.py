"""
SHAP Explainer module for FQE Framework.
Provides model interpretability using SHAP.
"""

import shap
import numpy as np

class SHAPExplainer:
    def __init__(self, model, background_data, feature_names):
        self.model = model
        self.background_data = background_data
        self.feature_names = feature_names
        self.explainer = shap.Explainer(model, background_data)

    def explain(self, data_row):
        """
        Explains prediction for a single row using SHAP.
        """
        shap_values = self.explainer(np.array([data_row]))
        return dict(zip(self.feature_names, shap_values.values[0]))
