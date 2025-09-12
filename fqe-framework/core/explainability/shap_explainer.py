"""
SHAP Explainer module for FQE Framework.
Provides local and global model interpretability using SHAP.
"""

import shap
import numpy as np

class SHAPExplainer:
    def __init__(self, model, background_data):
        self.model = model
        self.background_data = background_data
        self.explainer = shap.Explainer(model, background_data)

    def explain(self, data_row):
        """
        Explains prediction for a single row using SHAP.
        """
        shap_values = self.explainer(np.array([data_row]))
        return shap_values.values[0], shap_values.data[0]