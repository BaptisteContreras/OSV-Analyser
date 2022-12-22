from lib.deps.php_deps_driver import ComposerLockDriver


class DependancyFileDriverFactory:
    @staticmethod
    def create_php_file_deps_driver():
        return ComposerLockDriver()