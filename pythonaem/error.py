"""
PythonAEM error, contains a message and PythonAEM Result object
"""

class Error(RuntimeError):
    """
    PythonAEM error, contains a message and PythonAEM Result object
    useful for debugging the result and response when an error occurs
    """

    def __init__(self, message, result):
        """
        Initialise a result.

        :param message: result message
        :param resi;t: PythonAEM Result
        :return PythonAEM Error instance
        """
        super().__init__()
        self.message = message
        self.result = result
