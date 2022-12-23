from datetime import datetime

from lib.deps.model import Dependency


class FileDepsDriver:

    def read_file(self, location: str) -> [Dependency]:
        pass

    def get_content_hash(self, location: str) -> str:
        pass
