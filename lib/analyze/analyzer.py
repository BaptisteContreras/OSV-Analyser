import itertools

from lib.deps.file_deps_driver import FileDepsDriver
from lib.osv.sdk import OsvApiV1, OsvSdk


class Analyzer:
    def __init__(self, file_driver: FileDepsDriver, sdk: OsvSdk):
        self.fileDriver = file_driver
        self.osvSdk = sdk

    def supports(self, language: str):
        pass

    def analyze(self, file_to_analyze: str):
        deps = self.fileDriver.read_file(file_to_analyze)
        vulns = self.osvSdk.query_batch(deps)

        vulnsFound = []
        for subVulns in vulns:
            if subVulns:
                [vulnsFound.append(vuln) for vuln in subVulns]

        if vulnsFound:
            print(str(len(vulnsFound)) + " vulns found")
            [print(vuln) for vuln in vulnsFound]

        [print(dep) for dep in deps]
