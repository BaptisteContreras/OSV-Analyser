from lib.analyze.analyzer import Analyzer
from lib.analyze.php_analyzer import PhpAnalyzer
from lib.cache.factory import CacheHandlerFactory
from lib.deps.factory import DependancyFileDriverFactory
from lib.osv.factory import OsvSdkFactory


class AnalyzerFactory:
    @staticmethod
    def create_analyzer_list() -> [Analyzer]:
        return [AnalyzerFactory.create_php_analyzer()]

    @staticmethod
    def create_php_analyzer() -> Analyzer:
        return PhpAnalyzer(DependancyFileDriverFactory.create_php_file_deps_driver(), OsvSdkFactory.create_default_sdk(), CacheHandlerFactory.create_php_handler())
