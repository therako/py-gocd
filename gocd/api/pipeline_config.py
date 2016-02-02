from gocd.api.endpoint import Endpoint

__all__ = ['PipelineConfig']


class PipelineConfig(Endpoint):
    base_path = 'go/api/admin/pipelines'
    id = 'name'
    #: The result of a job/stage has been finalised when these values are set
    final_results = ['Passed', 'Failed']

    def __init__(self, server, name):
        """A wrapper for the `Go pipeline config API`__

        .. __: https://api.go.cd/current/#pipeline-config

        Args:
          server (Server): A configured instance of
            :class:gocd.server.Server
          name (str): The name of the pipeline we're working on
        """
        self.server = server
        self.name = name

    def get(self):
        """Gets pipeline config for specified pipeline name.

        See `The pipeline config object`__ for example responses.

        .. __: https://api.go.cd/current/#the-pipeline-config-object

        Returns:
          Response: :class:`gocd.api.response.Response` object
        """
        return self._get(self.name, headers={"Accept": "application/vnd.go.cd.v1+json"})

    def edit(self, config):
        """Update pipeline config for specified pipeline name.

        .. __: https://api.go.cd/current/#edit-pipeline-config

        Returns:
          Response: :class:`gocd.api.response.Response` object
        """

        return self._request(self.name,
                             ok_status=None,
                             data=config,
                             headers={"Accept": "application/vnd.go.cd.v1+json"})

    def create(self, config):
        """Update pipeline config for specified pipeline name.

        .. __: https://api.go.cd/current/#edit-pipeline-config

        Returns:
          Response: :class:`gocd.api.response.Response` object
        """

        return self._request("",
                             ok_status=None,
                             data=config,
                             headers={"Accept": "application/vnd.go.cd.v1+json"})
