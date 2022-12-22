from lib.analyze.analyzer import Analyzer
from lib.enum.language import Language


class PhpAnalyzer(Analyzer):
    def supports(self, language: str):
        return Language.PHP.value == language
