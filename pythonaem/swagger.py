"""
Swagger class contains logic related to swaggeraem.
"""

import re

def operation_to_method(operation):
    """
    Convert pythonaem spec's operation (consistent with Swagger spec's operationId)
    into swaggeraem's generated method name.

    :param operation: operation ID
    :return swaggeraem method name
    """
    return re.sub(r'(?<=[a-z])(?=[A-Z])', '_', operation).lower()
