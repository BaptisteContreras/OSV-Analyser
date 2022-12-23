from lib.deps.model import Dependency, PhpDependency, Vuln
from lib.enum.ecosystem import Ecosystem
from lib.enum.language import Language


class DependencyConverter:
    @staticmethod
    def convert_from_cache(dep_raw: dict) -> Dependency:
        if dep_raw["ecosystem"] == Ecosystem.PACKAGIST.value:
            return DependencyConverter.__convert_php(dep_raw)

        raise Exception("Ecosystem not supported")

    @staticmethod
    def __convert_php(dep_raw: dict) -> Dependency:
        dep = PhpDependency(dep_raw["name"], dep_raw["version"])
        DependencyConverter.__add_vulns_to_dep(dep, dep_raw["vulns"])

        return dep

    @staticmethod
    def __add_vulns_to_dep(dep: Dependency, vulns_raw: dict) -> None:
        for vuln_raw in vulns_raw:
            dep.addVuln(DependencyConverter.convert_vuln(vuln_raw))

    @staticmethod
    def convert_vuln(vuln_raw: dict) -> Vuln:
        return Vuln(vuln_raw["id"])
