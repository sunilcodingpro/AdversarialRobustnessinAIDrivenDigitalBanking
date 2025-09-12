"""
Constrained SHAP module for FQE Framework.
Implements domain-specific constraints for SHAP explanations.
"""

import shap
import numpy as np

class ConstrainedSHAP:
    def __init__(self, model, background_data, feature_names, constraints=None):
        self.model = model
        self.background_data = background_data
        self.feature_names = feature_names
        self.constraints = constraints or {}
        self.explainer = shap.Explainer(model, background_data)

    def explain(self, data_row):
        """
        Explains prediction for a single row using SHAP with domain constraints.
        """
        shap_values = self.explainer(np.array([data_row]))
        result = dict(zip(self.feature_names, shap_values.values[0]))
        # Apply constraints if any
        for feature, rule in self.constraints.items():
            if feature in result:
                result[feature] = rule(result[feature])
        return result
