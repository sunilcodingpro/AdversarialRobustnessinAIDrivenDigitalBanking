"""
Constrained SHAP module for FQE Framework explainability.
Applies SHAP under regulatory and domain constraints.
"""
import shap

class ConstrainedSHAP:
    def __init__(self, model, constraints=None):
        self.model = model
        self.constraints = constraints or {}

    def explain(self, X):
        """
        Generates SHAP values with applied constraints.

        Args:
            X: Input samples.

        Returns:
            shap_values: SHAP values with constraints applied.
        """
        explainer = shap.Explainer(self.model, X)
        shap_values = explainer(X)
        # Apply constraints (e.g., mask sensitive features)
        if self.constraints.get("mask_features"):
            for feature in self.constraints["mask_features"]:
                idx = list(X.columns).index(feature)
                shap_values.values[:, idx] = 0
        return shap_values