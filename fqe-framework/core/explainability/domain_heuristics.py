"""
Domain Heuristics module for FQE Framework explainability.
Implements rule-based reasoning for feature importance in financial models.
"""

class DomainHeuristics:
    def __init__(self, feature_metadata):
        self.feature_metadata = feature_metadata

    def score_features(self, input_data):
        """
        Assigns importance scores to features based on domain rules.

        Args:
            input_data (dict): Input features.

        Returns:
            dict: Feature importance scores.
        """
        scores = {}
        for feature, value in input_data.items():
            if feature in self.feature_metadata.get("key_risk_factors", []):
                scores[feature] = 1.0
            elif feature in self.feature_metadata.get("moderate_factors", []):
                scores[feature] = 0.5
            else:
                scores[feature] = 0.1
        return scores
