"""
Result class represents the result of a client call.
"""

class Result:
    """
    Result contains the following attributes:
    - message: a message string containing the description of the result
    - response: a RubyAem::Response response from AEM
    - data: the data payload, which can be of any type depending on the API call
    e.g. is_* and exists method provide result with boolean data.
    Some API calls result doesn't contain any data.
    """

    def __init__(self, message, response, data=None):
        """
        Initialise a result.

        :param message: result message
        :param response: HTTP response
        :return PythonAEM Result instance
        """
        self.message = message
        self.response = response
        self.data = data
