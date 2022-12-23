from lib.deps.php_deps_driver import ComposerLockDriver


class DependancyFileDriverFactory:
    php_composer_lock_driver = None

    @staticmethod
    def create_php_file_deps_driver():
        if not DependancyFileDriverFactory.php_composer_lock_driver:
            DependancyFileDriverFactory.php_composer_lock_driver = ComposerLockDriver()

        return DependancyFileDriverFactory.php_composer_lock_driver
