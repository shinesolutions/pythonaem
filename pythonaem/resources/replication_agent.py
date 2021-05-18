"""
ReplicationAgent class contains API calls related to managing an AEM replication agent.
"""

from urllib.parse import urlparse

class ReplicationAgent:
    """
    ReplicationAgent class contains API calls related to managing an AEM replication agent.
    """

    def __init__(self, client, run_mode, name):
        """
        Initialise a replication agent.
        :param client: PythonAEM Client
        :param run_mode: AEM run mode: author or publish
        :param name: the replication agent's name, e.g. some-replication-agent
        :return new PythonAEM Resources ReplicationAgent instance
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
          'transport_user': 'admin',
          'transport_password': 'admin',
          'log_level': 'error',
          'retry_delay': 30_000
        }):
        """
        Create or update a replication agent.

        :param title: replication agent title
        :param description: replication agent description
        :param dest_base_url: base URL of the agent target destination,
            e.g. https://somepublisher:4503
        :param opts: optional parameters:
        - transport_user: username for transport user, default is admin
        - transport_password: password for transport user, default is admin
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
        Delete the replication agent.

        :return PythonAEM Result
        """
        return self.client.call(self.__class__.__name__, 'delete', self.call_params)

    def exists(self):
        """
        Check whether the replication agent exists or not.
        If the replication agent  exists, this method returns a true result data,
        false otherwise.

        :return PythonAEM Result
        """
        return self.client.call(self.__class__.__name__, 'exists', self.call_params)
