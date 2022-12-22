from lib.osv.sdk import OsvApiV1, OsvSdk


class OsvSdkFactory:
    @staticmethod
    def create_default_sdk() -> OsvSdk:
        return OsvSdkFactory.create_v1()

    @staticmethod
    def create_v1() -> OsvSdk:
        return OsvApiV1()
