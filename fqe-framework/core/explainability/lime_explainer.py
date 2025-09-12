"""
LIME Explainer module for FQE Framework.
Provides local model interpretability using LIME.
"""

import lime
import lime.lime_tabular
import numpy as np

class LIMEExplainer:
    def __init__(self, model, training_data, feature_names):
        self.model = model
        self.training_data = training_data
        self.feature_names = feature_names
        self.explainer = lime.lime_tabular.LimeTabularExplainer(
            training_data,
            feature_names=feature_names,
            verbose=True,
            mode='regression'  # Change to 'classification' if needed
        )

    def explain(self, data_row):
        """
        Explains prediction for a single row using LIME.
        """
        exp = self.explainer.explain_instance(
            data_row,
            self.model.predict,
            num_features=len(self.feature_names)
        )
        return exp.as_list()