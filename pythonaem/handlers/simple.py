"""
Response handlers for no payload.
"""
import json
from ..error import Error
from ..result import Result


class SimpleHandler:
    """
    Response handlers for no payload.
    """

    def __init__(self, response, response_spec, call_params):
        self.response = response
        self.response_spec = response_spec
        self.call_params = call_params

    def simple(self):
        """
        Simple handler by returning result that contains status and message as
        configured in conf/spec.yaml AS-IS.

        :param response: HTTP response containing status_code, body, and headers
        :param response_spec: response specification as configured in conf/spec.yaml
        :param call_params: API call parameters
        :return PythonAEM Result
        """
        response_message = self.response_spec['message'].format(**self.call_params)
        return Result(response_message, self.response)

    def simple_true(self):
        """
        Simple handler with boolean true result data.

        :param response: HTTP response containing status_code, body, and headers
        :param response_spec: response specification as configured in conf/spec.yaml
        :param call_params: API call parameters
        :return PythonAEM Result
        """
        result = self.simple()
        result.data = True
        return result

    def simple_false(self):
        """
        Simple handler with boolean false result data.

        :param response: HTTP response containing status_code, body, and headers
        :param response_spec: response specification as configured in conf/spec.yaml
        :param call_params: API call parameters
        :return PythonAEM Result
        """
        result = self.simple()
        result.data = False
        return result

    def simple_nil(self):
        """
        Simple handler with nil result data.

        :param response: HTTP response containing status_code, body, and headers
        :param response_spec: response specification as configured in conf/spec.yaml
        :param call_params: API call parameters
        :return RubyAem::Result
        """
        result = self.simple()
        result.data = None
        return result

    def simple_error(self):
        """
        Simple handler with raised error.

        :param response: HTTP response containing status_code, body, and headers
        :param response_spec: response specification as configured in conf/spec.yaml
        :param call_params: API call parameters
        :return RubyAem::Result
        """
        response_message = self.response_spec['message'].format(**self.call_params)
        result = self.simple()
        print(response_message)
        raise Error(response_message, result)

    def simple_body(self):
        """
        Simple handler with response body as result data.

        :param response: HTTP response containing status_code, body, and headers
        :param response_spec: response specification as configured in conf/spec.yaml
        :param call_params: API call parameters
        :return PythonAEM Result
        """
        result = self.simple()
        result.data = self.response.body
        return result

    def json_aem_health_check(self):
        """
        Handle AEM Health Check Servlet JSON payload.

        :param response: HTTP response containing status_code, body, and headers
        :param response_spec: response specification as configured in conf/spec.yaml
        :param call_params: API call parameters
        :return PythonAEM Result
        """
        print(">>>>>>>")
        print(type(self.response))
        print(self.response.body)
        print(type(self.response.body))
        print("bb")
        _json = json.loads(self.response.body)
        print("aa")
        print(_json)
        response_message = self.response_spec['message'].format(**self.call_params)
        print(_json)
        data = _json['results']
        return Result(response_message, self.response, data)
