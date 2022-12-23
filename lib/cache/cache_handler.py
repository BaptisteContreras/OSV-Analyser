import json
from datetime import datetime
from os.path import exists

from lib.cache.converter import DependencyConverter
from lib.deps.file_deps_driver import FileDepsDriver
from lib.deps.model import Dependency


class CacheHandler:

    def __init__(self, cache_location, file_driver: FileDepsDriver, cache_file_name):
        self.cacheLocation = cache_location
        self.fileDriver = file_driver
        self.cacheFileName = cache_file_name

    def load(self, file_to_analyze: str) -> [Dependency]:
        cache_full_path = self.__get_cache_full_path()

        if not exists(cache_full_path):
            return []

        cache_json = self.__read_cache_file(cache_full_path)

        if "content_hash" in cache_json.keys():
            if self.fileDriver.get_content_hash(file_to_analyze) != cache_json["content_hash"]:
                return []

        deps = []
        try:
            for dep_raw in cache_json["deps"]:
                deps.append(DependencyConverter.convert_from_cache(dep_raw))
        except Exception:
            self.__write_to_cache('')

        return deps

    def save(self, dependency_collection: [Dependency], file_to_analyze: str) -> None:
        to_write = {
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "content_hash": self.fileDriver.get_content_hash(file_to_analyze),
            "deps": [dep.to_cache() for dep in dependency_collection]
        }

        self.__write_to_cache(json.dumps(to_write))

    def __read_cache_file(self, cache_full_path: str) -> dict:
        cache_file = open(cache_full_path, 'r')
        try:
            cache_raw = cache_file.read()
            json_result = json.loads(cache_raw)
        except json.decoder.JSONDecodeError:
            return {}
        finally:
            cache_file.close()

        return json_result

    def __get_cache_full_path(self) -> str:
        return self.cacheLocation + self.cacheFileName

    def __write_to_cache(self, content: str) -> None:
        cache_file = open(self.__get_cache_full_path(), 'w')
        try:
            cache_file.write(content)
        finally:
            cache_file.close()



class PhpCacheHandler(CacheHandler):
    def __init__(self, cache_location, file_driver: FileDepsDriver):
        super().__init__(cache_location, file_driver, ".osv_php_cache.json")
