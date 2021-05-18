"""
PythonAEM is a Python API client for interacting with AEM API.
"""
import swaggeraem
from swaggeraem.apis.custom_api import CustomApi
from swaggeraem.apis.sling_api import SlingApi
import yaml
from .client import Client
from .resources.aem import Aem
from .resources.flush_agent import FlushAgent
from .resources.replication_agent import ReplicationAgent

class PythonAem:
    """
    Aem class represents an AEM client instance.
    """

    def __init__(self, conf):
        """
        Initialise a PythonAEM instance
        :param conf: <dict>
        Configuration dictionary of the following configuration values:
        - username: username used to authenticate to AEM instance, default: 'admin'
        - password: password used to authenticate to AEM instance, default: 'admin'
        - protocol: AEM instance protocol (http or https), default: 'http'
        - host: AEM instance host name, default: 'localhost'
        - port: AEM instance port, default: 4502
        """
        conf = sanitise_conf(conf)

        configuration = swaggeraem.Configuration(
            username = conf['username'],
            password = conf['password'],
            host = f'{conf["protocol"]}://{conf["host"]}:{conf["port"]}'
        )

        apis = {}
        with swaggeraem.ApiClient(configuration) as api_client:
            apis['custom'] = CustomApi(api_client)
            apis['sling'] = SlingApi(api_client)

        with open('conf/spec.yaml', 'r') as spec_stream:
            spec = yaml.safe_load(spec_stream)

        self.client = Client(apis, spec)

    def aem(self):
        """
        Create an AEM instance.
        :return: new PythonAEM Resources AEM instance
        """
        return Aem(self.client)

    def flush_agent(self, run_mode, name):
        """
        Create a flush agent instance.
        :param run_mode: AEM run mode (author or publish)
        :param name: the flush agent's name, e.g. some-flush-agent
        :return: new PythonAEM Resources FlushAgent instance
        """
        return FlushAgent(self.client, run_mode, name)

    def replication_agent(self, run_mode, name):
        """
        Create a replication agent instance.
        :param run_mode: AEM run mode (author or publish)
        :param name: the replication agent's name, e.g. some-replication-agent
        :return: new PythonAEM Resources ReplicationAgent instance
        """
        return ReplicationAgent(self.client, run_mode, name)

def sanitise_conf(conf):
    """
    Set default configuration values
    :param conf: <dict>
    :return:
    """
    conf['username'] = conf.get('username', 'admin')
    conf['password'] = conf.get('password', 'admin')
    conf['protocol'] = conf.get('protocol', 'http')
    conf['host'] = conf.get('host', 'localhost')
    conf['port'] = conf.get('port', 4502)
    return conf
