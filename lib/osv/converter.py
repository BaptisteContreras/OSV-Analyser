from lib.deps.model import Dependency, Vuln
from lib.osv.model import Query


class DependencyConverter:

    @staticmethod
    def convertCollectionForApiRequest(dependencies: [Dependency]) -> [Query]:
        return [DependencyConverter.convertForApiRequest(dependency) for dependency in dependencies]

    @staticmethod
    def convertForApiRequest(dependency: Dependency) -> Query:
        return Query.buildWithVersion(
            version=dependency.version,
            name=dependency.name,
            ecosystem=dependency.ecosystem.value)


class VulnConverter:

    @staticmethod
    def convert_raw_result_to_vuln(raw_result: dict) -> Vuln:
        return Vuln(raw_result["id"])
