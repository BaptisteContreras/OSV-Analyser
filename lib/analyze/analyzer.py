import itertools

from lib.cache.cache_handler import CacheHandler
from lib.deps.file_deps_driver import FileDepsDriver
from lib.osv.sdk import OsvApiV1, OsvSdk


class Analyzer:
    def __init__(self, file_driver: FileDepsDriver, sdk: OsvSdk, cache_handler: CacheHandler):
        self.fileDriver = file_driver
        self.osvSdk = sdk
        self.cacheHandler = cache_handler

    def supports(self, language: str) -> bool:
        pass

    def analyze(self, file_to_analyze: str) -> bool:
        deps = self.fileDriver.read_file(file_to_analyze)
        vulns = self.osvSdk.query_batch(deps)

        vulns_found = []
        for sub_vulns in vulns:
            if sub_vulns:
                [vulns_found.append(vuln) for vuln in sub_vulns]

        if vulns_found:
            print(str(len(vulns_found)) + " vulns found")
            [print(vuln) for vuln in vulns_found]

        [print(dep) for dep in deps]

        self.cacheHandler.save(deps, file_to_analyze)

        return len(vulns_found) > 0
