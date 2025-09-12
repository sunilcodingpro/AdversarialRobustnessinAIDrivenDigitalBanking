"""
GDPR Compliance Module for FQE Framework.
Implements basic checks and mechanisms to ensure GDPR data handling.
"""

def check_data_minimization(data, required_fields):
    """
    Checks that only required fields are present in the data for GDPR minimization.
    """
    minimized_data = {field: data[field] for field in required_fields if field in data}
    return minimized_data

def pseudonymize(data, fields_to_pseudonymize):
    """
    Pseudonymizes specified fields for GDPR compliance.
    """
    return {k: (f"pseudo_{hash(v)}" if k in fields_to_pseudonymize else v) for k, v in data.items()}