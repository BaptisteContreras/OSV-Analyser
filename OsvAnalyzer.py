import argparse
import sys

from lib.analyze.analyzer import Analyzer
from lib.analyze.factory import AnalyzerFactory
from lib.enum.action import Action
from lib.enum.language import Language


class OsvAnalyzer:
    def __init__(self, language: str, file_to_analyze: str, analyzer_list: [Analyzer], action: str) -> None:
        self.language = language
        self.fileToAnalyze = file_to_analyze
        self.analyzerList = analyzer_list
        self.action = action

    @staticmethod
    def configure_parser(parser: argparse.ArgumentParser):
        parser.add_argument('-a', '--action', type=str, required=True, choices=[Action.ANALYZE.value])
        parser.add_argument('-l', '--language', type=str, required=True, choices=[Language.PHP.value])
        parser.add_argument('-f', '--file', type=str, required=True)

    def execute(self) -> int:
        if self.action == Action.ANALYZE.value:
            return self.__action_analyze()

        return 2

    def __action_analyze(self) -> int:
        should_fail = self.__select_analyzer().analyze(self.fileToAnalyze)

        if should_fail:
            return 1

        return 0

    def __select_analyzer(self):
        for analyzer in self.analyzerList:
            if analyzer.supports(self.language):
                return analyzer
        raise Exception('No analyzer found for ' + self.language)


class MainAppFactory:
    @staticmethod
    def init_app(parser: argparse.ArgumentParser) -> OsvAnalyzer:
        arguments_parsed = parser.parse_args(sys.argv[1:])

        return OsvAnalyzer(arguments_parsed.language, arguments_parsed.file, AnalyzerFactory.create_analyzer_list(), arguments_parsed.action)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="OsvAnalyzer",
        usage="./osvAnalyzer.py -a action -l language -f fileToAnalyze",
        description="Analyze the dependencies file with OSV database")

    OsvAnalyzer.configure_parser(parser)

    analyzer = MainAppFactory.init_app(parser)

    exit(analyzer.execute())
