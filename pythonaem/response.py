"""
Response wraps HTTP response data returned by swaggeraem.
"""

class Response:
    """
    Response wraps HTTP response data returned by swaggeraem.
    """

    def __init__(self, status_code, body, headers):
        """
        Initialise a result.

        :param status_code: HTTP status code
        :param body: HTTP response body
        :param headers: HTTP headers
        :return PythonAEM Response instance
        """
        self.status_code = status_code
        self.body = body
        self.headers = headers
