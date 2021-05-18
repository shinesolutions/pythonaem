"""
FlushAgent class contains API calls related to managing an AEM flush agent.
"""

from urllib.parse import urlparse

class FlushAgent:
    """
    FlushAgent class contains API calls related to managing an AEM flush agent.
    """

    def __init__(self, client, run_mode, name):
        """
        Initialise a flush agent.
        :param client: PythonAEM Client
        :param run_mode: AEM run mode: author or publish
        :param name: the flush agent's name, e.g. some-flush-agent
        :return new PythonAEM Resources FlushAgent instance
        """
        self.client = client
        self.call_params = {
            'run_mode': run_mode,
            'name': name
        }

    def create_update(
        self,
        title,
        description,
        dest_base_url,
        opts = {
          'log_level': 'error',
          'retry_delay': 30_000
        }):
        """
        Create or update a flush agent.

        :param title: flush agent title
        :param description: flush agent description
        :param dest_base_url: base URL of the agent target destination,
            e.g. http://somedispatcher:8080
        :param opts: optional parameters:
        - log_level: error, info, debug, default is error
        - retry_delay: in milliseconds, default is 30_000
        :return PythonAEM Result
        """
        self.call_params['title'] = title
        self.call_params['description'] = description
        self.call_params['dest_base_url'] = dest_base_url

        uri = urlparse(dest_base_url)
        self.call_params['ssl'] = 'relaxed' if uri.scheme == 'https' else ''

        self.call_params = {**self.call_params, **opts}

        return self.client.call(self.__class__.__name__, 'create_update', self.call_params)

    def delete(self):
        """
        Delete the flush agent.

        :return PythonAEM Result
        """
        return self.client.call(self.__class__.__name__, 'delete', self.call_params)

    def exists(self):
        """
        Check whether the flush agent exists or not.
        If the flush agent  exists, this method returns a true result data,
        false otherwise.

        :return PythonAEM Result
        """
        return self.client.call(self.__class__.__name__, 'exists', self.call_params)
