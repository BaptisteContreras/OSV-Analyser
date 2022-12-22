import json
import requests
from lib.deps.model import Dependency, Vuln
from lib.osv.converter import DependencyConverter, VulnConverter


class OsvSdk():
    def query_batch(self, dependencies: [Dependency]):
        pass


class OsvApiV1(OsvSdk):
    def __init__(self):
        self.base = "https://api.osv.dev/v1/"
        self.queryBatchEndpoint = 'querybatch'

    def query_batch(self, dependencies: [Dependency]) -> [[Vuln]]:
        fullEndpointUrl = self.base + self.queryBatchEndpoint

        payload = {
            "queries": [query.to_json() for query in DependencyConverter.convertCollectionForApiRequest(dependencies)]
        }
        queries_response = requests.post(fullEndpointUrl, json.dumps(payload))

        if queries_response.status_code != 200:
            raise Exception("API call failed")

        i = 0
        vulns = []
        for dep_raw_vulns in json.loads(queries_response.content)["results"]:
            tmpVulns = []
            if "vulns" in dep_raw_vulns.keys():
                tmpVulns = [VulnConverter.convert_raw_result_to_vuln(raw_vuln) for raw_vuln in dep_raw_vulns["vulns"]]
                self.__add_vulns_to_dependency(dependencies[i], tmpVulns)

            vulns.append(tmpVulns)
            i += 1

        return vulns

    @classmethod
    def __add_vulns_to_dependency(self, dependency: Dependency, vulns: [Vuln]):
        for vuln in vulns:
            dependency.addVuln(vuln)
