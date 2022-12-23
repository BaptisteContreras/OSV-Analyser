from lib.enum.ecosystem import Ecosystem

class Vuln:
    def __init__(self, id: str):
        self.id = id
    def __str__(self) -> str:
        return "Vuln #" + self.id
    def to_cache(self) -> dict:
        return {
            "id": self.id
        }

class Dependency:
    def __init__(self, name: str, version: str, ecosystem: Ecosystem):
        self.name = name
        self.version = version
        self.ecosystem = ecosystem
        self.vulns = []

    def to_cache(self) -> dict:
        return {
            "name": self.name,
            "version": self.version,
            "ecosystem": self.ecosystem.value,
            "vulns": [vuln.to_cache() for vuln in self.vulns]
        }
    def __str__(self) -> str:
        return self.ecosystem.value + " |  Vulns : " + ' '.join([vuln.__str__() for vuln in self.vulns])

    def addVuln(self, vuln: Vuln):
        self.vulns.append(vuln)

class PhpDependency(Dependency):
    def __init__(self, name: str, version: str):
        super().__init__(name, version, Ecosystem.PACKAGIST)

    @staticmethod
    def build_from_package_infos(package_infos) -> __init__:
        return PhpDependency(package_infos["name"], package_infos["version"])

    def __str__(self) -> str:
        return self.name + " " + self.version + " " + super().__str__()