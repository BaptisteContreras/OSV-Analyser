from lib.deps.php_deps_driver import ComposerLockDriver


class DependencyFileDriverFactory:
    php_composer_lock_driver = None

    @staticmethod
    def create_php_file_deps_driver():
        if not DependencyFileDriverFactory.php_composer_lock_driver:
            DependencyFileDriverFactory.php_composer_lock_driver = ComposerLockDriver()

        return DependencyFileDriverFactory.php_composer_lock_driver
