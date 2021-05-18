"""
AEM resources.
"""

class Aem:
    """
    AEM class contains API calls related to managing the AEM instance itself.
    """

    def __init__(self, client):
        """
        Initialise an AEM agent.
        :param client: PythonAEM Client
        :return new PythonAEM Resources AEM instance
        """
        self.client = client
        self.call_params = {
        }

    def get_aem_health_check(self, opts):
        """
        Retrieve AEM Health Check.
        This is a custom API and requires
        https://github.com/shinesolutions/aem-healthcheck
        to be installed.

        :param opts: optional parameters:
        - tags: comma separated tags of AEM Health Check tags
        - combine_tags_or: if true, the check needs to only pass
          one of the check tags in order to get the health check pass,
          if false, all check tags need to pass in order to get the health check pass.
        :return PythonAEM Result
        """
        self.call_params = {**self.call_params, **opts}
        return self.client.call(self.__class__.__name__, 'get_aem_health_check', self.call_params)
