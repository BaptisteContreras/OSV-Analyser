import json
from lib.deps.file_deps_driver import FileDepsDriver
from lib.deps.model import Dependency, PhpDependency


class ComposerLockDriver(FileDepsDriver):
    def read_file(self, location: str) -> [Dependency]:
        composer_lock_raw_content = self.__read_file_content(location)
        composer_lock_parsed = json.loads(composer_lock_raw_content)

        return self.__build_dependency_collection(composer_lock_parsed)

    @classmethod
    def __read_file_content(self, location: str) -> str:
        composer_lock_file = None
        try:
            composer_lock_file = open(location, 'r')
            result = composer_lock_file.read()
        finally:
            if composer_lock_file:
                composer_lock_file.close()

        return result

    @classmethod
    def __build_dependency_collection(self, composer_lock_parsed) -> [Dependency]:
        packages = composer_lock_parsed["packages"]
        dependency_collection = []

        for package in packages:
            dependency_collection.append(PhpDependency.build_from_package_infos(package))

        return dependency_collection

