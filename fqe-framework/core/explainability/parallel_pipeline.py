"""
Parallel Explainability Pipeline for FQE Framework.
Runs multiple explainers in parallel for robustness.
"""
from concurrent.futures import ThreadPoolExecutor

class ParallelExplainabilityPipeline:
    def __init__(self, explainers):
        self.explainers = explainers  # Dict of {name: explainer instance}

    def run(self, X):
        with ThreadPoolExecutor() as executor:
            futures = {name: executor.submit(exp.explain, X) for name, exp in self.explainers.items()}
            results = {name: future.result() for name, future in futures.items()}
        return results
