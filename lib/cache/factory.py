from lib.cache.cache_handler import CacheHandler, PhpCacheHandler
from lib.deps.factory import DependancyFileDriverFactory


class CacheHandlerFactory:

    @staticmethod
    def create_php_handler() -> CacheHandler:
        return PhpCacheHandler(CacheHandlerFactory.__get_default_cache_location(), DependancyFileDriverFactory.create_php_file_deps_driver())

    @staticmethod
    def __get_default_cache_location() -> str:
        return './'