"""
Client class makes Swagger AEM API calls and handles the response as
configured in conf/spec.yaml .
"""

from swaggeraem.exceptions import ApiException
from .error import Error
from .handlers.simple import SimpleHandler
from .response import Response
from .result import Result
from .swagger import operation_to_method

class Client:
    """
    Client class makes Swagger AEM API calls and handles the response as
    configured in conf/spec.yaml .
    """

    def __init__(self, apis, spec):
        """
        Initialise a client.
        :param apis: a dictionary of Swagger AEM client's API instances
        :param spec: pythonaem specification
        :return new Client instance
        """
        self.apis = apis
        self.spec = spec

    def call(self, clazz, action, call_params):
        """
        Make an API call using the relevant Swagger AEM API client.
        Clazz and action parameters are used to identify the action, API, and params
        from pythonaem specification, alongside the response handlers.
        Call parameters are used to construct HTTP request parameters based on the
        specification.

        :param clazz: the class name of the caller resource
        :param action: the action of the API call
        :param call_params: API call parameters
        :return PythonAEM Result
        """
        resource_name = clazz.lower()
        resource = self.spec[resource_name]
        action_spec = resource['actions'][action]

        api = self.apis[str(action_spec['api'].lower())]
        operation = action_spec['operation']

        params = []

        if 'required' in action_spec['params']:
            required_params = action_spec['params']['required']
            for key, value in required_params.items():
                params.append(value.format(**call_params))

        keyword_params = {}
        if 'optional' in action_spec['params']:
            optional_params = action_spec['params']['optional']

            if isinstance(optional_params, dict):
                for key, value in optional_params.items():
                    self.__add_optional_param(key, value, keyword_params, call_params)

            elif isinstance(optional_params, list):
                for key in optional_params:
                    self.__add_optional_param(key, None, keyword_params, call_params)

        responses_spec = {}
        if 'responses' in resource:
            responses_spec.update(resource['responses'])

        if 'responses' in action_spec:
            responses_spec.update(action_spec['responses'])

        try:
            swagger_method = operation_to_method(operation)
            swagger_http_method_name = '{}_with_http_info'.format(swagger_method)
            print(api)
            print(swagger_http_method_name)
            print(params)
            print(keyword_params)
            data, status_code, headers = getattr(
                api, swagger_http_method_name
            )(*params, **keyword_params)
            print("aaaaaaa")
            print(status_code)
            response = Response(status_code, data, headers)
        except ApiException as exception:
            response = Response(exception.status, exception.body, exception.headers)

        return self.handle(response, responses_spec, call_params)()

    # pylint: disable=no-else-return
    def handle(self, response, responses_spec, call_params):
        """
        Handle a response based on status code and a given list of response specifications.
        If none of the response specifications contains the status code, a failure result
        will then be returned.

        :param response: response containing HTTP status code, body, and headers
        :param responses_spec: a list of response specifications as configured in conf/spec.yaml
        :param call_params: API call parameters
        :return PythonAEM Result
        :raise PythonAEM Error when the response status code is unexpected
        """
        if response.status_code in responses_spec:
            response_spec = responses_spec[response.status_code]
            handler = response_spec['handler']
            handler_class = SimpleHandler(response, response_spec, call_params)
            return getattr(handler_class, handler)
        else:
            message = "Unexpected response\nstatus code: {}\nheaders: {}\nbody: {}".format(
                response.status_code, response.headers, response.body
            )
            result = Result(message, response)
            raise Error(message, result)

    # Switch boolean type  check to isinstance after integration and unit tests have better coverage
    # pylint: disable=unidiomatic-typecheck
    def __add_optional_param(self, key, value, params, call_params):
        print(key)
        print(value)
        print(call_params)
        # if there is no value in optional param spec,
        # then only add optional param that is set in call parameters
        if not value:
            if key in call_params:
                params[str(key)] = call_params[str(key)]
        # if value is provided in optional param spec,
        # then apply variable interpolation the same way as required param
        elif isinstance(value, str):
            params[str(key)] = value.format(**call_params)
        elif type(value) == bool:
            params[str(key)] = str(value).lower().format(**call_params)
        else:
            params[str(key)] = value
