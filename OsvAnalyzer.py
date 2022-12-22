import argparse
import sys

from lib.analyze.factory import AnalyzerFactory
from lib.enum.language import Language


class OsvAnalyzer:
    def __init__(self, language, file_to_analyze, analyzer_list) -> None:
        self.language = language
        self.fileToAnalyze = file_to_analyze
        self.analyzerList = analyzer_list

    @staticmethod
    def configure_parser(parser: argparse.ArgumentParser):
        parser.add_argument('-l', '--language', type=str, required=True, choices=[Language.PHP.value])
        parser.add_argument('-f', '--file', type=str, required=True)

    def start(self):
        self.__select_analyzer().analyze(self.fileToAnalyze)

    def __select_analyzer(self):
        for analyzer in self.analyzerList:
            if analyzer.supports(self.language):
                return analyzer
        raise Exception('No analyzer found for ' + self.language)


class MainAppFactory:
    @staticmethod
    def init_app(parser: argparse.ArgumentParser) -> OsvAnalyzer:
        argumentsParsed = parser.parse_args(sys.argv[1:])

        return OsvAnalyzer(argumentsParsed.language, argumentsParsed.file, AnalyzerFactory.create_analyzer_list())



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="OsvAnalyzer",
        usage="./osvAnalyzer.py -l language -f fileToAnalyze",
        description="Analyze the dependencies file with OSV database")

    OsvAnalyzer.configure_parser(parser)

    analyzer = MainAppFactory.init_app(parser)
    analyzer.start()
