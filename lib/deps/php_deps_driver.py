import json
from datetime import datetime

from lib.deps.file_deps_driver import FileDepsDriver
from lib.deps.model import Dependency, PhpDependency


class ComposerLockDriver(FileDepsDriver):
    def read_file(self, location: str) -> [Dependency]:
        return self.__build_dependency_collection(self.__read_file_content(location))

    def get_content_hash(self, location: str) -> str:
        return self.__read_file_content(location)["content-hash"]

    @classmethod
    def __read_file_content(self, location: str) -> dict:
        composer_lock_file = open(location, 'r')
        try:
            composer_lock_parsed = json.loads(composer_lock_file.read())
        finally:
            composer_lock_file.close()

        return composer_lock_parsed

    @classmethod
    def __build_dependency_collection(self, composer_lock_parsed) -> [Dependency]:
        packages = composer_lock_parsed["packages"]
        dependency_collection = []

        for package in packages:
            dependency_collection.append(PhpDependency.build_from_package_infos(package))

        return dependency_collection

