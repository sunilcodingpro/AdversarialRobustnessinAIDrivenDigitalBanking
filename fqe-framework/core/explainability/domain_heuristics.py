"""
Domain heuristics for explainability in FQE Framework.
Provides domain-specific rules and heuristics.
"""

class DomainHeuristics:
    def __init__(self, rules=None):
        self.rules = rules or {}

    def apply(self, explanation):
        """
        Applies domain heuristics to the explanation.
        """
        modified_explanation = explanation.copy()
        for feature, rule in self.rules.items():
            if feature in modified_explanation:
                modified_explanation[feature] = rule(modified_explanation[feature])
        return modified_explanation
