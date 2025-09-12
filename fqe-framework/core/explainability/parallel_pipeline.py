"""
Parallel pipeline for combining multiple explainability methods in FQE Framework.
"""

from concurrent.futures import ThreadPoolExecutor

class ParallelPipeline:
    def __init__(self, explainers):
        self.explainers = explainers

    def explain(self, data_row):
        """
        Runs all explainers in parallel and returns their results.
        """
        results = {}
        with ThreadPoolExecutor() as executor:
            future_to_name = {
                executor.submit(explainer.explain, data_row): name
                for name, explainer in self.explainers.items()
            }
            for future in future_to_name:
                name = future_to_name[future]
                results[name] = future.result()
        return results
